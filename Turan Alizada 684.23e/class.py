class Parent:
    def sayHelloParent(self):
        print("Hello from Parent")

class Child(Parent):
    def sayHelloChild(self):
        super.__init__.sayHelloParent(super)
        print("Hello from Child")

p = Parent()
c = Child()
print(c.sayHelloChild())