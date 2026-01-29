'''6. Load a small dataset with height and weight values. 
   Calculate mean, variance, covariance, and correlation. 
   Plot the data using a seaborn jointplot.'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

height = [150, 155, 160, 165, 170, 175, 180]
weight = [50, 55, 60, 65, 70, 75, 80]

df = pd.DataFrame({
    "Height": height,
    "Weight": weight
})

print("Mean:", df.mean())
print("Variance:", df.var())
print("Covariance:", df.cov())
print("Correlation:", df.corr())

sns.jointplot(x="Height", y="Weight", data=df)
plt.show()