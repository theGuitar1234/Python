from turanpy import classification
from turanpy import algebra
from turanpy import calculus
from turanpy.config import DEFAULTS

def main(X, y):
    res = classification.multi_class_logistic_gradient_descent(y, X, DEFAULTS.lr, DEFAULTS.epochs)
    print(f"""
        Predicted Weights for features: {res[0]}
        Predicted Biases: {res[1]}
    """)
    for i in X:
        print(f"For the features {i}, prediction: {predict(i, res)}")
    
def predict(input, tuple):
    w = tuple[0]
    b = tuple[1]
    
    return calculus.sigmoid(algebra.multi_class_lm(w, input, b))

if __name__ == "__main__":
    X = [
        [1, 5],
        [2, 10],
        [4, 20],
        [5, 25]
    ]

    y = [0, 0, 1, 1]

    main(X, y)
    # For the features [1, 5], prediction: 0.05990519151012022
    # For the features [2, 10], prediction: 0.24376560305131154
    # For the features [4, 20], prediction: 0.8918715597320146
    # For the features [5, 25], prediction: 0.9765939324123086