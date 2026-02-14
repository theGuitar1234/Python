class BaseGeometry:
    def area(self):
        raise Exception("area() is not implemented")
    def integer_validator(self, name, value):
        if value.__class__ is not int:
            raise TypeError(f"{name} must be an integer")
        elif value <= 0:
            raise ValueError(f"{name} must be greater than 0")
        return value

class Rectangle(BaseGeometry):
    def __init__(self, width, height):
        self.__width = self.integer_validator("width", width)
        self.__height = self.integer_validator("height", height)
    def area(self):
        return self.__height*self.__width
    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__width}/{self.__height}"
    
class Square(Rectangle):
    def __init__(self, size):
        self.__size = self.integer_validator("size", size)
    def area(self):
        return self.__size*self.__size
    def __str__(self):
        return f"[{self.__class__.__name__}] {self.__size}/{self.__size}"

r = Rectangle(3, 5)

print(r)
print(r.area())

# [Rectangle] 3/5
# 15

s = Square(13)

print(s)
print(s.area())

# [Rectangle] 13/13
# 169