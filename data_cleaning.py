import pandas as pd
import numpy as np

df = pd.read_csv(r"C:\Users\rajra\OneDrive\Desktop\global_gdp_inflation_2000_2024.csv")

print(df.head())
print(df.info())
print(df.describe())