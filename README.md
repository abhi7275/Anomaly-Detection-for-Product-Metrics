# 📊 Product Engagement Analysis & Anomaly Detection

## 🚀 Project Overview

This project analyzes product engagement data over a two-year period. The dataset includes key performance metrics such as:

- Daily Active Users (DAU)
- Click-Through Rate (CTR)
- Average Session Duration
- Conversion Rate

Anomalies were deliberately injected into the `daily_active_users` metric to simulate outlier behavior. The project implements anomaly detection using both **Z-score** and **Prophet** models and visualizes the results through an interactive **Streamlit dashboard**.

---

## 🧩 Problem Statement

The goal is to build a monitoring system that can:

- Detect anomalies in user engagement (e.g., spikes or drops in DAU).
- Compare the performance of Z-score and Prophet models for anomaly detection.
- Visualize key metrics and detected anomalies via a dashboard.

---

## 📂 Dataset Description

The dataset was synthetically generated with the following columns:

| Column                | Description                                                   |
|-----------------------|---------------------------------------------------------------|
| `date`                | Date of the entry                                             |
| `product_id`          | Product identifier (e.g., `google_product_001`)              |
| `category`            | Product category (e.g., `Search`)                            |
| `daily_active_users`  | Daily active users with trend, seasonality, and noise        |
| `click_through_rate`  | Click-through rate (CTR)                                      |
| `avg_session_duration`| Average session duration in minutes                          |
| `conversion_rate`     | Conversion rate                                               |
| `is_anomaly`          | Anomaly flag (1 = anomaly, 0 = normal)                        |

### 📈 Data Generation Logic

- **Trend**: Linear increase in DAU over two years  
- **Seasonality**: Weekly and yearly patterns  
- **Noise**: Random fluctuations to simulate real-world variability  
- **Anomalies**: Artificial spikes/drops to mimic outliers  

---

## 🔍 Anomaly Detection Methods

### 1. Z-Score Based Detection
- Computes Z-score for DAU
- Flags any point with |Z-score| > 1.5 (or configurable threshold) as anomaly

### 2. Prophet Model
- Time-series forecasting using Facebook Prophet
- Anomalies identified by deviation outside forecast confidence interval

---

## 📊 Analysis & Visualization

### Tools and Libraries Used
- Python
- Pandas & NumPy
- Facebook Prophet
- Streamlit

### Dashboard Features
- Time-series plot of DAU with anomalies
- Metrics: CTR, Avg Session Duration, Conversion Rate
- Toggle views for Z-score vs. Prophet anomalies

---

## 🛠️ Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/product-engagement-anomaly-detection.git
cd product-engagement-anomaly-detection
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Generate the Dataset

```bash
python data_prep.py
```

### 4. Run Anomaly Detection

```bash
python Zscore.py
python fbprophet.py
```

### 5. Launch the Dashboard

```bash
streamlit run app.py
```

---

## 📌 Example Output

**Z-Score Anomalies**  
Anomalies detected based on statistical deviation.

**Prophet Anomalies**  
Anomalies detected by comparing actual values with forecast bounds.

---

## ✅ Conclusion

This project showcases how statistical (Z-score) and machine learning (Prophet) models can be used for anomaly detection in product engagement data. It provides an interactive and comparative way to monitor user behavior over time.

---

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for more details.
