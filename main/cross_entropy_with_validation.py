import random
import math


def sigmoid(x):
    return 1.0 / (1.0 + math.exp(-x))


def dsigmoid_from_output(a):
    return a * (1.0 - a)


def loss_one(y_hat, y):
    eps = 1e-15
    p = y_hat[0]

    if p < eps:
        p = eps
    elif p > 1.0 - eps:
        p = 1.0 - eps

    return -(y[0] * math.log(p) + (1 - y[0]) * math.log(1 - p))


def init_layers(n_inputs, n_hidden, n_outputs):
    W1 = [
        [random.uniform(-1.0, 1.0) for _ in range(n_inputs)]
        for _ in range(n_hidden)
    ]

    b1 = [random.uniform(-1.0, 1.0) for _ in range(n_hidden)]

    W2 = [
        [random.uniform(-1.0, 1.0) for _ in range(n_hidden)]
        for _ in range(n_outputs)
    ]

    b2 = [random.uniform(-1.0, 1.0) for _ in range(n_outputs)]

    return [W1, b1, W2, b2]



def forward_one(x, WB):
    W1, b1, W2, b2 = WB

    z1 = []
    a1 = []

    for j in range(len(W1)):
        total = b1[j]

        for i in range(len(x)):
            total += W1[j][i] * x[i]

        z1.append(total)
        a1.append(sigmoid(total))

    z2 = []
    a2 = []

    for k in range(len(W2)):
        total = b2[k]

        for j in range(len(a1)):
            total += W2[k][j] * a1[j]

        z2.append(total)
        a2.append(sigmoid(total))

    return [z1, a1, z2, a2]



def backward_one(x, y, WB, cache):
    W1, b1, W2, b2 = WB
    z1, a1, z2, a2 = cache

    delta2 = []

    for k in range(len(a2)):
        y_hat = a2[k]
        delta = y_hat - y[k]
        delta2.append(delta)

    dW2 = [
        [0.0 for _ in range(len(a1))]
        for _ in range(len(W2))
    ]

    db2 = [0.0 for _ in range(len(W2))]

    for k in range(len(W2)):
        for j in range(len(a1)):
            dW2[k][j] = delta2[k] * a1[j]

        db2[k] = delta2[k]

    delta1 = []

    for j in range(len(a1)):
        back_signal = 0.0

        for k in range(len(W2)):
            back_signal += delta2[k] * W2[k][j]

        delta = back_signal * dsigmoid_from_output(a1[j])
        delta1.append(delta)

    dW1 = [
        [0.0 for _ in range(len(x))]
        for _ in range(len(W1))
    ]

    db1 = [0.0 for _ in range(len(W1))]

    for j in range(len(W1)):
        for i in range(len(x)):
            dW1[j][i] = delta1[j] * x[i]

        db1[j] = delta1[j]

    return [dW1, db1, dW2, db2]



def update_layers(WB, grads, lr):
    W1, b1, W2, b2 = WB
    dW1, db1, dW2, db2 = grads

    for j in range(len(W1)):
        for i in range(len(W1[j])):
            W1[j][i] -= lr * dW1[j][i]

        b1[j] -= lr * db1[j]

    for k in range(len(W2)):
        for j in range(len(W2[k])):
            W2[k][j] -= lr * dW2[k][j]

        b2[k] -= lr * db2[k]



def predict_one(x, WB):
    cache = forward_one(x, WB)
    return cache[3]



def evaluate_dataset(X, Y, WB):
    total_loss = 0.0
    correct = 0

    for i in range(len(X)):
        y_hat = predict_one(X[i], WB)
        total_loss += loss_one(y_hat, Y[i])

        predicted_class = 1 if y_hat[0] >= 0.5 else 0
        if predicted_class == Y[i][0]:
            correct += 1

    avg_loss = total_loss / len(X)
    accuracy = correct / len(X)
    return avg_loss, accuracy



def shuffle_dataset(X, Y, seed=42):
    pairs = list(zip(X, Y))
    random.Random(seed).shuffle(pairs)
    X_shuffled = [x for x, _ in pairs]
    Y_shuffled = [y for _, y in pairs]
    return X_shuffled, Y_shuffled



def train_validation_split(X, Y, val_ratio=0.2, seed=42):
    X_shuffled, Y_shuffled = shuffle_dataset(X, Y, seed)

    val_size = max(1, int(len(X_shuffled) * val_ratio))

    X_val = X_shuffled[:val_size]
    Y_val = Y_shuffled[:val_size]

    X_train = X_shuffled[val_size:]
    Y_train = Y_shuffled[val_size:]

    return X_train, Y_train, X_val, Y_val



def train(X_train, Y_train, X_val, Y_val, n_inputs, n_hidden, n_outputs, lr, epochs):
    WB = init_layers(n_inputs, n_hidden, n_outputs)

    best_val_loss = float("inf")
    best_WB = None
    patience = 400
    patience_counter = 0

    for epoch in range(epochs):
        total_train_loss = 0.0

        train_pairs = list(zip(X_train, Y_train))
        random.shuffle(train_pairs)

        for x, y in train_pairs:
            cache = forward_one(x, WB)
            y_hat = cache[3]
            total_train_loss += loss_one(y_hat, y)

            grads = backward_one(x, y, WB, cache)
            update_layers(WB, grads, lr)

        train_loss = total_train_loss / len(X_train)
        val_loss, val_acc = evaluate_dataset(X_val, Y_val, WB)

        if val_loss < best_val_loss:
            best_val_loss = val_loss
            best_WB = [
                [row[:] for row in WB[0]],
                WB[1][:],
                [row[:] for row in WB[2]],
                WB[3][:],
            ]
            patience_counter = 0
        else:
            patience_counter += 1

        if epoch % 200 == 0:
            print(
                "epoch =", epoch,
                "train_loss =", round(train_loss, 6),
                "val_loss =", round(val_loss, 6),
                "val_acc =", round(val_acc, 4)
            )

        if patience_counter >= patience:
            print("early stopping at epoch", epoch)
            break

    return best_WB if best_WB is not None else WB


if __name__ == "__main__":
    X_full = [
        [0.2, 1.1],
        [0.3, 1.0],
        [0.4, 0.9],
        [0.5, 1.2],
        [0.6, 1.0],

        [1.2, 0.1],
        [1.0, 0.2],
        [1.3, 0.3],
        [1.5, 0.4],
        [1.4, 0.2],

        [2.0, 1.5],
        [2.2, 1.7],
        [2.1, 1.6],
        [1.9, 1.4],
        [2.3, 1.8],
    ]

    Y_full = [
        [0],
        [0],
        [0],
        [0],
        [0],

        [1],
        [1],
        [1],
        [1],
        [1],

        [1],
        [1],
        [1],
        [1],
        [1],
    ]

    X_test = [
        [0.25, 1.05],
        [0.35, 0.95],
        [0.45, 1.10],
        [0.55, 0.85],
        [0.65, 1.15],

        [1.10, 0.15],
        [1.25, 0.25],
        [1.35, 0.35],
        [1.45, 0.30],
        [1.55, 0.45],

        [1.95, 1.45],
        [2.05, 1.55],
        [2.15, 1.65],
        [2.25, 1.75],
        [2.35, 1.85],
    ]

    Y_test = [
        [0],
        [0],
        [0],
        [0],
        [0],

        [1],
        [1],
        [1],
        [1],
        [1],

        [1],
        [1],
        [1],
        [1],
        [1],
    ]

    X_train, Y_train, X_val, Y_val = train_validation_split(X_full, Y_full, val_ratio=0.2, seed=42)

    print("train size =", len(X_train))
    print("validation size =", len(X_val))
    print("test size =", len(X_test))

    WB = train(
        X_train, Y_train,
        X_val, Y_val,
        n_inputs=2,
        n_hidden=4,
        n_outputs=1,
        lr=0.5,
        epochs=3000,
    )

    val_loss, val_acc = evaluate_dataset(X_val, Y_val, WB)
    test_loss, test_acc = evaluate_dataset(X_test, Y_test, WB)

    print("final validation loss =", round(val_loss, 6), "validation accuracy =", round(val_acc, 4))
    print("final test loss =", round(test_loss, 6), "test accuracy =", round(test_acc, 4))
