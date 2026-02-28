import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.preprocessing import MinMaxScaler as mx

# Handling Missing Values
Marks = [90, 85, None, 88, None]
se=pd.Series(Marks)
print("Missing Values: ",se.isnull().sum())
se1=se.fillna(se.mean())
se2=se.fillna(se.median())
print(se1)
print(se2)

# Removing Duplicates and Fixing Inconsistencies

Name=["Raj", "raj"," RAJ"," Aman"]
City= ["Delhi"," delhi"," Mumbai"," Mumbai"]
dupl=pd.DataFrame({"Name":Name,"City": City})
print(dupl)
dupl["Name"]=dupl["Name"].str.title().str.strip()
dupl["City"]=dupl["City"].str.title().str.strip()
print(dupl.drop_duplicates())

#Data Types

import pandas as pd

data = {
    "Age": ["21", "22", "23", "24"],   # Stored as strings
    "Salary": ["50000", "60000", "55000", "52000"]
}

df = pd.DataFrame(data)

print(df.info())
df["Age"]=df["Age"].astype(int)
df["Salary"]=df["Salary"].astype(int)
print(df.info())

# Data Outliers

data = {
    "Sal": [50, 55, 60, 58, 1000]
}

sal = pd.DataFrame(data)
print(sal)
Q1=sal["Sal"].quantile(0.25)
Q2=sal["Sal"].quantile(0.75)
IQR=Q2-Q1
upper=Q2+1.5*IQR
lower=Q1-1.5*IQR
sal=sal[(sal["Sal"]>lower) & (sal["Sal"]<upper)]
print(sal)
plt.boxplot(sal["Sal"])
plt.show()

# Encoding Categorial Variables

df = pd.DataFrame({
    "Gender": ["Male", "Female", "Female", "Male"],
    "Education": ["Graduate", "Postgraduate", "School", "Graduate"]
})
df=pd.get_dummies(df,columns=["Gender"])
df["Education"]=df["Education"].map({"School":0,"Graduate":1,"Postgraduate":2})
print(df)

# Feature Scaling

data = {
    "Age": ["21", "22", "23", "24"],   # Stored as strings
    "Salary": ["50000", "60000", "55000", "52000"]
}
df=pd.DataFrame(data)
df=df.apply(pd.to_numeric)
print(mx().fit_transform(df))

df=(df-df.min())/(df.max()-df.min()) #manually
print(df)