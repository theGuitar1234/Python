class Queue :
    def __init__(self, size) :
        self.queue = []
        self.size = size

    def enqueue(self, element) :
        if len(self.queue) == self.size :
            raise IndexError("The Queue is Full")
        self.queue.append(element)
    def dequeue(self) :
        if len(self.queue) == 0 :
            raise IndexError("The Queue is Empty")
        else :
            self.queue.pop(0)
obj = Queue(10)

obj.enqueue("a")
obj.enqueue("b")
obj.dequeue()
print(obj.queue)

    