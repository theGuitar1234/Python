#!/usr/bin/env python3
import numpy as np


class Node:
    def __init__(
        self,
        feature=None,
        threshold=None,
        left_child=None,
        right_child=None,
        is_root=False,
        depth=0,
    ):
        self.feature = feature
        self.threshold = threshold
        self.left_child = left_child
        self.right_child = right_child
        self.is_leaf = False
        self.is_root = is_root
        self.sub_population = None
        self.depth = depth

    def max_depth_below(self):
        max_depth = self.depth

        if self.left_child is not None:
            max_depth = max(max_depth, self.left_child.max_depth_below())

        if self.right_child is not None:
            max_depth = max(max_depth, self.right_child.max_depth_below())

        return max_depth


class Leaf(Node):
    def __init__(self, value, depth=None):

        super().__init__()
        self.value = value
        self.is_leaf = True
        self.depth = depth

    def max_depth_below(self):
        return self.depth


class Decision_Tree:
    def __init__(
        self, max_depth=10, min_pop=1, seed=0, split_criterion="random", root=None
    ):
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

    def depth(self):
        return self.root.max_depth_below()


if __name__ == "__main__":

    def example_0():
        leaf0 = Leaf(0, depth=1)
        leaf1 = Leaf(0, depth=2)
        leaf2 = Leaf(1, depth=2)
        internal_node = Node(
            feature=1, threshold=30000, left_child=leaf1, right_child=leaf2, depth=1
        )
        root = Node(
            feature=0,
            threshold=0.5,
            left_child=leaf0,
            right_child=internal_node,
            depth=0,
            is_root=True,
        )
        return Decision_Tree(root=root)

    def example_1(depth):
        level = [Leaf(i, depth=depth) for i in range(2**depth)]
        level.reverse()

        def get_v(node):
            if node.is_leaf:
                return node.value
            else:
                return node.threshold

        for d in range(depth):
            level = [
                Node(
                    feature=0,
                    threshold=(get_v(level[2 * i]) + get_v(level[2 * i + 1])) / 2,
                    left_child=level[2 * i],
                    right_child=level[2 * i + 1],
                    depth=depth - d - 1,
                )
                for i in range(2 ** (depth - d - 1))
            ]
        root = level[0]
        root.is_root = True
        return Decision_Tree(root=root)

    print(example_0().depth())
    print(example_1(5).depth())
