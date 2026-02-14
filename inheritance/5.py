class Complex:

    x: float
    y: float
    
    def __new__(cls, x, y):
        print("This method is called even before __init__")
        print(x, y)
        return super().__new__(cls)
    
    def __init__(self, real=0, imag=0):
        self.r = real
        self.im = imag

    def __str__(self):
        if (self.im >= 0):
            return f"x={self.r}+{self.im}i"
        return f"x={self.r}{self.im}i"
    
    @property
    def i(self):
        return "\u221A-1"
    
    @staticmethod
    def add(x, y):
        return Complex(x.r + y.r, x.im + y.im)

    @staticmethod
    def multiply(x, y):
        return Complex(x.r * y.r, x.im * y.im * -1)

x = Complex(3.0, -4.5) #Instance Object
y = Complex(2.0, 1.2)
print(str(x))
print(x.i)
sum = Complex.add(x, y)
print(str(sum))
mul = Complex.multiply(x, y)
print(str(mul))

method = x.add #method object
print(method(x, y))