import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
data = pd.read_csv("Titanic Dataset.csv")
data.head(5)
sns.boxplot(y=data["Age"],x=data["Embarked"])
plt.show()
sns.scatterplot(y=data["Age"],x=data["Parch"])
plt.show()
sns.scatterplot(y=data["Age"],x=data["SibSp"])
plt.show()
sns.scatterplot(y=data["Age"],x=data["Fare"])
plt.show()
sns.scatterplot(y=data["Gender"],x=data["Embarked"])
plt.show()
association_categorical = pd.crosstab(data["Gender"],data["Embarked"])
print(association_categorical)