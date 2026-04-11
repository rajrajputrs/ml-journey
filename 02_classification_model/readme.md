# 🩺 Diabetes Prediction using Machine Learning

## 📌 Objective
The goal of this project is to predict whether a person has diabetes using medical attributes and classification techniques.

---

## 📊 Dataset
- Pima Indians Diabetes Dataset
- Features include:
  - Glucose
  - Blood Pressure
  - BMI
  - Insulin
  - Skin Thickness
  - Age
  - Diabetes Pedigree Function
- Target:
  - Outcome (0 = No Diabetes, 1 = Diabetes)

---

## ⚙️ Data Preprocessing

### 1. Handling Invalid Values
- Replaced zero values in key columns (Glucose, BloodPressure, BMI, Insulin, SkinThickness) with median values.

### 2. Outlier Removal
- Applied IQR (Interquartile Range) method to remove outliers.
- Improved data quality and reduced noise.

### 3. Feature Selection
- Removed less impactful features:
  - Insulin
  - SkinThickness
  - DiabetesPedigreeFunction

### 4. Feature Scaling
- Applied StandardScaler to normalize feature values.

---

## 📊 Exploratory Data Analysis (EDA)

Performed visual analysis to understand the dataset:

- Distribution of diabetes cases (Outcome)
- Correlation analysis with target variable
- Detection of important features

### 🔍 Key Insights:
- Glucose has the strongest correlation with diabetes outcome  
- BMI and Age show moderate influence  
- Dataset initially contained outliers and invalid values  

---

## 🤖 Model Building

- Model: Logistic Regression  
- Solver: liblinear  
- Class Handling: Balanced (to handle class imbalance)  
- Train-Test Split: 80-20 (with stratification)  

---

## 📈 Model Evaluation

- Accuracy: 72.18%

## 📊 Visualizations

- Outcome Distribution (Countplot)
- Correlation Heatmap (focused on Outcome)
- Confusion Matrix Heatmap

---

## 🧠 Key Learnings

- Importance of handling invalid data  
- Effect of outliers on model performance  
- Feature selection improves model efficiency  
- Role of class imbalance and how to handle it  
- Understanding classification metrics beyond accuracy  

---

## 🚀 Future Improvements

- Try advanced models (Random Forest, XGBoost)
- Hyperparameter tuning
- Cross-validation
- Deploy model using Flask / API

---

## 📁 Project Structure
