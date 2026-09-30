import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("Unemployment.csv")

# Clean column names
df.columns = df.columns.str.strip()

# Convert date
df["Date"] = pd.to_datetime(
    df["Date"],
    dayfirst=True,
    errors="coerce"
)

# Convert unemployment rate to numeric
df["Estimated Unemployment Rate (%)"] = pd.to_numeric(
    df["Estimated Unemployment Rate (%)"],
    errors="coerce"
)

# Remove missing values
df = df.dropna(
    subset=["Date", "Estimated Unemployment Rate (%)"]
)

# Display cleaned data
print("Cleaned Data:")
print(df.head())

print("\nAverage Unemployment Rate:")
print(df["Estimated Unemployment Rate (%)"].mean())
monthly = (
    df.groupby(pd.Grouper(key="Date", freq="MS"))
    ["Estimated Unemployment Rate (%)"]
    .mean()
    .dropna()
)

plt.figure(figsize=(12, 5))

plt.plot(monthly.index, monthly.values)

plt.title("Unemployment Rate Over Time")
plt.xlabel("Date")
plt.ylabel("Unemployment Rate (%)")

plt.xticks(rotation=45)
plt.grid(True)
plt.tight_layout()

plt.show()
pre_covid = df[
    (df["Date"] >= "2019-01-01") &
    (df["Date"] < "2020-03-01")
]

covid = df[
    (df["Date"] >= "2020-03-01") &
    (df["Date"] <= "2020-12-31")
]

pre_avg = pre_covid[
    "Estimated Unemployment Rate (%)"
].mean()

covid_avg = covid[
    "Estimated Unemployment Rate (%)"
].mean()

print("Pre-COVID Average:", pre_avg)
print("COVID Period Average:", covid_avg)
print("Difference:", covid_avg - pre_avg)
comparison = pd.Series({
    "Pre-COVID": pre_avg,
    "COVID Period": covid_avg
})

comparison.plot(kind="bar", color=["skyblue", "orange"])

plt.title("Unemployment Before and During COVID-19")
plt.ylabel("Average Unemployment Rate (%)")
plt.xticks(rotation=0)
plt.tight_layout()

plt.show()