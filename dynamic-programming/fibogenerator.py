def fibo_generator(n) :
    yield 0
    yield 1
    prev = 0
    next = 1
    for i in range(2, n) :
        current = prev+next
        prev = next
        next = current
        yield current
g = fibo_generator(100)
for i in g :
    print(i, end=" ")
