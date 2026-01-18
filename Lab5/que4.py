'''4. Check for missing values in the dataset. 
Fill missing numerical values with the mean.'''

import pandas as pd

df = pd.read_csv("data.csv")

print(df.isnull().sum())

df.fillna(df.mean(numeric_only=True), inplace=True)
# df.to_csv("data1.csv", index=True)
print(df)