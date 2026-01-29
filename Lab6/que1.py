'''1. Create a dataset of hours studied and marks scored for 10 students. 
   Calculate the covariance between the two variables. 
   Plot the data using a scatter plot.'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

studies={
    "hours" : [11,12,13,14,15,16,17,18,19,20],
    "marks" : [80,81,82,83,84,85,86,87,88,89]
}

df  = pd.DataFrame(studies)

covariance = df.cov()
print("the covarience:")
print(covariance)

plt.scatter(df["hours"], df["marks"])
plt.xlabel("Hours Studied")
plt.ylabel("Marks")
plt.title("Hours Studied and marks scored of 10 students")
plt.show()



# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# hours = np.array([1,2,3,4,5,6,7,8,9,10])
# marks = np.array([35,40,50,55,60,65,70,80,85,90])

# df_study = pd.DataFrame({
#     "Hours_Studied": hours,
#     "Marks": marks
# })
# print(df_study)

# cov_study = df_study.cov()
# print("Covariance:\n", cov_study)

# plt.scatter(hours, marks)
# plt.xlabel("Hours Studied")
# plt.ylabel("Marks")
# plt.title("Hours Studied vs Marks")
# plt.show()