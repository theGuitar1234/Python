class Tree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_fibonacci_tree(n):
    if n <= 1:
        return Tree(n)  

    root = Tree(build_fibonacci_tree(n - 1).value + build_fibonacci_tree(n - 2).value)  
    root.left = build_fibonacci_tree(n - 1)  
    root.right = build_fibonacci_tree(n - 2) 

    return root  

def check_fibonacci_property(root):
    if root is None or (root.left is None and root.right is None):
        return True 

    if root.value != (root.left.value + root.right.value):
        return False

    return check_fibonacci_property(root.left) and check_fibonacci_property(root.right)

n = 6  
fib_tree = build_fibonacci_tree(n)

if check_fibonacci_property(fib_tree):
    print("Every non-leaf node satisfies F(n) = F(n-1) + F(n-2)")
else:
    print("The tree does not satisfy the Fibonacci property.")
