import matplotlib.pyplot as plt
import pandas as pd

df = pd.read_csv(r"C:\Users\Student\Downloads\weather.csv")
print(df.head())


df = pd.read_csv("/mnt/data/1c56f46a-0c43-4516-abf3-28602ed467aa.csv")
df.columns = df.columns.str.strip()
df["temperature"] = pd.to_numeric(df["temperature"], errors="coerce")
df["day"] = pd.to_datetime(df["year"].astype(str) + "-" + df["day"])

overall_avg = round(df["temperature"].mean(),2)

df["month"] = df["day"].dt.month
monthly_avg = df.groupby("month")["temperature"].mean()

hottest = df.loc[df["temperature"].idxmax()]
coldest = df.loc[df["temperature"].idxmin()]

def season(month):
    if month in [12,1,2]: return "Winter"
    if month in [3,4,5]: return "Spring"
    if month in [6,7,8]: return "Summer"
    return "Autumn"

df["season"] = df["month"].apply(season)
seasonal_avg = df.groupby("season")["temperature"].mean()

plt.figure()
monthly_avg.plot(kind="bar")
plt.savefig("/mnt/data/monthly.png")
plt.close()

plt.figure()
plt.plot(df["day"], df["temperature"])
plt.savefig("/mnt/data/trend.png")
plt.close()

overall_avg, monthly_avg, hottest, coldest, seasonal_avg

# aa
