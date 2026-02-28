import pandas as pd

data = {
    "ID": [101, 102, 102, 103, 104, 105],
    "Name": [" john", "SARA ", "SARA ", "mike", None, "Anna  "],
    "Age": ["25", "30", "30", "-5", "abc", "40"],
    "Department": ["sales", "HR", "HR", "Sales ", " hr", "SALES"],
    "Salary": ["50000", "60000", "60000", "70000", "80000", "-10000"]
}

df = pd.DataFrame(data)
print(df)
df["Name"]=df["Name"].str.strip().str.title()
df["Department"]=df["Department"].str.strip().str.lower()
df["Age"]=pd.to_numeric(df["Age"],errors="coerce")
df["Salary"]=pd.to_numeric(df["Salary"],errors="coerce")
df=df.drop_duplicates()
df=df.dropna(subset=["Name"])
df=df[df["Age"]>=0]
df=df[df["Salary"]>=0]
print(df)