import random

from turanpy import calculus
from turanpy import classification

def main(X, y): 
    for _ in range(5):
        h = random.randint(0, 10)
        print(f"Hours studied: {h}", predict(h, y, X, 0.01, 50000))

def predict(input, y, X, learning_rate, epochs):
    tuple = classification.MSE_gradient_descent(y, X, learning_rate, epochs)
    w = tuple[0]
    b = tuple[1]
    return calculus.sigmoid(input*w + b)

if __name__ == "__main__":

    X = [0.5, 1.0, 2.0, 3.0, 4.0, 5.0]
    y = [0, 0, 0, 1, 1, 1]

    main(X, y)
    # Hours studied: 5 1.1753424657534224
    # Hours studied: 10 2.5726027397260194
    # Hours studied: 8 2.0136986301369806
    # Hours studied: 2 0.3369863013698644
    # Hours studied: 10 2.5726027397260194