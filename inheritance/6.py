#When you use the for statements, 
#it calls the iter() behind the scenes. On the container object 
#Then __next__ magic method is called. 
#It accesses elements one at a time
#when there are no elements, it raises StopIteration exception
#so loop is terminated

# s = "abc"
# i = iter(s)
# print(next(i))
# print(next(i))

class Reverse:
    def __init__(self, data):
        self.data = data
        self.index = len(data)
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if (self.index == 0):
            raise StopIteration
        self.index -= 1
        return self.data[self.index]

r = Reverse('hello')
iter(r)
for i in r:
    print(i)

class Class:
    def __init__(self):
        self.__private_attribute = 12
obj = Class()
print(obj.__private_attribute) #AttributeError

print(obj._Class__private_attribute) #12

