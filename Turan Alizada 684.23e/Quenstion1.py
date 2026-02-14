class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right

def is_complete_tree(root):
    if root == None:
        return "The Tree is a complete Tree"

    queue = [root]
    encountered_null = False  

    while queue:
        node = queue.pop(0)  

        if node:
            if encountered_null:
                return "The Tree is not a complete Tree" 
            
            queue.append(node.left)
            queue.append(node.right)
        else:
            encountered_null = True 

    return "The Tree is a complete Tree"

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
root.right.left = TreeNode(6)

print(is_complete_tree(root))  

