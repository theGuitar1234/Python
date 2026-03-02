from turanpy import classification
def main(X, y):
    res = classification.multi_class_MSE_gradient_descent(y, X, 0.0001, 50000)
    print(f"""
        Predicted Weights for features: {res[0]}
        Predicted Bias: {res[1]}
    """)

if __name__ == "__main__":
    X = [
        [1, 5],
        [2, 10],
        [4, 20],
        [5, 25]
    ]

    y = [50, 55, 70, 75]

    main(X, y)