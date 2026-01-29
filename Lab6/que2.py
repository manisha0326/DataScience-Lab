'''2. Using the same dataset, compute the correlation coefficient. 
   Interpret whether the relationship is positive, negative, or weak. 
   Visualize it using a seaborn regression plot.'''


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

studies={
    "hours" : [11,12,13,14,15,16,17,18,19,20],
    "marks" : [80,81,82,83,84,85,86,87,88,89]
}

df  = pd.DataFrame(studies)

correlation = df.corr()
print("the correlation:")
print(correlation)

sns.regplot(x="hours", y="marks", data=df, marker = "v")
plt.title("Regression Plot: Hours vs Marks")
plt.show()




# import numpy as np
# import pandas as pd
# import matplotlib.pyplot as plt

# import seaborn as sns

# hours = np.array([1,2,3,4,5,6,7,8,9,10])
# marks = np.array([35,40,50,55,60,65,70,80,85,90])

# df_study = pd.DataFrame({
#     "Hours_Studied": hours,
#     "Marks": marks
# })
# print(df_study)

# corr_study = df_study.corr()
# print("Correlation:\n", corr_study)


# sns.regplot(x="Hours_Studied", y="Marks", data=df_study)
# plt.title("Hours Studied vs Marks (Regression)")
# plt.show()

