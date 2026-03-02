from turanpy.config import DEFAULTS
from turanpy import classification

import random 

def main(X, y, lr=0.001, epochs=50000):
    res = classification.MSE_gradient_descent(y, X, lr, epochs)
    for _ in range(5):
        h = random.randint(0, 10)
        print(f"Hours studied: {h}", predict_raw(h, res), predict_label(h, res))

def predict_raw(input, tuple):
    
    w = tuple[0]
    b = tuple[1]
    
    return input*w + b

def predict_label(input, tuple):
    w = tuple[0]
    b = tuple[1]
 
    if (input*w + b > 0.5):
        return "The student will likely pass"
    else:
        return "The student will likely fail"

if __name__ == "__main__":

    # Hours studied
    X = [1, 2, 4, 5, 7] 
    # Actual scores (y)
    y = [50, 55, 70, 75, 85]

    main(X, y, DEFAULTS.lr, DEFAULTS.epochs)