from turanpy import classification
from turanpy import calculus
from turanpy.config import DEFAULTS

import random 

def main(X, y):
    res = classification.single_class_logistic_gradient_descent(y, X, 0.01, DEFAULTS.epochs)
    for _ in range(5):
        h = random.randint(0, 10)
        print(f"Hours studied: {h}", predict_raw(h, res), predict_label(h, res))

def predict_raw(input, tuple):
    w = tuple[0]
    b = tuple[1]
    return calculus.sigmoid(input*w + b)

def predict_label(input, tuple):
    w = tuple[0]
    b = tuple[1]
 
    if (calculus.sigmoid(input*w + b) > 0.5):
        return "The student will likely pass"
    else:
        return "The student will likely fail"

if __name__ == "__main__":

    # # Hours studied
    # X = [1, 2, 4, 5, 7] 
    # # Actual scores (y)
    # y = [50, 55, 70, 75, 85]

    # X = [0.5, 1.0, 2.0, 3.0, 4.0, 5.0]
    # y = [0, 0, 0, 1, 1, 1]

    X = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 10]
    y = [0,   0,  0,   0, 0,   0, 1,   0, 1,   0,  1,   0,  0,   1,  1,   0,  1,   1,  1,  1]

    if __name__ == "__main__":
        main(X, y)
        # Hours studied: 9 0.9995276597013458
        # Hours studied: 4 0.5929301794798776
        # Hours studied: 5 0.862040397364535
        # Hours studied: 4 0.5929301794798776
        # Hours studied: 1 0.0181163858897732