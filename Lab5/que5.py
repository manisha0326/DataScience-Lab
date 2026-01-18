'''5. Detect duplicate rows in the dataset. 
Remove duplicates and verify the result.'''

import pandas as pd

df = pd.read_csv("data.csv")

print(df.duplicated())

df = df.drop_duplicates()

# df.to_csv("data1.csv", index=False)

print("After removing duplicates: ", df.shape)

