#!/usr/bin/env python3
"""Isolation Random Tree module."""

import numpy as np

Node = __import__("8-build_decision_tree").Node
Leaf = __import__("8-build_decision_tree").Leaf


class Isolation_Random_Tree:
    """Isolation Random Tree (random splits, leaf value = depth)."""

    def __init__(self, max_depth=10, seed=0, root=None):
        self.rng = np.random.default_rng(seed)
        if root:
            self.root = root
        else:
            self.root = Node(is_root=True)
        self.explanatory = None
        self.max_depth = max_depth
        self.predict = None
        self.min_pop = 1

    def __str__(self):
        """Docstring."""
        return self.root.__str__()

    def depth(self):
        """Docstring."""
        return self.root.max_depth_below()

    def count_nodes(self, only_leaves=False):
        """Docstring."""
        return self.root.count_nodes_below(only_leaves=only_leaves)

    def update_bounds(self):
        """Docstring."""
        self.root.update_bounds_below()

    def get_leaves(self):
        """Docstirng."""
        return self.root.get_leaves_below()

    def update_predict(self):
        """Docstring."""
        self.update_bounds()
        leaves = self.get_leaves()
        for leaf in leaves:
            leaf.update_indicator()
        values = np.array([leaf.value for leaf in leaves], dtype=float)

        def predict_func(a):
            """Docstring."""
            lst = [leaf.indicator(a) for leaf in leaves]
            indicators = np.array(lst, dtype=int)
            return values @ indicators
        self.predict = predict_func

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

    def get_leaf_child(self, node, sub_population):
        """Docstring."""
        leaf_depth = node.depth + 1
        leaf_child = Leaf(leaf_depth, depth=leaf_depth)
        leaf_child.depth = leaf_depth
        leaf_child.subpopulation = sub_population
        leaf_child.sub_population = sub_population
        return leaf_child

    def get_node_child(self, node, sub_population):
        """Docstring."""
        n = Node()
        n.depth = node.depth + 1
        n.sub_population = sub_population
        return n

    def fit_node(self, node):
        """Docstring."""
        pop_size = int(np.sum(node.sub_population))
        if pop_size <= self.min_pop or node.depth >= self.max_depth:
            node.left_child = self.get_leaf_child(
                node, np.zeros_like(node.sub_population, dtype=bool)
            )
            a = self.get_leaf_child(node, node.sub_population.copy())
            node.right_child = a
            return
        sub_x = self.explanatory[node.sub_population, :]
        if np.all(np.ptp(sub_x, axis=0) == 0):
            node.feature = 0
            node.threshold = float(sub_x[0, 0])
            node.left_child = self.get_leaf_child(
                node, np.zeros_like(node.sub_population, dtype=bool)
            )
            b = self.get_leaf_child(node, node.sub_population.copy())
            node.right_child = b
            return
        node.feature, node.threshold = self.random_split_criterion(node)
        feat_col = self.explanatory[:, node.feature]
        go_left = feat_col > node.threshold
        left_population = node.sub_population & go_left
        right_population = node.sub_population & (~go_left)
        child_depth = node.depth + 1
        is_left_leaf = (
            child_depth >= self.max_depth
            or np.sum(left_population) <= self.min_pop
        )
        is_right_leaf = (
            child_depth >= self.max_depth
            or np.sum(right_population) <= self.min_pop
        )
        if is_left_leaf:
            node.left_child = self.get_leaf_child(node, left_population)
        else:
            node.left_child = self.get_node_child(node, left_population)
            self.fit_node(node.left_child)
        if is_right_leaf:
            node.right_child = self.get_leaf_child(node, right_population)
        else:
            node.right_child = self.get_node_child(node, right_population)
            self.fit_node(node.right_child)

    def fit(self, explanatory, verbose=0):
        """Docstring."""
        self.split_criterion = self.random_split_criterion
        self.explanatory = explanatory
        self.root.sub_population = np.ones(explanatory.shape[0], dtype=bool)
        self.fit_node(self.root)
        self.update_predict()
        if verbose == 1:
            print(
                f"""  Training finished.
    - Depth                     : {self.depth()}
    - Number of nodes           : {self.count_nodes()}
    - Number of leaves          : {self.count_nodes(only_leaves=True)}"""
            )

$ cat 10-main.py
#!/usr/bin/env python3

Isolation_Random_Tree = __import__('10-isolation_tree').Isolation_Random_Tree
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


def visualize_bassins(ax, model, x_min, x_max, y_min, y_max,cmap) :
    """ color the points of a box
    with the color corresponding to the class predicted by the model """
    assert model.explanatory.shape[1]==2, "Not a 2D example"
    X       = np.linspace(x_min, x_max, 100)
    Y       = np.linspace(y_min, y_max, 100)
    XX,YY   = np.meshgrid(X, Y)
    XX_flat = XX.ravel()
    YY_flat = YY.ravel()
    Z       = model.predict(np.vstack([XX_flat, YY_flat]).T)
    ax.pcolormesh(XX, YY, Z.reshape([100,100]), cmap=cmap,shading='auto')


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

#Main
explanatory,_ = circle_of_clouds(1,100,sigma=.2)   # a cloud
explanatory[0]=[-1,0]                              # an outlier

fig,axes=plt.subplots(3,3,figsize=(12,12))
plt.subplots_adjust(hspace = 0.3,wspace=.3)
axes[0,0].scatter(explanatory[:,0],explanatory[:,1])
axes[0,0].set_title("a cloud and an outlier")
for i in range(1,9) :
        T = Isolation_Random_Tree( max_depth=8, seed=i, root=None)
        T.fit(explanatory)
        visualize_bassins(axes[i%3,i//3],T,-1.2,1.5,-.5,.5,cmap=plt.cm.RdBu)  
        axes[i%3,i//3].set_title(f"bassins of isolation tree for seed={i}")  
plt.show()
$ ./10-main.py
