import pandas as pd
from prophet import Prophet
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("product_engagement_2yrs.csv", parse_dates=["date"])
df = df.sort_values("date")

# Prepare for Prophet: rename columns
prophet_df = df[["date", "daily_active_users"]].rename(columns={"date": "ds", "daily_active_users": "y"})

# Initialize and fit Prophet
model = Prophet(daily_seasonality=True, yearly_seasonality=True)
model.fit(prophet_df)

# Create future dataframe and forecast
future = model.make_future_dataframe(periods=0)
forecast = model.predict(future)

# Merge forecast with actual data
results = pd.merge(df, forecast[["ds", "yhat", "yhat_lower", "yhat_upper"]], left_on="date", right_on="ds", how="left")

# Anomaly detection: if actual outside predicted bounds
results["prophet_anomaly"] = ((results["daily_active_users"] < results["yhat_lower"]) |
                              (results["daily_active_users"] > results["yhat_upper"])).astype(int)

# Plot
plt.figure(figsize=(14, 6))
plt.plot(results["date"], results["daily_active_users"], label="Actual", color="blue")
plt.plot(results["date"], results["yhat"], label="Forecast", color="green", alpha=0.6)
plt.fill_between(results["date"], results["yhat_lower"], results["yhat_upper"], color="gray", alpha=0.3, label="Confidence Interval")
plt.scatter(results[results["prophet_anomaly"] == 1]["date"],
            results[results["prophet_anomaly"] == 1]["daily_active_users"],
            color='red', label="Anomaly", zorder=5)
plt.title("Prophet-Based Anomaly Detection (Daily Active Users)")
plt.xlabel("Date")
plt.ylabel("Users")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.show()
