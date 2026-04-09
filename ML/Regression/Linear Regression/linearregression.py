import numpy as np3
import matplotlib.pyplot as plt

# Features : [Size of the house (in sqft), Number of bedrooms]
x = np.array([[1000, 2], [1500, 3], [2000, 4], [2500, 5], [3000, 6]])
y = np.array([50, 75, 100, 125, 150])

# Initialize parameters

m = np.zeros(2) # Slope
b = 0 # Intercept

lr= 0.00001 # Learning rate
epochs = 1000 # Gradient Descent
# Gradient Descent

for epoch in range(epochs):
    y_pred = np.dot(x, m) + b # Predicted values\

    error = y_pred - y # Calculate error

    m_gradient = (2/len(x)) * np.dot(x.T, error) # Gradient for slope
    b_gradient = (2/len(x)) * np.sum(error) # Gradient for intercept

    m -= lr * m_gradient # Update slope
    b -= lr * b_gradient # Update intercept

# Plotting

plt.scatter(x[:, 0], y, color='blue', label='Actual')
plt.plot(x[:, 0], y_pred, color='red', label='Predicted')
plt.xlabel('Size of the house (in sqft)')
plt.ylabel('Price (in $1000s)')
plt.title('Linear Regression: House Price Prediction')
plt.legend()
plt.show()