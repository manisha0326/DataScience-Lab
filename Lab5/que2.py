'''2. Load a CSV file into a DataFrame. 
Display column names, data types, and basic statistics.'''

import pandas as pd

df = pd.read_csv("data.csv")

print("COLUMNS\n")
print(df.columns)

print("DTYPES")
print( df.dtypes)

print("DESCRIBE")
print(df.describe())