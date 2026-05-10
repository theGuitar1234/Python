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

$ cat 4-main.py
#!/usr/bin/env python3

Node = __import__('4-build_decision_tree').Node
Leaf = __import__('4-build_decision_tree').Leaf
Decision_Tree = __import__('4-build_decision_tree').Decision_Tree

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

def test_bounds():
    c = 0
    for T in [example_0(), example_1(5)]:
        print("example_", c)
        c += 1
        T.update_bounds()
        leaves = T.get_leaves()
        for i in range(len(leaves)):
            print("  leaf number ", i)
            print("    lower :", leaves[i].lower)
            print("    upper :", leaves[i].upper)

test_bounds()
$ ./4-main.py
example_ 0
  leaf number  0
    lower : {0: 0.5}
    upper : {0: inf}
  leaf number  1
    lower : {0: -inf, 1: 30000}
    upper : {0: 0.5}
  leaf number  2
    lower : {0: -inf}
    upper : {0: 0.5, 1: 30000}
example_ 1
  leaf number  0
    lower : {0: 30.5}
    upper : {0: inf}
  leaf number  1
    lower : {0: 29.5}
    upper : {0: 30.5}
  leaf number  2
    lower : {0: 28.5}
    upper : {0: 29.5}
  leaf number  3
    lower : {0: 27.5}
    upper : {0: 28.5}
  leaf number  4
    lower : {0: 26.5}
    upper : {0: 27.5}
  leaf number  5
    lower : {0: 25.5}
    upper : {0: 26.5}
  leaf number  6
    lower : {0: 24.5}
    upper : {0: 25.5}
  leaf number  7
    lower : {0: 23.5}
    upper : {0: 24.5}
  leaf number  8
    lower : {0: 22.5}
    upper : {0: 23.5}
  leaf number  9
    lower : {0: 21.5}
    upper : {0: 22.5}
  leaf number  10
    lower : {0: 20.5}
    upper : {0: 21.5}
  leaf number  11
    lower : {0: 19.5}
    upper : {0: 20.5}
  leaf number  12
    lower : {0: 18.5}
    upper : {0: 19.5}
  leaf number  13
    lower : {0: 17.5}
    upper : {0: 18.5}
  leaf number  14
    lower : {0: 16.5}
    upper : {0: 17.5}
  leaf number  15
    lower : {0: 15.5}
    upper : {0: 16.5}
  leaf number  16
    lower : {0: 14.5}
    upper : {0: 15.5}
  leaf number  17
    lower : {0: 13.5}
    upper : {0: 14.5}
  leaf number  18
    lower : {0: 12.5}
    upper : {0: 13.5}
  leaf number  19
    lower : {0: 11.5}
    upper : {0: 12.5}
  leaf number  20
    lower : {0: 10.5}
    upper : {0: 11.5}
  leaf number  21
    lower : {0: 9.5}
    upper : {0: 10.5}
  leaf number  22
    lower : {0: 8.5}
    upper : {0: 9.5}
  leaf number  23
    lower : {0: 7.5}
    upper : {0: 8.5}
  leaf number  24
    lower : {0: 6.5}
    upper : {0: 7.5}
  leaf number  25
    lower : {0: 5.5}
    upper : {0: 6.5}
  leaf number  26
    lower : {0: 4.5}
    upper : {0: 5.5}
  leaf number  27
    lower : {0: 3.5}
    upper : {0: 4.5}
  leaf number  28
    lower : {0: 2.5}
    upper : {0: 3.5}
  leaf number  29
    lower : {0: 1.5}
    upper : {0: 2.5}
  leaf number  30
    lower : {0: 0.5}
    upper : {0: 1.5}
  leaf number  31
    lower : {0: -inf}
    upper : {0: 0.5}