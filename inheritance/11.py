from typing import override

class Parent:
    def sayhello(self):
        print(f"Hello from Parent")

    def __init__(self, name):
        self.name = name
class Child(Parent):
    @override
    def sayhello(self):
        super().sayhello()
        print(f"Hello from {self.__class__}")

    def __init__(self, name, age):
        self.age = age

p = Parent("Bill")
c = Child("Thomas", 12)
c.sayhello()
print(c.age, c.name)

