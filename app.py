import streamlit as st
import pandas as pd
import altair as alt

# --- Load Data ---
@st.cache_data
def load_data():
    df = pd.read_csv("product_engagement_combined.csv", parse_dates=["date"])
    return df

df = load_data()

# --- Sidebar Filters ---
st.sidebar.header("📅 Filters & Controls")
start_date, end_date = st.sidebar.date_input("Select Date Range", [df.date.min(), df.date.max()])
selected_methods = st.sidebar.multiselect("Show Anomaly Method(s)", ["Z-score", "Prophet"], default=["Z-score", "Prophet"])

# Filter by date
df = df[(df["date"] >= pd.to_datetime(start_date)) & (df["date"] <= pd.to_datetime(end_date))]

# --- KPIs ---
st.title("📊 Product Engagement Anomaly Dashboard")
col1, col2, col3 = st.columns(3)
col1.metric("CTR", f"{df['click_through_rate'].mean():.2%}")
col2.metric("Avg Session Duration", f"{df['avg_session_duration'].mean():.2f} min")
col3.metric("Conversion Rate", f"{df['conversion_rate'].mean():.2%}")

# --- Anomaly Chart ---
st.subheader("📈 Daily Active Users with Z-score and Prophet Anomalies")

# Base Line Chart
base = alt.Chart(df).mark_line(color="steelblue").encode(
    x="date:T",
    y="daily_active_users:Q",
    tooltip=["date:T", "daily_active_users"]
)

# Z-score Anomalies
z_anomaly_layer = alt.Chart(df[df["zscore_anomaly"] == 1]).mark_point(
    color="red", size=60, shape="circle"
).encode(
    x="date:T",
    y="daily_active_users:Q",
    tooltip=["date:T", "daily_active_users"]
)

# Prophet Anomalies
prophet_anomaly_layer = alt.Chart(df[df["prophet_anomaly"] == 1]).mark_point(
    color="orange", size=60, shape="diamond"
).encode(
    x="date:T",
    y="daily_active_users:Q",
    tooltip=["date:T", "daily_active_users"]
)

# Combine Layers
chart = base
if "Z-score" in selected_methods:
    chart += z_anomaly_layer
if "Prophet" in selected_methods:
    chart += prophet_anomaly_layer

st.altair_chart(chart.properties(width=800, height=400), use_container_width=True)

# --- Data Table ---
with st.expander("📄 View Raw Data"):
    st.dataframe(df.sort_values("date", ascending=False).reset_index(drop=True))
