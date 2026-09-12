import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns 
data = pd.read_csv("Iris Dataset.csv")
data.isnull().sum()
data.describe()
labels = ["Id","SepalLengthCm","SepalWidthCm","PetalLengthCm",
          "PetalWidthCm"]
for label in labels:
    print("Distribution of",label)
    sns.boxplot(data[label])
    plt.show()
sns.heatmap(data.corr())
labels = ["Id","SepalLengthCm","SepalWidthCm","PetalLengthCm",
          "PetalWidthCm"]
for label in labels:
    print("Distribution of",label)
    sns.distplot(data[label])
    plt.show()
    labels = ["Id","SepalLengthCm","SepalWidthCm","PetalLengthCm",
          "PetalWidthCm"]
for label in labels:
    print("Skewness of",label)
    print(data[label].skew())
    