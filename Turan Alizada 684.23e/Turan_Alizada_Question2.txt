class Stacks :
    def __init__(self) :
        self.s = []
    def add(self, element) :
        self.s.append(element)
    def remove(self) :
        self.s.pop()
            

def smaller_integers_stack(list) :
    stack = Stacks()
    result = Stacks()  

    for num in list:
        while len(stack.s) != 0 and stack.s[-1] >= num:
            stack.remove()

        if len(stack.s) != 0 :
            result.add(stack.s[-1])
        else:
            result.add(None)  

        stack.add(num)

    return result.s

list = [1, 6, 4, 10, 2, 5]
print(smaller_integers_stack(list))