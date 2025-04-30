import streamlit as st
import pandas as pd
import plotly.express as px

# --- Load Data ---
@st.cache_data
def load_data():
    # Assumes CSV has both zscore_anomaly and prophet_anomaly
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

# --- Time Series Plot ---
st.subheader("📈 Daily Active Users with Z-score and Prophet Anomalies")

fig = px.line(df, x="date", y="daily_active_users", title="Daily Active Users")

# Add Z-score anomalies
if "Z-score" in selected_methods:
    z_anomalies = df[df["zscore_anomaly"] == 1]
    fig.add_scatter(
        x=z_anomalies["date"], y=z_anomalies["daily_active_users"],
        mode='markers', name='Z-score Anomaly',
        marker=dict(color='red', size=7)
    )

# Add Prophet anomalies
if "Prophet" in selected_methods:
    p_anomalies = df[df["prophet_anomaly"] == 1]
    fig.add_scatter(
        x=p_anomalies["date"], y=p_anomalies["daily_active_users"],
        mode='markers', name='Prophet Anomaly',
        marker=dict(color='orange', size=7, symbol="diamond")
    )

st.plotly_chart(fig, use_container_width=True)

# --- Data Table ---
with st.expander("📄 View Raw Data"):
    st.dataframe(df.sort_values("date", ascending=False).reset_index(drop=True))
