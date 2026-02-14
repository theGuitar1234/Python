class Class1:
    pass
class Class2(Class1):
    pass

c1 = Class1()
c2 = Class2()

print(type(c1))
print(type(c2))

print(type(2) == int)
print(type(c1) == Class1)
print(isinstance(c1, Class1))
print(issubclass(bool, int))
print(issubclass(Class2, Class1))
print(issubclass(Class1, Class2))