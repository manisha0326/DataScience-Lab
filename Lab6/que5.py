'''5. Create two random numerical datasets with no clear relationship. 
   Compute their covariance and correlation. 
   Visualize them using a scatter plot and observe the pattern.'''

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

np.random.seed(1)

x = np.random.randint(1, 100, 50)
y = np.random.randint(1, 100, 50)

df = pd.DataFrame({"X": x, "Y": y})

print("Covariance:", df.cov())
print("Correlation:", df.corr())

plt.scatter(x, y)
plt.xlabel("X")
plt.ylabel("Y")
plt.title("Random  Numerical Data Scatter Plot")
plt.show()