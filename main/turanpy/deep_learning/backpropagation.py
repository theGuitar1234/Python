from turanpy.algebra import multi_class_lm as linear_model

def backward_pass(D, A, WB, dhidden_act_from_output):
    for l in range(len(WB) - 2, -1, -1):
        D[l] = []

        for j in range(len(WB[l][0])):
            back_signal = 0.0

            for k in range(len(D[l + 1])):
                back_signal += D[l + 1][k] * WB[l + 1][0][k][j]

            delta = back_signal * dhidden_act_from_output(A[l + 1][j])
            D[l].append(delta)

    grad_W = [None] * len(WB)
    grad_b = [None] * len(WB)

    for l in range(len(WB)):
        grad_W[l] = []
        grad_b[l] = []

        for row in range(len(WB[l][0])):
            current_row = []

            for col in range(len(A[l])):
                current_row.append(D[l][row] * A[l][col])

            grad_W[l].append(current_row)
            grad_b[l].append(D[l][row])
    
    return grad_W, grad_b

def forward_pass(x, WB, hidden_act, output_act):
    Z = []
    A = [x]

    current_input = x

    for l in range(len(WB)):
        W, b = WB[l]

        current_z = []
        for j in range(len(W)):
            current_z.append(linear_model(W[j], current_input, b[j]))

        if l == len(WB) - 1:
            current_a = [output_act(z) for z in current_z]
        else:
            current_a = [hidden_act(z) for z in current_z]

        Z.append(current_z)
        A.append(current_a)

        current_input = current_a

    return Z, A

def update_parameters(WB, grad_W, grad_b, learning_rate):
    for l in range(len(WB)):
        for row in range(len(WB[l][0])):
            for col in range(len(WB[l][0][row])):
                WB[l][0][row][col] -= learning_rate * grad_W[l][row][col]

        for row in range(len(WB[l][1])):
            WB[l][1][row] -= learning_rate * grad_b[l][row]

def train(X, Y, WB, learning_rate, hidden_act, output_act, dact_from_output, loss, dloss_output_delta, epochs=5000):
    for i in range(epochs):
        epoch_loss = 0.0
        for j in range(len(X)):
            x = X[j]
            
            Z, A = forward_pass(x, WB, hidden_act, output_act)

            y_hat = A[-1][0]
            y = Y[j]

            epoch_loss += loss(y_hat, y)

            D = [None] * len(WB)
            D[-1] = [dloss_output_delta(y_hat, y)]

            grad_W, grad_b = backward_pass(D, A, WB, dact_from_output)
            
            update_parameters(WB, grad_W, grad_b, learning_rate)

        if i % 500 == 0:
            avg_loss = epoch_loss / len(X)
            print("epoch =", i, "avg_loss =", avg_loss)
        
    x1 = X[0]
    x2 = X[1]
    print(f"Final Predictions: {forward_pass(x1, WB, hidden_act, output_act)[1][-1]}")
    print(f"Final Predictions: {forward_pass(x2, WB, hidden_act, output_act)[1][-1]}")

    return WB

if __name__ == "__main__":
    pass