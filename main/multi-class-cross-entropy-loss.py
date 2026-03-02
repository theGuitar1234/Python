from turanpy import classification
from turanpy.config import DEFAULTS

def main(y, y_index, X, W, b):
    print(classification.cross_entropy_index(y_index, X, W, b, DEFAULTS.eps))
    print(classification.multiclass_cross_entropy_loss(y, X, W, b, DEFAULTS.eps))

if __name__ == "__main__":
    
    X = [
        [0.2, 1.1],
        [0.4, 0.9],
        [1.2, 0.1],
        [1.0, 0.2],
        [2.0, 1.5],
        [2.2, 1.7],
    ]

    y_index = [0, 0, 1, 1, 2, 2]

    y = [
        [1,0,0],
        [1,0,0],
        [1,0,0],
        [1,0,0],
        [0,1,0],
        [0,1,0],
        [0,1,0],
        [0,0,1],
        [0,0,1],
        [0,0,1],
    ]

    W = [
        [-1.0,  1.2],
        [ 0.8, -0.4],
        [ 1.1,  0.2],
    ]

    b = [1.0, 0.0, -1.0]

    main(y, y_index, X, W, b)

    # 0.5397047768167696
    # 1.3431756173620357