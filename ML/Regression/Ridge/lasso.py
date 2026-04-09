import pandas as pd
from sklearn.linear_model import Lasso
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error, r2_score

# Sample data
data={
    "size":[1000, 1500, 2000, 2500, 3000],
    "bedrooms":[2, 3, 4, 4, 5],
    "price":[200000, 300000, 400000, 500000, 600000],
    "noise": [10, 20, 30, 40, 50]
}
df = pd.DataFrame(data)
print(df)

# Splitting the data into features and target variable
X = df[["size", "bedrooms", "noise"]]
y = df["price"]

# Standardizing the features
scaler = StandardScaler()
X=scaler.fit_transform(X)

# Train-test split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Fitting the Lasso Regression model
model = Lasso(alpha=0.1)
model.fit(X_train, y_train)

# Predicting values
y_pred = model.predict(X_test)
print("Predicted values:", y_pred)

# Evaluating the model
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print("Mean Squared Error:", mse)
print("R^2 Score:", r2)

# Check weights and bias
print("Weights:", model.coef_)
print("Bias:", model.intercept_)

# Experimenting with different alpha values
alphas = [0.01, 0.1, 1, 10]
for alpha in alphas:
    model = Lasso(alpha=alpha)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    mse = mean_squared_error(y_test, y_pred)
    r2 = r2_score(y_test, y_pred)
    print(f"Alpha: {alpha}->Weights: {model.coef_}, Bias: {model.intercept_}, MSE: {mse}, R^2: {r2}")