import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import statistics as stats
data = pd.read_csv("Bestsellers with categories.csv")
data.head(5)
data.isnull().any()
data.fillna("N/A")
var1 = np.var(data["User Rating"])
std1 = np.std(data["User Rating"])
var2 = np.var(data["Price"])
std2 = np.std(data["Price"])
plt.hist(data["User Rating"],bins=np.arange(1,100,30))
plt.show()
plt.hist(data["Price"],bins=np.arange(1,100,20))
plt.show()