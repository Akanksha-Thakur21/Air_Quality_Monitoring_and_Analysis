import pandas as pd

df = pd.read_csv("city_day.csv")
print(df.head())
print(df.shape)
print(df.isnull().sum())
df.drop_duplicates(inplace=True)
numeric_cols = ['PM2.5','PM10','NO','NO2','NOx','NH3','CO','SO2','O3','Benzene','Toluene','Xylene','AQI']
for col in numeric_cols:
    df[col] = df[col].fillna(df[col].mean())

df['AQI_Bucket'] = df['AQI_Bucket'].fillna(df['AQI_Bucket'].mode()[0])
print(df.isnull().sum())
df.to_csv("cleaned_air_quality.csv", index=False)
print(df.describe())
city_aqi = df.groupby("City")["AQI"].mean()

print(city_aqi.sort_values(ascending=False))
import matplotlib.pyplot as plt

city_aqi.sort_values().plot(kind="bar")
plt.title("Average AQI by City")
plt.ylabel("AQI")
plt.show()
df["AQI"].hist()
plt.title("AQI Distribution")
plt.xlabel("AQI")
plt.ylabel("Frequency")
plt.show()
print(df["AQI_Bucket"].value_counts())

import matplotlib.pyplot as plt

city_aqi.sort_values(ascending=False).head(10).plot(kind="bar")

plt.title("Top 10 Most Polluted Cities")
plt.xlabel("City")
plt.ylabel("Average AQI")
plt.show()