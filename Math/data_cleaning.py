import pandas as pd
import numpy as np
import matplotlib.pyplot as mlt

df = pd.read_csv(r"C:\Users\rajra\OneDrive\Desktop\Batsman_Data.csv")

mlt.scatter(df["Match_ID"],df["Runs"])
mlt.show()