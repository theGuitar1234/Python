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

$ cat 6-main.py
#!/usr/bin/env python3

Node = __import__('6-build_decision_tree').Node
Leaf = __import__('6-build_decision_tree').Leaf
Decision_Tree = __import__('6-build_decision_tree').Decision_Tree
import numpy as np

def random_tree(max_depth, n_classes,n_features,seed=0) :
    assert max_depth>0, "max_depth must be a strictly positive integer"
    rng=np.random.default_rng(seed)
    root=Node(is_root=True,depth=0)
    root.lower={i:-100 for i in range(n_features)}
    root.upper={i:100 for i in range(n_features)}

    def build_children(node) :
        feat=rng.integers(0,n_features)
        node.feature=feat
        node.threshold = np.round(rng.uniform(0,1)*(node.upper[feat]-node.lower[feat])+node.lower[feat],2)
        if node.depth==max_depth-1 :
            node.left_child=Leaf(depth=max_depth, value=rng.integers(0,n_classes))
            node.right_child=Leaf(depth=max_depth, value=rng.integers(0,n_classes))
        else :
            node.left_child=Node(depth=node.depth+1)
            node.left_child.lower=node.lower.copy()
            node.left_child.upper=node.upper.copy()
            node.left_child.lower[feat]=node.threshold
            node.right_child=Node(depth=node.depth+1)
            node.right_child.lower=node.lower.copy()
            node.right_child.upper=node.upper.copy()
            node.right_child.upper[feat]=node.threshold
            build_children(node.left_child)
            build_children(node.right_child)

    T=Decision_Tree(root=root)
    build_children(root)

    A=rng.uniform(0,1,size=100*n_features).reshape([100,n_features])*200-100
    return T, A

T,A=random_tree(4, 3 ,5,seed=1)
print(T)

T.update_predict()

print("T.pred(A) :\n",np.array([T.pred(x) for x in A]))
print("T.predict(A) :\n",T.predict(A))

test=np.all(np.equal(T.predict(A),np.array([T.pred(x) for x in A])))                         
print(f"Predictions are the same on the explanatory array A : {test}")      
$ ./6-main.py
root [feature=2, threshold=90.09]
    +---> node [feature=2, threshold=91.52]
    |      +---> node [feature=4, threshold=-37.63]
    |      |      +---> node [feature=4, threshold=20.63]
    |      |      |      +---> leaf [value=0]
    |      |      |      +---> leaf [value=2]
    |      |      +---> node [feature=1, threshold=9.92]
    |      |             +---> leaf [value=1]
    |      |             +---> leaf [value=0]
    |      +---> node [feature=0, threshold=50.7]
    |             +---> node [feature=4, threshold=-34.05]
    |             |      +---> leaf [value=1]
    |             |      +---> leaf [value=1]
    |             +---> node [feature=3, threshold=-39.36]
    |                    +---> leaf [value=0]
    |                    +---> leaf [value=1]
    +---> node [feature=4, threshold=-19.38]
           +---> node [feature=0, threshold=-59.31]
           |      +---> node [feature=2, threshold=42.64]
           |      |      +---> leaf [value=0]
           |      |      +---> leaf [value=0]
           |      +---> node [feature=1, threshold=-2.96]
           |             +---> leaf [value=0]
           |             +---> leaf [value=2]
           +---> node [feature=3, threshold=44.96]
                  +---> node [feature=4, threshold=-56.37]
                  |      +---> leaf [value=2]
                  |      +---> leaf [value=0]
                  +---> node [feature=3, threshold=40.6]
                         +---> leaf [value=0]
                         +---> leaf [value=1]

T.pred(A) :
 [0 0 0 0 1 1 2 0 1 0 0 0 2 0 2 0 1 0 1 1 0 1 0 0 0 2 1 0 0 0 1 0 0 0 0 1 0
 1 0 1 0 1 1 0 1 2 0 1 1 0 0 1 0 1 0 1 0 1 1 1 0 0 0 2 0 0 0 1 0 2 2 0 0 0
 0 0 1 0 0 1 0 1 0 1 1 0 0 0 0 0 0 1 0 0 1 1 0 0 0 1]
T.predict(A) :
 [0 0 0 0 1 1 2 0 1 0 0 0 2 0 2 0 1 0 1 1 0 1 0 0 0 2 1 0 0 0 1 0 0 0 0 1 0
 1 0 1 0 1 1 0 1 2 0 1 1 0 0 1 0 1 0 1 0 1 1 1 0 0 0 2 0 0 0 1 0 2 2 0 0 0
 0 0 1 0 0 1 0 1 0 1 1 0 0 0 0 0 0 1 0 0 1 1 0 0 0 1]
Predictions are the same on the explanatory array A : True