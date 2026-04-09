import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures

# Sample data
X = np.array([1, 2, 3, 4, 5]).reshape(-1, 1)
y = np.array([1, 4, 9, 16, 25])

# Transforming the data to include polynomial features
polynomial_features = PolynomialFeatures(degree=2)
X_poly = polynomial_features.fit_transform(X)

# Fitting the Linear Regression model to the polynomial features
model = LinearRegression()
model.fit(X_poly, y)

# Predicting values
y_pred = model.predict(X_poly)

# Plotting the results
plt.scatter(X, y, color='red', label='Data Points') 
plt.plot(X, y_pred, color='blue', label='Polynomial Fit')
plt.title('Polynomial Regression')
plt.xlabel('X')
plt.ylabel('y')
plt.legend()
plt.show()