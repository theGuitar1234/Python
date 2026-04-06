class Queue:
    def __init__(self):
        self.queue = []

    def enqueue(self, element):
        self.queue.append(element)

    def dequeue(self):
        if not self.is_empty():
            return self.queue.pop(0) 
        else :
            return None 

    def is_empty(self):
        if len(self.queue) == 0 :
            return True
        else :
            return False


class TreeNode:
    def __init__(self, value=0, left=None, right=None):
        self.value = value
        self.left = left
        self.right = right


def is_complete_tree(root):
    if root == None:
        return "The Tree is a complete Tree"

    queue = Queue()
    queue.enqueue(root)
    encountered_null = False  

    while not queue.is_empty():
        node = queue.dequeue()  

        if node:
            if encountered_null:
                return "The Tree is not a complete Tree" 
            
            queue.enqueue(node.left)
            queue.enqueue(node.right)
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
