'''4. Calculate the correlation for the temperature vs ice-cream sales dataset. 
   Compare the covariance and correlation values. 
   Explain why correlation is easier to interpret. '''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(42)

temp = np.random.randint(20, 40, 10)
icecream = temp * 5 + np.random.randint(-10, 10, 10)

df = pd.DataFrame({
    "temperature":temp,
    "Icecream_sales":icecream
})

print("Correlation", df.corr())