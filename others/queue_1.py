class Queue :
    dequeue_mid = None
    dequeue_increment = None
    mid = None
    increment = None
    def __init__(self, size) :
        self.queue = [None] * (size)
        self.mid = len(self.queue)//2
        self.dequeue_mid = self.mid
        self.dequeue_increment = 0
        self.increment = 0
    def enqueue(self, element) :
        if self.mid+self.increment == len(self.queue) :
            self.mid = 0
            self.increment = 0
        if self.queue[self.mid+self.increment] != None :
            raise IndexError("The Queue is Full")
        self.queue[self.mid+self.increment] = element
        self.increment += 1
    def dequeue(self) :
        if self.dequeue_mid+self.dequeue_increment == len(self.queue) :
            self.dequeue_mid = 0
            self.dequeue_increment = 0
        if self.queue[self.dequeue_mid+self.dequeue_increment] == None :
            raise IndexError("The Queue is Empty")
        self.queue[self.dequeue_mid+self.dequeue_increment] = None
        self.dequeue_increment += 1
    def reverse(self) :
        self.queue = self.queue[::-1]
    def length(self) :
        length = 0
        for i in self.queue :
            if i != None :
                length += 1
        return length
    
obj = Queue(20)
for i in range(1, 19) :
    obj.enqueue("Thomas")
for i in range(1, 19) :
    obj.dequeue()
for i in range(1, 19) :
    obj.enqueue("THomas")
print(obj.length())

    