from turanpy.config import DEFAULTS

def derivative(f, x, h=1, threshold=1e-5) :
    current = x
    prev = None

    while True :
        next = (f(current+h) - f(current)) / h
        if (prev is not None and abs(next-prev) < threshold):
            break
        prev = next
        h /= 2
    return next

if __name__ == "__main__":
    pass