import pandas as pd
df_info = pd.DataFrame({
  "Roll": [1,2,3,4],
  "Name": ["Ram", "Hari", "Shyam", "Ramesh"],
  "Age": [21,23,22,23],
  "Address": ["kathmandu", "Lalitpur", "Bhaktapur", "Dhanusha"]
})

df_marks = pd.DataFrame({
  "Roll": [1,1,2,2,3,3,4,4],
  "Subject": ["Math","Sciece", "Math","Sciece", "Math","Sciece", "Math","Sciece"],
  "1stTerminal": [80,75,78,90,98,88,56,45],
  "2ndTerminal": [75,34,67,87,90,99,56,76],
  "3rdTerminal": [88,86,68,56,89,56,77,66]
})

df_marks["Average_Marks"]= df_marks[["1stTerminal", "2ndTerminal", "3rdTerminal"]].mean(axis=1)

df_final = pd.merge(df_info,df_marks, on="Roll")

print(df_final)




