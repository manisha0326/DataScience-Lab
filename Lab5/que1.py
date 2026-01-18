'''1. Import pandas and create a DataFrame with columns: Name, Age, Marks. 
Display the first 5 rows and dataset shape.'''

import pandas as pd

data = {
  "Name": ["Ram", "Shyam", "Hari", "Ramesh", "Sita", "Gita", "Mohan"],
  "Age": [22, 21, 20, 23, 20, 21, 22],
  "Marks": [55, 78, 65, 90, 78, 55, 80]
}

df = pd.DataFrame(data)

print(df.head(5))

print("Shape: ", df.shape)

# df.to_csv("Lab\Lab5\data.csv", index=False)