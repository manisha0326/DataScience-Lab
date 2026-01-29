'''7. Create a dataset where one variable increases linearly and another increases randomly. 
   Compute covariance and correlation. 
   Plot both cases and compare the results. '''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

x = np.arange(1, 11) 

y_linear = x * 5   
y_random = np.random.randint(1, 50, 10)

df_linear = pd.DataFrame({"X": x, "Y": y_linear})
df_random = pd.DataFrame({"X": x, "Y": y_random})

print("Linear Data Corvariance:", df_linear.cov())
print("Random Data Corvariance:", df_random.cov())

print("Linear Data Correlation:", df_linear.corr())
print("Random Data Correlation:", df_random.corr())


plt.scatter(x, y_linear)
plt.xlabel("X")
plt.ylabel("Y Linear")
plt.title("Linear Relationship")
plt.show()

plt.scatter(x, y_random)
plt.xlabel("X")
plt.ylabel("Y Random")
plt.title("Random Relationship")
plt.show()