from turanpy.classification import cross_entropy_loss
from turanpy.config import DEFAULTS

def main(X, y, w, b):
    res = cross_entropy_loss(X, y, w, b, DEFAULTS.epochs)
    print(f"""
        For the weight {w} and bias {b}
        the accuracy of the linear model is: {res}    
    """)

if __name__ == "__main__":

    X = [0, 0.5, 1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5, 5.5, 6, 6.5, 7, 7.5, 8, 8.5, 9, 10]
    y = [0,   0,  0,   0, 0,   0, 1,   0, 1,   0,  1,   1,  1,   1,  1,   1,  1,   1,  1,  1]

    w = 1.4562492955153008
    b = -5.448905251095365

    main(X, y, w, b)
    # For the weight 1.4562492955153008 and bias -5.448905251095365,
    # the accuracy of the linear model is: -0.0015504892253229258