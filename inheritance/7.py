def f1(self, x, y):
    return min(x, x+y)
attribute = 23
class C:
    f = f1 #Class adopted the functin as a method
    class_attribute = attribute #can also adopt attributes
    def g(self):
        return 'hello world'
    h = g #method assigned to a class attribute

obj = C()
print(obj.class_attribute)
print(obj.f(2, 4))
print(obj.h())

class Bag:
    def __init__(self):
        self.data = []
    def add(self, x):
        self.data.append()
    def add_twice(self, x):
        self.add(x)
        self.add(x)
