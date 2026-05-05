class Node:
    def __init__(self, key):
        self.key = key
        self.nodes = []

    def search_key(self, key):
        if self.key == key:
            return self
        else:
            for node in self.nodes:
                result = node.search_key(key)
                if result is not None:
                    return result
        return None

    def visualize(self):
        if len(self.nodes) == 0:
            return self.key + "  "

        result = f"\nBranch: {self.key} "
        for node in self.nodes:
            result += node.visualize()

        return result


class Tree:
    def __init__(self):
        self.root = None

    def insert_node(self, key, value):
        if self.root is None:
            self.root = Node(key)
        node = self.root.search_key(key)
        if node is not None:
            node.nodes.append(Node(value))
        else:
            raise RuntimeError("Key not found")

    def search_node(self, key):
        if self.root is None:
            raise RuntimeError("Tree is empty")
        node = self.root.search_key(key)
        if node is not None:
            return node
        else:
            raise RuntimeError("Key not found")

    def visualize(self):
        return self.root.visualize()


tree = Tree()
tree.insert_node("root", "root_child1")
tree.insert_node("root", "root_child2")
tree.insert_node("root_child1", "child1_descendant1")
tree.insert_node("root_child2", "child2_descendant1")
tree.insert_node("child1_descendant1", "descendant1_child1")
tree.insert_node("child2_descendant1", "descendant2_child2")

# root_child1 = tree.search_node("root_child1")
# for node in root_child1.nodes:
#     print(node.key)

# root_child2 = tree.search_node("root_child2")
# print(root_child2.key)

result = tree.visualize()
print(result)

result = tree.visualize()
print(result)
