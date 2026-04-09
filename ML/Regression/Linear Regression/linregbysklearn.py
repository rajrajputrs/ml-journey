from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LinearRegression

# Load the data
X = [[1], [2], [3], [4], [5]]
y = [2, 3, 5, 7, 11]

# Standardize the features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Create and fit the model
model = LinearRegression()
model.fit(X_scaled, y)

# Predict using the model
y_pred = model.predict(X_scaled)

# Print the coefficients
print("Coefficient (slope):", model.coef_[0])
print("Intercept:", model.intercept_)

# Plotting
import matplotlib.pyplot as plt
plt.scatter(X, y, color='blue', label='Actual')
plt.plot(X, y_pred, color='red', label='Predicted')
plt.xlabel('Feature (X)')
plt.ylabel('Target (y)')
plt.title('Linear Regression: Feature vs Target')
plt.legend()
plt.show()