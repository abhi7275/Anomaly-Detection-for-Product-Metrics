import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Load dataset
df = pd.read_csv("product_engagement_2yrs.csv", parse_dates=["date"])

# Sort by date just in case
df = df.sort_values("date")

# Calculate Z-scores for Daily Active Users
mean_dau = df['daily_active_users'].mean()
std_dau = df['daily_active_users'].std()

df['zscore_dau'] = (df['daily_active_users'] - mean_dau) / std_dau

# Mark anomalies: Z-score threshold (e.g., |z| > 2)
z_threshold = 1.5
df['zscore_anomaly'] = np.where(np.abs(df['zscore_dau']) > z_threshold, 1, 0)

# Print summary
print(f"Total anomalies found using Z-score: {df['zscore_anomaly'].sum()}")

# Plotting
plt.figure(figsize=(14, 6))
sns.lineplot(data=df, x="date", y="daily_active_users", label="Daily Active Users", color='blue')
sns.scatterplot(data=df[df['zscore_anomaly'] == 1], x="date", y="daily_active_users", color='red', label="Anomalies")
plt.title("Z-Score Anomaly Detection on Daily Active Users")
plt.xlabel("Date")
plt.ylabel("Users")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
