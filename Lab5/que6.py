'''6. Identify outliers in the Marks column using the IQR method. 
Remove the outliers from the dataset.'''

import pandas as pd

df = pd.read_csv("data1.csv")

Q1 = df["Marks"].quantile(0.25)
Q3 = df["Marks"].quantile(0.75)

IQR = Q3 - Q1

lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

df = df[(df["Marks"] >= lower_bound) & (df["Marks"] <= upper_bound)]

print(df)