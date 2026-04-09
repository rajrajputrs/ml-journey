import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score,classification_report, confusion_matrix
from sklearn.model_selection import train_test_split

# Data Reading
data = pd.read_csv("C:\\Users\\rajra\\OneDrive\\Desktop\\diabetes.csv")
print(data.head())

# Handle Invalid Zeros
col=["Glucose", "BloodPressure", "SkinThickness", "Insulin", "BMI"]
for c in col:
    data[c] = data[c].replace(0, data[c].median())
print("Handled missing values", data.isnull().sum().sum())

# Remove Outliers (IQR method)
def remove_outliers_iqr(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    return df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
for c in col:
    data = remove_outliers_iqr(data, c)

# EDA
print(data.info())
print(data.describe())

# Data Preprocessing
# Handle missing values if any
data = data.dropna()

# Split Data into Features and Target
X = data.drop(["Outcome", "Insulin", "SkinThickness","DiabetesPedigreeFunction"], axis=1)
y = data["Outcome"]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42, stratify=y)

# Feature Scaling
scaler = StandardScaler()
X_train_scaled = scaler.fit_transform(X_train)
X_test_scaled = scaler.transform(X_test)

# Model Training
model = LogisticRegression(class_weight="balanced",solver='liblinear', max_iter=1000)
model.fit(X_train_scaled, y_train)

# Prediction
y_pred = model.predict(X_test_scaled)

# Evaluation
print("Accuracy:", accuracy_score(y_test, y_pred))
print("Confusion Matrix:\n", confusion_matrix(y_test, y_pred))
print("Classification Report:\n", classification_report(y_test, y_pred))

# Visualization
# Outcome Distribution

sns.countplot(x="Outcome", data=data)
plt.xlabel("Diabetes Outcome")
plt.ylabel("Count")
plt.title("Diabetes Distribution")
plt.show()

# Correlation Heatmap

corr = data.corr()
corr_target = corr["Outcome"].drop("Outcome").sort_values(ascending=False)
plt.figure(figsize=(6,8))
sns.heatmap(corr_target.to_frame(), annot=True, cmap="coolwarm")
plt.title("Feature Correlation with Outcome")
plt.show()

# Confusion Matrix Heatmap
cm = confusion_matrix(y_test, y_pred)
sns.heatmap(cm, annot=True, fmt='d', cmap='Blues')
plt.title("Confusion Matrix")
plt.xlabel("Predicted")
plt.ylabel("Actual")
plt.show()