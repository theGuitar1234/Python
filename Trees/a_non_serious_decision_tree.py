import numpy as np
import sys


class Node:
    def __init__(self, feature=None, threshold=None):
        self.feature = feature
        self.threshold = threshold
        self.left = None
        self.right = None
        self.value = None


class ANonSeriousDecisionTree:
    def __init__(self, max_depth=3, categorical=False, adjacent=False):
        self.root = None
        self.max_depth = max_depth
        self.categorical = categorical
        self.adjacent = adjacent

    def fit(self, X, y):
        if X.shape[0] != y.shape[0]:
            raise ValueError(
                f"X and y must match in shapes : {X.shape[0]} != {y.shape[0]}"
            )
        self.root = self._build_tree(X, y, depth=0)

    def _build_tree(self, X, y, depth):
        node = Node()

        if depth >= self.max_depth or len(set(y)) == 1:
            node.value = self._majority_class(y)
            return node
        feature, threshold = self._choose_split(X, y)

        if feature is None:
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
        node.left = self._build_tree(X[left_mask], y[left_mask], depth + 1)
        node.right = self._build_tree(X[right_mask], y[right_mask], depth + 1)

        return node

    def _choose_split(self, X, y):
        best_feature = None
        best_threshold = None
        best_gini = float("inf")

        _, features = X.shape
        for feature in range(features):
            values = np.sort(X[:, feature])
            order = np.argsort(values)
            sorted_values = values[order]
            categories = np.unique(sorted_values)

            if not self.categorical:
                if self.adjacent:
                    sorted_y = y[order]
                    mask = sorted_y[1:] != sorted_y[:-1]
                    # mask = self.adjacent_classes(sorted_y)
                    categories = (categories[1:][mask] + categories[:-1][mask]) / 2
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

                __gini_left = self.gini(left_group)
                __gini_right = self.gini(right_group)

                weighted_gini = self.gini_weighted(
                    __gini_left, __gini_right, len(left_group), len(right_group)
                )

                if weighted_gini < best_gini:
                    best_gini = weighted_gini
                    best_feature = feature
                    best_threshold = category
        return best_feature, best_threshold

    # def adjacent_classes(self, sorted_y):
    #     mask = sorted_y[1:] != sorted_y[:-1]
    #     return mask

    def gini(self, y):
        if len(y) == 0:
            return 0
        _, counts = np.unique(y, return_counts=True)
        proportions = counts / len(y)
        return 1 - np.sum(proportions**2)

    def gini_weighted(self, gini_left, gini_right, left_size, right_size):
        total_size = left_size + right_size
        return (left_size / total_size) * gini_left + (
            right_size / total_size
        ) * gini_right

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
        X = np.array(X)
        return [self.predict_one(x) for x in X]

    def _majority_class(self, y):
        return max(set(y), key=list(y).count)


if __name__ == "__main__":
    tree = ANonSeriousDecisionTree(categorical=False, adjacent=True)
    # X = [
    #     [2, 1],
    #     [2, 0],
    #     [2, 0],
    #     [1, 1],
    #     [1, 0],
    #     [0, 1],
    #     [0, 0],
    #     [0, 0],
    # ]
    # y = [1, 1, 1, 1, 0, 1, 0, 0]
    X = [
        [60],
        [70],
        [75],
        [85],
        [90],
        [95],
        [100],
        [110],
        [120],
        [125],
    ]
    y = [0, 0, 0, 1, 1, 1, 0, 0, 0, 0]

    X = np.asarray(X, dtype=np.int32)
    y = np.asarray(y, dtype=np.int32)

    tree.fit(X, y)
    input = [
        [72],
        [96],
        [200],
    ]
    print(tree.predict(input))
