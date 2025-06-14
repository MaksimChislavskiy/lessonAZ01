import pandas as pd


df1 = pd.read_csv('personality_dataset.csv')

print(df1.head())
print(df1.info())
print(df1.describe())
print('_' * 50)

df2 = pd.read_csv('dz.csv')
df2['City'] = df2['City'].fillna('Unknown')
df2['Salary'] = df2['Salary'].fillna(0)
print(df2[['City', 'Salary']])
group = df2.groupby('City')['Salary'].mean()
print('Средняя зарплата по городам:')
print(group)