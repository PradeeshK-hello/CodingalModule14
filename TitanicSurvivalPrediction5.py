import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
data = pd.read_csv("Titanic Dataset.csv")
data.head(5)
sns.boxplot(y=data["Age"],x=data["Pclass"])
plt.title("Distribution of Age and Class")
plt.show()