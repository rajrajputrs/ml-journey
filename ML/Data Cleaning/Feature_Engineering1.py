import pandas as pd
import numpy as np

data = {
    "Age": [22, 30, 25, 28, 35, 40, 29],
    "Salary": [30000, 80000, 40000, 50000, 120000, 150000, 52000],
    "Department": ["Sales", "HR", "Sales", "Marketing", "HR", "Marketing", "Sales"],
    "Join_Date": ["2020-01-01", "2018-06-15", "2021-03-10",
                  "2019-07-23", "2017-11-11", "2016-05-05", "2022-08-01"]
}

df = pd.DataFrame(data)
df["Join_Date"]=pd.to_datetime(df["Join_Date"])
df["Join_Day"]=pd.to_datetime(df["Join_Date"]).dt.day_name()
df["Join_Month"]=pd.to_datetime(df["Join_Date"]).dt.month_name()
df["Join_Year"]=pd.to_datetime(df["Join_Date"]).dt.year
df["Log_Salary"]=np.log(df["Salary"])
df["Age_Salary_Interaction"]=df["Age"]*df["Salary"]
df["Age_Group"]=pd.cut(df["Age"],bins=[0,25,40,100],labels=["Young","Adult","Old"])
avg_sal=df.groupby("Department")["Salary"].mean()
df["Avg_Salary"]=df["Department"].map(avg_sal)
print(df)