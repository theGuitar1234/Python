def inherits_from(a, clazz):
    return issubclass(a.__class__, clazz) and not a.__class__ is clazz

a = True
if inherits_from(a, int):
    print("{} inherited from class {}".format(a, int.__name__))
if inherits_from(a, bool):
    print("{} inherited from class {}".format(a, bool.__name__))
if inherits_from(a, object):
    print("{} inherited from class {}".format(a, object.__name__))

# True inherited from class int
# True inherited from class object