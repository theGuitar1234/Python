class Queue :
    n = None
    z = None
    t = None
    m = None
    
    def __init__(self, size) :
        global n
        global z
        global t
        global m
        self.queue = size*[""]
        n = len(self.queue)//2
        z = n
        t = n
        m = 0
    def add(self, element) :
        global n
        global z
        if (n==len(self.queue)) :
            n = 0
        self.queue[n] = element
        if n==z-1 :
            raise IndexError("The Queue is full")
        n += 1
    
    def dequeue(self) :
        global t
        global m
        if t+m == len(self.queue) :
            m = 0
            t = 0
        if t+m==z-1 :
            raise IndexError("The Queue is empty")
        self.queue[t+m] = ''
        m += 1

    def reverse(self) :
        self.queue = self.queue[::-1]
    def length(self) :
        length = 0
        for i in self.queue :
            if i == "" :
                continue
            length += 1
        return length

obj = Queue(29)
for i in range(1, 21) :
    obj.add(1)
print(obj.queue)
print(obj.length())