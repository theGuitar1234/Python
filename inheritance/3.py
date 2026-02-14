#PEB8 Python Standart
#This is more strict than Pycodestyle
#Which only required stuff like :
#There must be spaces around operators and 
# there can't be space inbetween a statement declaration like if else for while and ":" colon
#if 2 > 3:
#In PEB8 : 
#import must be at the top and there must be 2 blank lines after
#Each class and function must have docstring
#Which is just """DocString""" used to explain what class of function does
#And there must be a blank line inbetween each function
import inheritance.package.Binary_Search as b


class MyClass:
    """
    Docstring for MyClass
    """

    def func():
        """
        Docstring for func
        """

    def func2():
        """
        Docstring for func2
        """

obj = MyClass()
print(obj.__doc__)
print(obj.func.__doc__)
print(obj.func2.__doc__)