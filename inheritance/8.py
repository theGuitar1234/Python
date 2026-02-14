#super is not the parent class
#It is a proxy object that says
#When you look up an attribute/method, start after this class in the MRO
#method resolution order for this instance
#from typing import override

class Parent:
    def sayHello(self):
        print(f"hello from {self.__class__.__name__}!")

class Child(Parent):
    def sayHiToParent(self):
       mro = type(self).mro()
       parent = mro[mro.index(Child) + 1]
       print(f"hello {parent.__name__}!")
    
    #@override
    def sayHello(self):
        return super().sayHello()

c = Child()
c.sayHello()
c.sayHiToParent()