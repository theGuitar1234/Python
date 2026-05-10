#!/usr/bin/env python3
"""Docstring."""


import numpy as np


class Node:
    """Docstring."""

    def __init__(self,
                 feature=None,
                 threshold=None,
                 left_child=None,
                 right_child=None,
                 is_root=False, depth=0):
        """Docstring."""
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        """Docstring."""
        max_depth = self.depth

        if self.left_child is not None:
            max_depth = max(max_depth, self.left_child.max_depth_below())

        if self.right_child is not None:
            max_depth = max(max_depth, self.right_child.max_depth_below())

        return max_depth

    def count_nodes_below(self, only_leaves=False):
        """Docstring."""
        count = 0 if only_leaves else 1

        if self.left_child is not None:
            count += self.left_child.count_nodes_below(
                only_leaves=only_leaves)

        if self.right_child is not None:
            count += self.right_child.count_nodes_below(
                only_leaves=only_leaves)

        return count

    def left_child_add_prefix(self, text):
        """Docstring."""
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"
        for x in lines[1:]:
            new_text += ("    |  " + x) + "\n"
        return new_text

    def right_child_add_prefix(self, text):
        """Docstring."""
        lines = text.split("\n")
        new_text = "    +--" + lines[0] + "\n"
        for x in lines[1:]:
            new_text += ("       " + x) + "\n"
        return new_text

    def __str__(self):
        """Return a printable representation of the subtree."""
        if self.is_root:
            text = (
                f"root [feature={self.feature}, "
                f"threshold={self.threshold}]"
            )
        else:
            text = (
                f"-> node [feature={self.feature}, "
                f"threshold={self.threshold}]"
            )

        if self.left_child is not None:
            text += "\n" + self.left_child_add_prefix(
                str(self.left_child).rstrip("\n")
            )

        if self.right_child is not None:
            if self.left_child is None:
                text += "\n"
            text += self.right_child_add_prefix(
                str(self.right_child).rstrip("\n")
            )

        return text

    def get_leaves_below(self):
        """Return all leaves in this subtree."""
        leaves = []

        if self.left_child is not None:
            leaves.extend(self.left_child.get_leaves_below())

        if self.right_child is not None:
            leaves.extend(self.right_child.get_leaves_below())

        return leaves

    def update_bounds_below(self):
        """Docstring."""
        if self.is_root:
            self.upper = {0: np.inf}
            self.lower = {0: -np.inf}

        for child in [self.left_child, self.right_child]:
            if child is None:
                continue

            child.lower = dict(self.lower)
            child.upper = dict(self.upper)

            if child is self.left_child:
                prev = child.lower.get(self.feature, -np.inf)
                child.lower[self.feature] = max(prev, self.threshold)
            else:
                prev = child.upper.get(self.feature, np.inf)
                child.upper[self.feature] = min(prev, self.threshold)

        for child in [self.left_child, self.right_child]:
            if child is not None:
                child.update_bounds_below()

    def update_indicator(self):
        """Docstring."""

        def is_large_enough(x):
            """Docstring."""
            if (
                not hasattr(self, "lower")
                or self.lower is None or len(self.lower) == 0
            ):
                return np.ones(x.shape[0], dtype=bool)
            checks = np.array([
                np.greater(x[:, key], self.lower[key])
                for key in self.lower.keys()
            ])
            return np.all(checks, axis=0)

        def is_small_enough(x):
            """Docstring."""
            if (
                not hasattr(self, "upper")
                or self.upper is None or len(self.upper) == 0
            ):
                return np.ones(x.shape[0], dtype=bool)
            checks = np.array([
                np.less_equal(x[:, key], self.upper[key])
                for key in self.upper.keys()
            ])
            return np.all(checks, axis=0)
        self.indicator = lambda x: np.all(
            np.array([is_large_enough(x), is_small_enough(x)]),
            axis=0,
        )

    def pred(self, x):
        """Docstring."""
        if x[self.feature] > self.threshold:
            return self.left_child.pred(x)
        return self.right_child.pred(x)


class Leaf(Node):
    """Docstring."""
    def __init__(self, value, depth=None):
        """Docstring."""
        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        """Docstring."""
        return self.depth

    def count_nodes_below(self, only_leaves=False):
        """Docstring."""
        return 1

    def __str__(self):
        """Docstring."""
        return (f"-> leaf [value={self.value}]")

    def get_leaves_below(self):
        """Return this leaf as a one-item list."""
        return [self]

    def update_bounds_below(self):
        """Leaf: nothing to propagate further."""
        pass

    def pred(self, x):
        """Docstring."""
        return self.value


class Decision_Tree():
    """Docstring."""
    def __init__(self,
                 max_depth=10,
                 min_pop=1,
                 seed=0,
                 split_criterion="random",
                 root=None):
        """Docstring."""
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.target = None
        self.max_depth = max_depth
        self.min_pop = min_pop
        self.split_criterion = split_criterion
        self.predict = None

    def __str__(self):
        """Docstring."""
        return self.root.__str__()

    def depth(self):
        """Docstring."""
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """Docstring."""
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def get_leaves(self):
        """Return all leaves in the tree."""
        return self.root.get_leaves_below()

    def update_bounds(self):
        """Compute bounds for all nodes/leaves."""
        self.root.update_bounds_below()

    def update_predict(self):
        """Docstring."""
        self.update_bounds()
        leaves = self.get_leaves()
        for leaf in leaves:
            leaf.update_indicator()
        values = np.array([leaf.value for leaf in leaves], dtype=int)

        def predict_func(A):
            """Docstring."""
            indicators = np.array(
                [leaf.indicator(A) for leaf in leaves],
                dtype=int
            )
            return values @ indicators
        self.predict = predict_func

    def pred(self, x):
        """Docstring."""
        return self.root.pred(x)

    def np_extrema(self, arr):
        """Docstring."""
        return np.min(arr), np.max(arr)

    def random_split_criterion(self, node):
        """Docstring."""
        diff = 0
        while diff == 0:
            feature = self.rng.integers(0, self.explanatory.shape[1])
            vals = self.explanatory[:, feature][node.sub_population]
            feature_min, feature_max = self.np_extrema(vals)
            diff = feature_max - feature_min
        x = self.rng.uniform()
        threshold = (1 - x) * feature_min + x * feature_max
        return feature, threshold

    def fit(self, explanatory, target, verbose=0):
        """Docstring."""
        if self.split_criterion == "random":
            self.split_criterion = self.random_split_criterion
        else:
            self.split_criterion = self.Gini_split_criterion
        self.explanatory = explanatory
        self.target = target
        self.root.sub_population = np.ones_like(self.target, dtype="bool")
        self.fit_node(self.root)
        self.update_predict()
        if verbose == 1:
            str = self.count_nodes(only_leaves=True)
            str2 = self.accuracy(self.explanatory, self.target)
            print(
                f"""  Training finished.
    - Depth                     : {self.depth()}
    - Number of nodes           : {self.count_nodes()}
    - Number of leaves          : {str}
    - Accuracy on training data : {str2}"""
            )

    def fit_node(self, node):
        """Docstring."""
        node.feature, node.threshold = self.split_criterion(node)
        feat_col = self.explanatory[:, node.feature]
        go_left = feat_col > node.threshold
        left_population = node.sub_population & go_left
        right_population = node.sub_population & (~go_left)
        child_depth = node.depth + 1

        def is_leaf_population(sub_pop):
            """Docstring."""
            n = np.sum(sub_pop)
            if n < self.min_pop:
                return True
            if child_depth >= self.max_depth:
                return True
            y = self.target[sub_pop]
            if y.size > 0 and np.min(y) == np.max(y):
                return True
            return False
        if is_leaf_population(left_population):
            node.left_child = self.get_leaf_child(node, left_population)
        else:
            node.left_child = self.get_node_child(node, left_population)
            self.fit_node(node.left_child)
        if is_leaf_population(right_population):
            node.right_child = self.get_leaf_child(node, right_population)
        else:
            node.right_child = self.get_node_child(node, right_population)
            self.fit_node(node.right_child)

    def get_leaf_child(self, node, sub_population):
        """Docstring."""
        y = self.target[sub_population]
        value = int(np.argmax(np.bincount(y)))
        leaf_child = Leaf(value)
        leaf_child.depth = node.depth + 1
        leaf_child.sub_population = sub_population
        leaf_child.subpopulation = sub_population
        return leaf_child

    def get_node_child(self, node, sub_population):
        """Docstring."""
        n = Node()
        n.depth = node.depth + 1
        n.sub_population = sub_population
        return n

    def accuracy(self, test_explanatory, test_target):
        """Docstring."""
        preds = self.predict(test_explanatory)
        return np.sum(np.equal(preds, test_target)) / test_target.size

$ cat 7-main_2.py
#!/usr/bin/env python3

Decision_Tree = __import__('7-build_decision_tree').Decision_Tree
import numpy as np
import matplotlib.pyplot as plt

#                                     #########################
#                                     # Generating examples : #
#                                     #########################

def circle_of_clouds(n_clouds, n_objects_by_cloud, radius=1, sigma=None, seed=0, angle=0):
    """
    This function returns a dataset made of 'n_clouds' classes.
    Each class is a small gaussian cloud containing 'n_objects_by_cloud' points.
    The centers of the clouds are regularly disposed on a circle of radius 'radius' (and center (0,0)).
    The spreadth of the clouds is governed by 'sigma'.
    """
    rng = np.random.default_rng(seed)
    if not sigma:
        sigma = np.sqrt(2 - 2 * np.cos(2 * np.pi / n_clouds)) / 7

    def rotate(x, k):
        theta = 2 * k * np.pi / n_clouds + angle
        m = np.matrix([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
        return np.matmul(x, m)

    def cloud():
        return (rng.normal(size=2 * n_objects_by_cloud) * sigma).reshape(n_objects_by_cloud, 2) + np.array([radius, 0])

    def target():
        return np.array(([[i] * n_objects_by_cloud for i in range(n_clouds)]), dtype="int32").ravel()

    return np.concatenate([np.array(rotate(cloud(), k)) for k in range(n_clouds)], axis=0), target()

#                                     #########################
#                                     #    2D Visualization   #
#                                     #########################

def np_extrema(arr):
    return np.min(arr), np.max(arr)


def visualize_bassins(ax, model, x_min, x_max, y_min, y_max, cmap):
    """ color the points of a box
    with the color corresponding to the class predicted by the model """
    assert T.explanatory.shape[1] == 2, "Not a 2D example"
    X = np.linspace(x_min, x_max, 100)
    Y = np.linspace(y_min, y_max, 100)
    XX, YY = np.meshgrid(X, Y)
    XX_flat = XX.ravel()
    YY_flat = YY.ravel()
    Z = model.predict(np.vstack([XX_flat, YY_flat]).T)
    ax.pcolormesh(XX, YY, Z.reshape([100, 100]), cmap=cmap, shading='auto')


def visualize_training_dataset_2D(ax, model, cmap):
    """ color the points of the 'explanatory' array
    with the color corresponding to the class stored in 'target' """
    ax.scatter(model.explanatory[:, 0], model.explanatory[:, 1], c=model.target, cmap=cmap)


def visualize_model_2D(model, cmap=plt.cm.Set1):
    """ gather the results of visualize_bassins and visualize_training_dataset_2D """
    assert model.explanatory.shape[1] == 2, "Not a 2D example"

    x_min, x_max = np_extrema(model.explanatory[:, 0])
    y_min, y_max = np_extrema(model.explanatory[:, 1])
    fig, axes = plt.subplots(1, 2, figsize=(15, 7))
    for ax in axes:
        ax.set_xlim(x_min, x_max)
        ax.set_ylim(y_min, y_max)
    visualize_training_dataset_2D(axes[0], model, cmap)
    visualize_bassins(axes[1], model, x_min, x_max, y_min, y_max, cmap)
    plt.savefig("bassins2.png")
    plt.show()

#Main 2
explanatory,target = circle_of_clouds(10,30)
T=Decision_Tree(split_criterion="random")
T.fit(explanatory,target,verbose=0)
visualize_model_2D(T)
$ ./7-main_2.py

$ cat 7-main_1.py
#!/usr/bin/env python3

Decision_Tree = __import__('7-build_decision_tree').Decision_Tree
import numpy as np
from sklearn import datasets


#                                     #########################
#                                     # Generating examples : #
#                                     #########################

def circle_of_clouds(n_clouds, n_objects_by_cloud, radius=1, sigma=None, seed=0, angle=0):
    """
    This function returns a dataset made of 'n_clouds' classes.
    Each class is a small gaussian cloud containing 'n_objects_by_cloud' points.
    The centers of the clouds are regularly disposed on a circle of radius 'radius' (and center (0,0)).
    The spreadth of the clouds is governed by 'sigma'.
    """
    rng = np.random.default_rng(seed)
    if not sigma:
        sigma = np.sqrt(2 - 2 * np.cos(2 * np.pi / n_clouds)) / 7

    def rotate(x, k):
        theta = 2 * k * np.pi / n_clouds + angle
        m = np.matrix([[np.cos(theta), np.sin(theta)], [-np.sin(theta), np.cos(theta)]])
        return np.matmul(x, m)

    def cloud():
        return (rng.normal(size=2 * n_objects_by_cloud) * sigma).reshape(n_objects_by_cloud, 2) + np.array([radius, 0])

    def target():
        return np.array(([[i] * n_objects_by_cloud for i in range(n_clouds)]), dtype="int32").ravel()

    return np.concatenate([np.array(rotate(cloud(), k)) for k in range(n_clouds)], axis=0), target()


def iris():
    """ Returns the explanatory features and the target of the famous iris dataset """
    iris = datasets.load_iris()
    return iris.data, iris.target


def wine():
    """ Returns the explanatory features and the target of the wine dataset """
    wine = datasets.load_wine()
    return wine.data, wine.target


#                                     #########################
#                                     #    Data preparation   #
#                                     #########################

def split(explanatory, target, seed=0, proportion=.1):
    """ Returns a dictionary containing a a training dataset and a test dataset """
    rng = np.random.default_rng(seed)
    test_indices = rng.choice(target.size, int(target.size * proportion), replace=False)
    test_filter = np.zeros_like(target, dtype="bool")
    test_filter[test_indices] = True

    return {"train_explanatory": explanatory[np.logical_not(test_filter), :],
            "train_target": target[np.logical_not(test_filter)],
            "test_explanatory": explanatory[test_filter, :],
            "test_target": target[test_filter]}

# Main 1

for d,name in zip([ split(*circle_of_clouds(10,30)) , split(*iris()), split(*wine()) ], ["circle of clouds", "iris dataset", "wine dataset"]) :
    print("-"*52+"\n"+name+" :")
    T=Decision_Tree(split_criterion="random",max_depth=20,seed=0)
    T.fit(d["train_explanatory"],d["train_target"],verbose=1)
    T.update_predict()
    print(f"    - Accuracy on test          : {T.accuracy(d['test_explanatory'],d['test_target'])}")
print("-"*52)
$ ./7-main_1.py
----------------------------------------------------
circle of clouds :
  Training finished.
    - Depth                     : 10
    - Number of nodes           : 81
    - Number of leaves          : 41
    - Accuracy on training data : 1.0
    - Accuracy on test          : 0.9666666666666667
----------------------------------------------------
iris dataset :
  Training finished.
    - Depth                     : 15
    - Number of nodes           : 43
    - Number of leaves          : 22
    - Accuracy on training data : 1.0
    - Accuracy on test          : 0.9333333333333333
----------------------------------------------------
wine dataset :
  Training finished.
    - Depth                     : 17
    - Number of nodes           : 137
    - Number of leaves          : 69
    - Accuracy on training data : 1.0
    - Accuracy on test          : 0.7058823529411765
----------------------------------------------------