

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


# temp = np.array([20,22,24,26,28,30,32,34,36,38])
# icecream = np.array([100,120,140,160,180,200,220,240,260,280])

np.random.seed(42)

temp = np.random.randint(20, 40, 10)
icecream = temp * 5 + np.random.randint(-10, 10, 10)

df = pd.DataFrame({
    "temperature":temp,
    "Icecream_sales":icecream
})

print("Covariance:", df.cov())

plt.scatter(temp,icecream)
plt.xlabel("Temperature")
plt.ylabel("Icecream Sales")
plt.title("Temperature and Icecream Sales")
plt.show()
