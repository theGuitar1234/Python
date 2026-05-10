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

$ cat 5-main.py
#!/usr/bin/env python3

Node = __import__('5-build_decision_tree').Node
Leaf = __import__('5-build_decision_tree').Leaf
Decision_Tree = __import__('5-build_decision_tree').Decision_Tree
import numpy as np

def example_0():
    leaf0 = Leaf(0, depth=1)
    leaf1 = Leaf(0, depth=2)
    leaf2 = Leaf(1, depth=2)
    internal_node = Node(feature=1, threshold=30000, left_child=leaf1, right_child=leaf2, depth=1)
    root = Node(feature=0, threshold=.5, left_child=leaf0, right_child=internal_node, depth=0, is_root=True)
    return Decision_Tree(root=root)


def example_1(depth):
    level = [Leaf(i, depth=depth) for i in range(2 ** depth)]
    level.reverse()

    def get_v(node):
        if node.is_leaf:
            return node.value
        else:
            return node.threshold

    for d in range(depth):
        level = [Node(feature=0,
                      threshold=(get_v(level[2 * i]) + get_v(level[2 * i + 1])) / 2,
                      left_child=level[2 * i],
                      right_child=level[2 * i + 1], depth=depth - d - 1) for i in range(2 ** (depth - d - 1))]
    root = level[0]
    root.is_root = True
    return Decision_Tree(root=root)

def print_indicator_values_on_leaves(T,A):
    leaves=T.get_leaves()
    T.update_bounds()
    for leaf in leaves :
        leaf.update_indicator()
    print ("values of indicators of leaves :\n",np.array([leaf.indicator(A) for leaf in leaves]))

T=example_0()
A=np.array([[1,22000],[1,44000],[0,22000],[0,44000]])
print("\n\nFor example_0()")
print("A=\n",A)
print_indicator_values_on_leaves(T,A)

T=example_1(4)
A=np.array([[11.65],[6.917]])
print("\n\nFor example_1(4)")
print("A=\n",A)
print_indicator_values_on_leaves(T,A)
$ ./5-main.py


For example_0()
A=
 [[    1 22000]
 [    1 44000]
 [    0 22000]
 [    0 44000]]
values of indicators of leaves :
 [[ True  True False False]
 [False False False  True]
 [False False  True False]]


For example_1(4)
A=
 [[11.65 ]
 [ 6.917]]
values of indicators of leaves :
 [[False False]
 [False False]
 [False False]
 [ True False]
 [False False]
 [False False]
 [False False]
 [False False]
 [False  True]
 [False False]
 [False False]
 [False False]
 [False False]
 [False False]
 [False False]
 [False False]]