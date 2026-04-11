import matplotlib.pyplot as plt
import time

plt.ion()

figure, ax = plt.subplots()
line, = ax.plot([], [])
# ax.set_xlim(-1, 1)
# ax.set_ylim(-1, 1)

X = [1, 2, 3, 4, 5]
Y = [2, 4, 6, 8, 10]

loss_data = []
step_data = []
    
def gd(X, Y, learning_rate=0.03, epochs=5000, step=100):
    w = 0.0
    b = 0.0
    for i in range(epochs):
        y_hat = [w*X[k] + b for k in range(len(X))]
        loss = [y_hat[t] - Y[t] for t in range(len(Y))]
        avg_loss = mean(loss)
        
        grad_w = 2*mean([loss[j]*X[j] for j in range(len(X))])
        grad_b = 2*avg_loss
        
        w = w - learning_rate*grad_w
        b = b = learning_rate*grad_b

        if i % step == 0:
            print(f"Loss : {avg_loss}")
            loss_data.append(avg_loss)
            step_data.append(i)
            line.set_data(loss_data, step_data)
            
            ax.relim()
            ax.autoscale_view()
            
            figure.canvas.draw_idle()
        plt.pause(0.05)
            
    return (w, b)

def mean(v):
    sum = 0.0
    for i in range(len(v)):
        sum += v[i]
    return sum/len(v)

w, b = gd(X, Y, 0.001, 50000, 10)
print(w, b)