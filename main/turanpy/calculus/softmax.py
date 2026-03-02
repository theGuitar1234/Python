from turanpy.config import DEFAULTS

def softmax(Z):
    e = DEFAULTS.e   
    result = [0 for _ in range(len(Z))] 
    sum = 0
    for i in range(len(Z)):
        sum += e**Z[i]
    for i in range(len(Z)):
        result[i] = e**Z[i] / sum
    return result

if __name__ == "__main__":
    pass