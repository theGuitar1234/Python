from enum import Enum

import numpy as np
import sys
import os
from sklearn.model_selection import train_test_split
from sklearn import datasets
from sklearn.metrics import confusion_matrix
from sklearn.model_selection import StratifiedKFold
import numpy as np
import copy
import math


class Node:
    def __init__(self, feature=None, threshold=None):
        self.feature = feature
        self.threshold = threshold
        self.is_leaf = False
        self.left = None
        self.right = None
        self.value = None
        self.majority_class = None
        self.number_of_samples = None
        self.number_of_classes = None
        self.number_of_leaves = None
        self.leaf_error = None
        self.subtree_error = None


class ANonSeriousDecisionTree:

    class InformationGain(Enum):
        GINI = 1
        ENTROPY = 2

    def __init__(
        self,
        minimum_population_size=2,
        minimum_split_size=1,
        minimum_gain=0.001,
        max_depth=3,
        categorical=False,
        adjacent=False,
        log=False,
        information_gain=None,
    ):
        self.root = None
        self.max_depth = max_depth
        self.categorical = categorical
        self.adjacent = adjacent
        self.minimum_population_size = minimum_population_size
        self.minimum_split_size = minimum_split_size
        self.minimum_gain = minimum_gain
        self.information_gain = information_gain
        self.log = log

    def fit(self, X, y):
        if y.ndim == 2:
            y = np.argmax(y, axis=1)
        if X.shape[0] != y.shape[0]:
            raise ValueError(
                f"X and y must match in shapes : {X.shape[0]} != {y.shape[0]}"
            )
        self.X_train_ = X
        self.y_train_ = y
        self.root = self._build_tree(X, y, depth=0)
        return self

    def _build_tree(self, X, y, depth):
        node = Node()
        node.majority_class = self._majority_class(y)
        node.number_of_samples = len(y)
        node.leaf_error = self._leaf_error(y) 

        if (
            depth >= self.max_depth
            or len(set(y)) == 1
            or len(y) <= self.minimum_population_size
        ):
            node.is_leaf = True
            node.value = self._majority_class(y)
            return node
        feature, threshold = self._choose_split(X, y)

        if self.log:
            print(
                f"Fitting the tree... [Best Feature : {feature}] [Best Split : {threshold}]"
            )

        if feature is None:
            node.is_leaf = True
            node.value = self._majority_class(y)
            return node
        node.feature = feature
        node.threshold = threshold

        if self.categorical:
            left_mask = X[:, feature] == threshold
            right_mask = X[:, feature] != threshold
        else:
            left_mask = X[:, feature] > threshold
            right_mask = X[:, feature] <= threshold

        if (
            len(X[left_mask]) < self.minimum_split_size
            or len(X[right_mask]) < self.minimum_split_size
        ):
            node.is_leaf = True
            node.value = self._majority_class(y)
            return node

        node.left = self._build_tree(X[left_mask], y[left_mask], depth + 1)
        node.right = self._build_tree(X[right_mask], y[right_mask], depth + 1)

        return node

    def calculate_error(self, node):
        if node is None:
            return

        if node.is_leaf or node.value is not None:
            node.number_of_leaves = 1
            node.subtree_error = node.leaf_error
            return

        self.calculate_error(node.left)
        self.calculate_error(node.right)

        node.number_of_leaves = node.left.number_of_leaves + node.right.number_of_leaves
        node.subtree_error = node.left.subtree_error + node.right.subtree_error

    def weakest_node(self, node):
        if (
            node is None
            or node.is_leaf
            or node.value is not None
            or node.number_of_leaves <= 1
        ):
            return None, float("inf")

        alpha = (node.leaf_error - node.subtree_error) / (node.number_of_leaves - 1)

        left_node, left_alpha = self.weakest_node(node.left)
        right_node, right_alpha = self.weakest_node(node.right)

        weakest = node
        weakest_alpha = alpha

        if left_alpha < weakest_alpha:
            weakest = left_node
            weakest_alpha = left_alpha
        if right_alpha < weakest_alpha:
            weakest = right_node
            weakest_alpha = right_alpha

        return weakest, weakest_alpha

    def prune_reduced_error(self, node, X_val, y_val):
        if node is None:
            return
        if node.value is not None:
            return

        if self.categorical:
            left_mask = X_val[:, node.feature] == node.threshold
            right_mask = X_val[:, node.feature] != node.threshold
        else:
            left_mask = X_val[:, node.feature] > node.threshold
            right_mask = X_val[:, node.feature] <= node.threshold

        self._prune_node(node.left, X_val[left_mask], y_val[left_mask])
        self._prune_node(node.right, X_val[right_mask], y_val[right_mask])

        if len(y_val) == 0:
            return

        subtree_predictions = np.array([self.predict_one(x, node) for x in X_val])
        subtree_accuracy = np.mean(subtree_predictions == y_val)

        leaf_predictions = np.full_like(y_val, node.majority_class)
        leaf_accuracy = np.mean(leaf_predictions == y_val)

        if leaf_accuracy >= subtree_accuracy:
            self._prune_node(node)

    def prune_post_complexity(self, X_val, y_val):
        candidates = []
        current_tree = copy.deepcopy(self)

        while True:
            current_tree.calculate_error(current_tree.root)
            candidates.append(copy.deepcopy(current_tree))
            weakest, alpha = current_tree.weakest_node(current_tree.root)

            if weakest is None or alpha == float("inf"):
                break
            self._prune_node(weakest)

        best_tree = None
        best_accuracy = -1

        for candidate in candidates:
            _, accuracy = candidate.evaluate_dataset(X_val, y_val)
            if accuracy > best_accuracy:
                best_accuracy = accuracy
                best_tree = candidate
        self.root = best_tree.root

        return self
    
    def prune_pessimistic(self):
        self._prune_node_pessimistic(self.root)
        return self
    
    def prune_error_based(self, confidence_factor=0.25, subtree_raising=True):
        self._prune_error_based_node(
            self.root,
            self.X_train_,
            self.y_train_,
            confidence_factor,
            subtree_raising,
        )
        return self

    def _prune_error_based_node(self, node, X_node, y_node, confidence_factor, subtree_raising):
        if node is None or node.is_leaf or node.value is not None:
            return
        X_left, y_left, X_right, y_right = self._route_node_data(node, X_node, y_node)
        
        self._prune_error_based_node(node.left, X_left, y_left, confidence_factor, subtree_raising)
        self._prune_error_based_node(node.right, X_right, y_right, confidence_factor, subtree_raising)
        
        N = len(y_node)
        tree_errors = self._count_errors(node, X_node, y_node)
        tree_estimate = N * self.ucf(tree_errors, N, confidence_factor)
        majority, leaf_errors = self._leaf_error(y_node)
        leaf_estimate = N * self.ucf(leaf_errors, N, confidence_factor)
        
        raised_estimate = float("inf")
        raised_subtree = None
        
        if subtree_raising and node.left is not None and node.right is not None:
            if len(y_left) >= len(y_right):
                raised_subtree = node.left
            else:
                raised_subtree = node.right
            raised_errors = self._count_errors(raised_subtree, X_node, y_node)
            raised_estimate = N * self.ucf(raised_errors, N, confidence_factor)
        
        if leaf_estimate <= tree_estimate and leaf_estimate <= raised_estimate:
            node.is_leaf = True
            node.value = majority
            node.majority_class = majority
            node.left = None
            node.right = None
            node.feature = None
            node.threshold = None
            node.number_of_leaves = 1
        elif raised_estimate < tree_estimate and raised_estimate < leaf_estimate:
            node.feature = raised_subtree.feature
            node.threshold = raised_subtree.threshold
            node.left = raised_subtree.left
            node.right = raised_subtree.right
            node.value = raised_subtree.value
            node.is_leaf = raised_subtree.is_leaf
            
            node.majority_class, node.leaf_error =  self._leaf_error(y_node)
            node.number_of_samples = len(y_node)
        else:
            pass

    def _route_node_data(self, node, X, y):
        if self.categorical:
            left_mask = X[:, node.featre] == node.threshold
            right_mask = X[:, node.feature] != node.threshold
        else:
            left_mask = X[:, node.feature] > node.threshold
            right_mask = X[:, node.feature] <= node.threshold
        return X[left_mask], y[left_mask], X[right_mask], y[right_mask]
    
    def _count_errors(self, node, X, y):
        predictions = np.array([self.predict_one(x, node) for x in X])
        return np.sum(predictions != y)
    
    def _leaf_error(self, y):
        majority = self._majority_class(y)
        errors = np.sum(y != majority)
        return majority, errors
    
    def ucf(self, errors, total, confidence_factor=0.25):
        if total == 0:
            return 0.0
        if errors == 0:
            return 1.0 - confidence_factor ** (1.0 / total)
        if errors == total:
            return 1.0
        
        low = errors / total
        high = 1.0
        
        while high - low > 1e-12:
            mid = (low + high) / 2
            probability = self.binomial_cdf(errors, total, mid)
            if probability > confidence_factor:
                low = mid
            else:
                high = mid
        return high
    
    def binomial_cdf(self, errors, total, p):
        return sum(
            math.comb(total, i) * (p ** i) * ((1 - p) ** (total - i))
            for i in range(errors + 1)
        )
    
    def _prune_node(self, node):
        node.is_leaf = True
        node.number_of_leaves = 1
        node.subtree_error = node.leaf_error
        node.left = None
        node.right = None
        node.feature = None
        node.threshold = None
        node.value = node.majority_class

    def _prune_node_pessimistic(self, node):
        if node is None:
            return
        if node.value is not None:
            self._prune_node(node)
            return
        
        self._prune_node_pessimistic(node.left)
        self._prune_node_pessimistic(node.right)
        
        node.number_of_leaves = node.left.number_of_leaves + node.right.number_of_leaves
        node.subtree_error = node.left.subtree_error + node.right.subtree_error
        
        leaf_pessimistic_error = node.leaf_error + 0.5
        subtree_pessimistic_error = node.subtree_error + 0.5 + node.number_of_leaves
        
        standart_error = math.sqrt(
            (subtree_pessimistic_error * (node.number_of_samples - subtree_pessimistic_error)) / node.number_of_samples
        )
        
        if leaf_pessimistic_error <= subtree_pessimistic_error + standart_error:
            self._prune_node(node)

    def _choose_split(self, X, y):
        best_feature = None
        best_threshold = None
        best_gain = float("inf")

        _, features = X.shape
        for feature in range(features):
            values = X[:, feature]
            order = np.argsort(values)
            sorted_values = values[order]
            categories = np.unique(sorted_values)

            if not self.categorical:
                if self.adjacent:
                    sorted_y = y[order]
                    mask = sorted_y[1:] != sorted_y[:-1]
                    mask &= sorted_values[1:] != sorted_values[:-1]
                    categories = (
                        sorted_values[1:][mask] + sorted_values[:-1][mask]
                    ) / 2
                else:
                    categories = (categories[1:] + categories[:-1]) / 2
            for category in categories:
                if self.categorical:
                    left_mask = values == category
                    right_mask = values != category
                else:
                    left_mask = values > category
                    right_mask = values <= category
                if np.sum(left_mask) == 0 or np.sum(right_mask) == 0:
                    continue
                left_group = y[left_mask]
                right_group = y[right_mask]

                match self.information_gain:
                    case self.InformationGain.GINI:
                        __left = self.gini(left_group)
                        __right = self.gini(right_group)
                    case self.InformationGain.ENTROPY:
                        __left = self.entropy(left_group)
                        __right = self.entropy(right_group)
                    case _:
                        raise ValueError(
                            f"Unsupported Information Gain, supported values are {list(self.InformationGain)}"
                        )

                weighted_gain = self.weighted_gain(
                    __left, __right, len(left_group), len(right_group)
                )

                if weighted_gain < best_gain:
                    best_gain = weighted_gain
                    best_feature = feature
                    best_threshold = category

        if best_feature is None:
            return None, None

        match self.information_gain:
            case self.InformationGain.GINI:
                __parent_impurity = self.gini(y)
            case self.InformationGain.ENTROPY:
                __parent_impurity = self.entropy(y)
            case _:
                raise ValueError(
                    f"Unsupported Information Gain, supported values are {list(self.InfomrationGain)}"
                )

        if __parent_impurity - best_gain < self.minimum_gain:
            return None, None
        return best_feature, best_threshold

    def gini(self, y):
        if len(y) == 0:
            return 0
        _, counts = np.unique(y, return_counts=True)
        proportions = counts / len(y)
        return 1 - np.sum(proportions**2)

    def entropy(self, y):
        if len(y) == 0:
            return 0
        _, counts = np.unique(y, return_counts=True)
        proportions = counts / len(y)
        return -np.sum(proportions * np.log2(proportions))

    def weighted_gain(self, left, right, left_size, right_size):
        total_size = left_size + right_size
        return (left_size / total_size) * left + (right_size / total_size) * right

    def predict_one(self, x, node=None):
        if node is None:
            node = self.root

        if node.value is not None:
            return node.value

        if self.categorical:
            if x[node.feature] == node.threshold:
                return self.predict_one(x, node.left)
            else:
                return self.predict_one(x, node.right)
        else:
            if x[node.feature] > node.threshold:
                return self.predict_one(x, node.left)
            else:
                return self.predict_one(x, node.right)

    def predict(self, X):
        return np.array([self.predict_one(x) for x in X])

    def _majority_class(self, y):
        values, counts = np.unique(y, return_counts=True)
        return values[np.argmax(counts)]

    def evaluate_dataset(self, X, y):
        if y.ndim == 2:
            y = np.argmax(y, axis=1)

        predictions = np.asarray(self.predict(X))
        accuracy = np.mean(predictions == y) * 100.0

        return predictions, accuracy

    @classmethod
    def generate_config(cls, max_depth, max_gain=None):
        configs = []
        for max_depth in [i for i in range(max_depth + 1)]:
            for minimum_gain in [0.0, 0.001, 0.01, 0.05]:
                for information_gain in [
                    cls.InformationGain.GINI,
                    cls.InformationGain.ENTROPY,
                ]:
                    configs.append(
                        {
                            "max_depth": max_depth,
                            "minimum_gain": minimum_gain,
                            "information_gain": information_gain,
                        }
                    )
        return configs

    @staticmethod
    def validate_tree(configs):
        best_tree = None

        best_config = None
        best_val_accuracy = -1

        for config in configs:
            tree = ANonSeriousDecisionTree(
                minimum_population_size=2,
                minimum_split_size=1,
                minimum_gain=config["minimum_gain"],
                max_depth=config["max_depth"],
                categorical=False,
                adjacent=True,
                information_gain=config["information_gain"],
            )

            tree.fit(X_train, y_train)

            _, train_accuracy = tree.evaluate_dataset(X_train, y_train)
            _, val_accuracy = tree.evaluate_dataset(X_val, y_val)

            print(config, f"Train: {train_accuracy:.2f}%", f"Val: {val_accuracy:.2f}%")

            if val_accuracy > best_val_accuracy:
                best_val_accuracy = val_accuracy
                best_tree = tree
                best_config = config
        return best_val_accuracy, best_tree, best_config

    @staticmethod
    def cross_validate_tree(X, y, config, splits=5):
        skf = StratifiedKFold(n_splits=splits, shuffle=True, random_state=42)

        scores = []

        for train_index, val_index in skf.split(X, y):
            X_train, X_val = X[train_index], X[val_index]
            y_train, y_val = y[train_index], y[val_index]

            tree = ANonSeriousDecisionTree(
                minimum_population_size=2,
                minimum_split_size=1,
                minimum_gain=config["minimum_gain"],
                max_depth=config["max_depth"],
                categorical=False,
                adjacent=True,
                information_gain=config["information_gain"],
            )

            tree.fit(X_train, y_train)
            scores.append(tree.evaluate_dataset(X_val, y_val)[1])

        return np.mean(scores)

    @classmethod
    def choose_best_cross_validation(cls, X_train_val, y_train_val, config, splits=5):
        best_config = None
        best_cv_score = -1
        for config in configs:
            cv_score = cls.cross_validate_tree(
                X_train_val, y_train_val, config, splits=splits
            )
            print(config, f"CV Score: {cv_score:.2f}%")
            if cv_score > best_cv_score:
                best_cv_score = cv_score
                best_config = config
        print("\nBest config:", best_config)
        print("Best CV score:", best_cv_score)
        final_tree = ANonSeriousDecisionTree(
            minimum_population_size=2,
            minimum_split_size=1,
            minimum_gain=best_config["minimum_gain"],
            max_depth=best_config["max_depth"],
            categorical=False,
            adjacent=True,
            information_gain=best_config["information_gain"],
        )
        final_tree.fit(X_train_val, y_train_val)
        return final_tree


if __name__ == "__main__":

    dataset = datasets.load_wine()
    X = dataset.data
    y = dataset.target

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=0.20, random_state=42, stratify=y
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=0.25, random_state=42, stratify=y_train_val
    )

    # 60% training
    # 20% validation
    # 20% test

    configs = ANonSeriousDecisionTree.generate_config(max_depth=10)

    final_tree = ANonSeriousDecisionTree.choose_best_cross_validation(
        X_train_val, y_train_val, configs
    )
    _, final_test_accuracy = final_tree.evaluate_dataset(X_test, y_test)

    print(f"\nFinal Test Accuracy: {final_test_accuracy}%")

    print("\nPruning the tree...")
    final_tree.prune_error_based()

    print(
        "After pruning Validation Accuracy:",
        final_tree.evaluate_dataset(X_val, y_val)[1],
    )
    print("Final test accuracy:", final_tree.evaluate_dataset(X_test, y_test)[1])

    # best_val_accuracy, best_tree, best_config = ANonSeriousDecisionTree.validate_tree(
    #     configs
    # )

    # print("\nBest config:", best_config)
    # print("Best validation accuracy:", best_val_accuracy)

    # _, test_accuracy = best_tree.evaluate_dataset(X_test, y_test)
    # print(f"\nTest Accuracy: {test_accuracy}")
