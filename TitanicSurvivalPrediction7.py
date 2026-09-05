import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
data = pd.read_csv("Titanic Dataset.csv")
new_data = data.select_dtypes(include="number")
sns.boxplot(data=new_data)
plt.show()
from sklearn.preprocessing import StandardScaler
scalar = StandardScaler()
new_data = scalar.fit_transform(new_data)
print(new_data)