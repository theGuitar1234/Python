from ..algebra.mean import mean_vector as mv
from ..algebra.dot_product import dot_product as dt
from ..calculus.sigmoid import sigmoid

def single_feature_gradient_descent(train_data, input, learning_rate, epochs=1000):
    w = 1000

    for _ in range(epochs):
        grad = 2*(w*input - train_data) * input
        w = w - learning_rate*grad
    
    return w

def MSE_gradient_descent(y, X, learning_rate, epochs):
    w = 0.0
    b = 0.0

    for _ in range(epochs):
        y_hat = [w*X[i] + b for i in range(len(X))]

        error = [y_hat[i] - y[i] for i in range(len(y_hat))]

        grad_w = 2*mv([error[i]*X[i] for i in range(len(error))])
        grad_b = 2*mv(error)

        w -= learning_rate*grad_w
        b -= learning_rate*grad_b
    
    return (w, b)

def single_class_logistic_gradient_descent(y, X, learning_rate, epochs):
    w = 0.0
    b = 0.0

    for _ in range(epochs):
        y_hat = [sigmoid(w*X[i] + b) for i in range(len(X))]

        error = [y_hat[i] - y[i] for i in range(len(y_hat))]

        grad_w = mv([error[i]*X[i] for i in range(len(error))])
        grad_b = mv(error) 

        w -= learning_rate*grad_w
        b -= learning_rate*grad_b
    
    print(w, b)
    
    return (w, b)

def multi_class_MSE_gradient_descent(y, X, learning_rate, epochs):
    w = [0.0] * len(X[0])
    b = 0.0

    for _ in range(epochs):
        y_hat = [dt(w, X[i]) + b for i in range(len(X))]

        error = [y_hat[i] - y[i] for i in range(len(y_hat))]

        grad_w = [0.0] * len(X[0])

        for j in range(len(X[0])):
            s = 0.0
            for i in range(len(X)):
                s += error[i] * X[i][j]
            grad_w[j] = (2.0 / len(X)) * s

        grad_b = (2.0 / len(X)) * sum(error)

        for j in range(len(X[0])):
            w[j] -= learning_rate * grad_w[j]
        b -= learning_rate * grad_b
    
    return (w, b)

def multi_class_logistic_gradient_descent(y, X, learning_rate, epochs):
    w = [0.0] * len(X[0])
    b = 0.0

    for _ in range(epochs):
        y_hat = [sigmoid(dt(w, X[i]) + b) for i in range(len(X))]

        error = [y_hat[i] - y[i] for i in range(len(y_hat))]

        grad_w = [0.0] * len(X[0])

        for j in range(len(X[0])):
            s = 0.0
            for i in range(len(X)):
                s += error[i] * X[i][j]
            grad_w[j] = s / len(X)

        grad_b = sum(error) / len(X)

        for j in range(len(X[0])):
            w[j] -= learning_rate * grad_w[j]
        b -= learning_rate * grad_b

    return (w, b)

if __name__ == "__main__":
    pass