import pandas as pd


df1 = pd.read_csv('personality_dataset.csv')

print(df1.head())
print(df1.info())
print(df1.describe())
