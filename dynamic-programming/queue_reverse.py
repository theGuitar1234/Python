def reverse_queue(queue) :

    if len(queue) == 1 :
        return queue
    
    for i in range(len(queue)-1) :
        queue.append(queue.pop(0))
    
    return [queue.pop(0)] + reverse_queue(queue)

def queue_reverse(queue, k) :
    queue2 = []

    for i in range(k) :
        int = queue.pop(0)
        queue2.append(int)

    queue2 = reverse_queue(queue2)

    for i in range(len(queue)) :
        queue2.append(queue.pop(0))
    return queue2

queue = [1, 2, 3, 4, 5, 6, 7]
print(queue_reverse(queue, 6))