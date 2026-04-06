class Deque:
    def __init__(self):
        self.queue = []

    def push_front(self, value):
        self.queue = [value] + self.queue  

    def push_back(self, value):
        self.queue.append(value) 

    def pop_front(self):
        if not self.is_empty():
            value = self.queue[0]
            self.queue = self.queue[1:] 
            return value
        print("Deque is empty!")
        return None

    def pop_back(self):
        if not self.is_empty():
            return self.queue.pop() 
        print("Deque is empty!")
        return None

    def is_empty(self):
        return len(self.queue) == 0

    def display(self):
        print(self.queue)

dq = Deque()
dq.push_front(1)
dq.push_back(2)
dq.push_front(0)
dq.display()  
print(dq.pop_front()) 
print(dq.pop_back())   
dq.display() 
