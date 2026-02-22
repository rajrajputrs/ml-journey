import matplotlib.pyplot as plt
x=10
iterations=50
learning_rate=0.1
def derivative(x):
    return x*2
x_values = []

for i in range(iterations):
    grad = derivative(x)
    x = x - learning_rate * grad
    x_values.append(x)

plt.plot(x_values)
plt.title("Convergence of Gradient Descent")
plt.xlabel("Iteration")
plt.ylabel("x value")
plt.show()
