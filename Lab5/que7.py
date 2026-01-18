'''7. Create a new column by transforming Marks (e.g., Marks / 10). 
Rename columns and save the cleaned dataset to a CSV file.'''

import pandas as pd
df = pd.read_csv("data1.csv")

df["New_Marks"] = df["Marks"] / 10

df.rename(columns={"Marks": "Total_Marks"}, inplace=True)

df.to_csv("cleaned_data.csv", index=False)
print(df)

print("Cleaned data saved successfully")

