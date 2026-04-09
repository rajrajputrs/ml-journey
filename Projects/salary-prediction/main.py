import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score

# Data Reading
data = pd.read_csv("C:\\Users\\rajra\\OneDrive\\Desktop\\ML-Journey\\Projects\\salary-prediction\\data\\Salary_dataset.csv")
print(data.head())

# EDA
print(data.info())
print(data.describe())

# Data Preprocessing
# Handle missing values if any
data = data.dropna()

# Split Data into Features and Target
X = data[["YearsExperience"]]
y = data["Salary"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Model Training
model= LinearRegression()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Mean Squared Error:", mean_squared_error(y_test, y_pred))
print("R^2 Score:", r2_score(y_test, y_pred))

# Visualization
plt.scatter(X, y, color='blue', label='Actual Data')
plt.plot(X, model.predict(X), color='red', label='Predicted Line')
plt.xlabel('Years of Experience')
plt.ylabel('Salary')
plt.title('Salary Prediction')
plt.legend()
plt.show()