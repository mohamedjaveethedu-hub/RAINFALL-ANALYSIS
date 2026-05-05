import pandas as pd
import matplotlib.pyplot as plt
df = pd.read_csv("rainfall.csv")
print("Data loaded successfully.")
print("First 5 rows:")
print(df.head())
print("\nData info:")
print(df.info())

#fix column names
df.columns = df.columns.str.strip()
#check for missing values
print(df.isnull().sum())

#convert numeric columns
for col in df.columns[2:]:
    df[col] = pd.to_numeric(df[col],errors='coerce')

#which district has the highest rainfall?
df['total'] = df.iloc[:,2:].sum(axis=1)
top = df.sort_values(by='total',ascending=False)
print(top[['District','total']].head())

#monthly rainfall trend
monthly_avg = df.iloc[:,2:-1].mean()
print('monthly average',monthly_avg)

#top 5 district comparison
top5 = top.head(5)
print(top5[['District','total']])

#top 5 rainfall bar chart
plt.figure()
plt.bar(top5['District'],top5['total'])
plt.title('top 5 district by rainfall')
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig('outputs/top5_rainfall.png')
#monthly trend
plt.figure()
monthly_avg.plot(kind='line')
plt.title('monthly rainfall trend')
plt.tight_layout()
plt.savefig('outputs/monthly_trend.png')
