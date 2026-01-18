'''3. Select rows where Marks > 60. 
Select only Name and Marks columns.'''

import pandas as pd
df = pd.read_csv("data.csv")

df_filter = df[df["Marks"] > 60][["Name", "Marks"]]

print(df_filter)