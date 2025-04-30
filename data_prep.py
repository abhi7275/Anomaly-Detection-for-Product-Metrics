import numpy as np
import pandas as pd
from datetime import timedelta

# Config
np.random.seed(42)
start_date = "2022-01-01"
end_date = "2024-12-31"
date_range = pd.date_range(start=start_date, end=end_date)
n_days = len(date_range)

# Base values
trend = np.linspace(1000, 5000, n_days)  # Trend for DAU
weekly_seasonality = 300 * np.sin(2 * np.pi * date_range.dayofweek / 7)
yearly_seasonality = 500 * np.sin(2 * np.pi * date_range.dayofyear / 365)
noise = np.random.normal(0, 200, n_days)

# Engagement metrics
daily_active_users = trend + weekly_seasonality + yearly_seasonality + noise
click_through_rate = np.clip(np.random.normal(0.15, 0.03, n_days), 0.05, 0.3)
avg_session_duration = np.clip(np.random.normal(4, 1, n_days), 1, 8)  # in minutes
conversion_rate = np.clip(np.random.normal(0.04, 0.01, n_days), 0.01, 0.1)

# Inject anomalies in DAU
anomalies_idx = np.random.choice(n_days, size=20, replace=False)
daily_active_users = daily_active_users.astype(int)  # Ensure DAU is integer type

# Update the daily_active_users column in the DataFrame directly
df = pd.DataFrame({
    "date": date_range,
    "product_id": "google_product_001",
    "category": "Search",
    "daily_active_users": daily_active_users,
    "click_through_rate": click_through_rate,
    "avg_session_duration": avg_session_duration,
    "conversion_rate": conversion_rate,
    "is_anomaly": 0
})

# Inject anomalies into the DataFrame
df.loc[anomalies_idx, "daily_active_users"] += np.random.choice([-1500, 2000], size=20)
df.loc[anomalies_idx, "is_anomaly"] = 1  # Mark as anomalies

# Save to CSV
df.to_csv("product_engagement_2yrs.csv", index=False)
print("Dataset saved as product_engagement_2yrs.csv")
