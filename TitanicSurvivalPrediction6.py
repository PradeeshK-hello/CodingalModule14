import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
data = pd.read_csv("Titanic Dataset.csv")
sns.set_style("whitegrid")
sns.countplot(x="Survived",data=data)
plt.show()
sns.barplot(x="Gender",y="Survived",data=data,palette="Blues")
plt.show()
sns.countplot(x="Embarked",data=data)
plt.xticks(rotation=45,fontsize=10)
plt.show()