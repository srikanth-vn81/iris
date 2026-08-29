import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('Iris.csv')
print(df.head())
print(df.columns)
print(df.info())

# Descriptive Statistics
des_stat = df.describe(include=float).T
print(des_stat)

# Visualisation
boxplot = sns.boxplot(data=df,x='SepalLengthCm')
boxplot

