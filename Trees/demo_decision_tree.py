import numpy as np


class Node:
    def __init__(self, feature=None, threshold=None):
        self.feature = feature
        self.threshold = threshold
        self.left = None
        self.right = None
        self.value = None


class DecisionTree:
    def __init__(self, max_depth=3):
        self.max_depth = max_depth
        self.root = None

    def fit(self, X, y):
        X = np.array(X)
        y = np.array(y)
        self.root = self._build_tree(X, y, depth=0)

    def _build_tree(self, X, y, depth):
        node = Node()

        if depth >= self.max_depth or len(set(y)) == 1:
            node.value = self._majority_class(y)
            return node

        feature, threshold = self._choose_split(X, y)
        node.feature = feature
        node.threshold = threshold

        left_mask = X[:, feature] > threshold
        right_mask = ~left_mask

        node.left = self._build_tree(X[left_mask], y[left_mask], depth + 1)
        node.right = self._build_tree(X[right_mask], y[right_mask], depth + 1)

        return node

    def predict_one(self, x, node=None):
        if node is None:
            node = self.root

        if node.value is not None:
            return node.value

        if x[node.feature] > node.threshold:
            return self.predict_one(x, node.left)
        else:
            return self.predict_one(x, node.right)

    def predict(self, X):
        X = np.array(X)
        return [self.predict_one(x) for x in X]

    def _majority_class(self, y):
        return max(set(y), key=list(y).count)

    def _choose_split(self, X, y):
        feature = 0
        threshold = X[:, feature].mean()
        return feature, threshold


if __name__ == "__main__":
    tree = DecisionTree()
    X = [[1], [2], [3], [10], [11], [12]]
    y = [0, 0, 0, 1, 1, 1]

    tree.fit(X, y)
    print(tree.predict([[12], [2], [11]]))
