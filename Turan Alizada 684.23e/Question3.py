class Queue:
    def __init__(self):
        self.queue = [] 
        self.max_queue = [] 

    def enqueue(self, value):
        self.queue.append(value)

        while len(self.max_queue) != 0 and self.max_queue[-1] < value:
            self.max_queue.pop()

        self.max_queue.append(value)

    def dequeue(self):
        if len(self.queue) == 0:
            return None 
        
        value = self.queue.pop(0)

        if value == self.max_queue[0]:
            self.max_queue.pop(0)

        return value

    def get_max_value(self):
        if len(self.max_queue) == 0:
            return None 
       
        return self.max_queue[0]

q = Queue()
q.enqueue(1)
q.enqueue(3)
q.enqueue(2)
q.enqueue(5)
q.enqueue(4)

print(q.get_max_value())  

q.dequeue()
q.dequeue()

print(q.get_max_value())  

q.dequeue()

print(q.get_max_value())  

q.dequeue()
print(q.get_max_value())
