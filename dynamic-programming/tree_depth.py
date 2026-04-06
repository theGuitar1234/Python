class A:
    def __init__(self):
        self.value = "Root"
        self.b = B(self) 
        self.c = C(self)  

    def depth(self):
        return 1 + self.b.depth() + self.c.depth()

class B:
    def __init__(self, parent):
        self.value = "A's Child"
        self.parent = parent
        self.f = F(self)  

    def depth(self):
        return 1 + self.f.depth()

class C:
    def __init__(self, parent):
        self.value = "A's Child"
        self.parent = parent
        self.d = D(self) 

    def depth(self):
        return 1 + self.d.depth()

class D:
    def __init__(self, parent):
        self.value = "C's child"
        self.parent = parent
        self.e = E(self) 

    def depth(self):
        return 1 + self.e.depth()

class E:
    def __init__(self, parent):
        self.value = "D's child"
        self.parent = parent

    def depth(self):
        return 1 

class F:
    def __init__(self, parent):
        self.value = "B's child"
        self.parent = parent

    def depth(self):
        return 1
    
a = A()

print(a.value)     
print(a.depth())   
