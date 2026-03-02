from ..algebra.linear_model import lm
from ..calculus import softmax
from ..calculus import logits_multiclass
from ..calculus import sigmoid

import math

def MSEloss(train_data, input, w, b):
    sum = 0
    for i in range(len(train_data)):
        sum += (lm(w, input[i][0], b) - train_data[i])**2
    return sum/len(input)

def cross_entropy_loss(X, y, w, b, eps=1e-12):
    sum = 0
    for i in range(len(X)):
        p_hat = sigmoid(lm(w, X[i], b))
        sum += y[i]*math.log(p_hat + eps) - (1 - y[i])*math.log(1 - p_hat + eps)
    return -1/len(X) * sum

def multiclass_cross_entropy_loss(y, X, W, b, eps = 1e-12):
    total = 0.0
    N = len(X)

    for i in range(N):
        logits = logits_multiclass.lgts_mc(W, X[i], b)
        p = softmax(logits)
        total += sum(y[i][k] * math.log(p[k] + eps) for k in range(len(p)))

    return -total / N

def cross_entropy_index(y, X, W, b, eps=1e-12):
    total = 0.0
    N = len(X)

    for i in range(N):
        p = softmax(logits_multiclass.lgts_mc(W, b, X[i]))
        total += math.log(p[y[i]] + eps)

    return -total / N

if __name__ == "__main__":
    pass