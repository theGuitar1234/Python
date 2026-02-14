class Class:
    class_attribute = 123
    def __init__(self):
        self.instance_attribute = 124
obj = Class()

#del will only work if writable
#You can't delete the class value but the written value
obj.class_attribute = 345

print(obj.class_attribute)
print(obj.instance_attribute)

del obj.class_attribute

#instance attributes aren't class attributes
#They have no problem with del
del obj.instance_attribute

try:
    print(obj.class_attribute)
    print(obj.instance_attribute)
except Exception as e:
    print(str(e))

print(obj)
del obj

try:
    print(obj)
except Exception as e:
    print(str(e))

#If both class and instance attributes are used, instance will be prioritized