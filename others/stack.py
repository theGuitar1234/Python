class Stacks :
    def __init__(self) :
        self.s = []
    def add(self, element) :
        self.s.append(element)
    def insert(self, element) :
        for i in range(len(self.s)) :
            if element>self.s[i] :
                continue
            else :
                self.s.append(None)
                k = len(self.s) - 1
                n = len(self.s) - 2
                while k>i :
                    self.s[k] = self.s[n]
                    n -= 1
                    k -= 1
                self.s[i] = element
                return self.s

stack = Stacks()
stack.add(1)
stack.add(1)
stack.add(2)
stack.add(3)
stack.add(3)
stack.add(5)
print(stack.insert(2.5))
print(stack.insert(4.5))