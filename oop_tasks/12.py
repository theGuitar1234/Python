def add_attribute(clazz, name, value):
    if not hasattr(clazz, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(clazz, name, value)

class MyClass():
    pass

mc = MyClass()
add_attribute(mc, "name", "John")
print(mc.name)

try:
    a = "My String"
    add_attribute(a, "name", "Bob")
    print(a.name)
except Exception as e:
    print("[{}] {}".format(e.__class__.__name__, e))