Product Engagement Analysis & Anomaly Detection
Project Overview
This project focuses on analyzing product engagement data over a two-year period. The dataset contains various metrics such as Daily Active Users (DAU), Click-Through Rate (CTR), Average Session Duration, and Conversion Rate. Anomalies are intentionally injected into the Daily Active Users metric to simulate outlier behavior, providing a basis for anomaly detection using both Z-score and Prophet models.

Problem Statement
We aim to develop an anomaly detection system for monitoring key engagement metrics of a product over time. The system will:

Identify anomalies in user behavior (e.g., unusual spikes or drops in daily active users).

Use Z-score and Prophet to detect anomalies, comparing their effectiveness in different contexts.

Visualize the anomalies and other key metrics using an interactive dashboard.

Dataset
Data Source
The dataset was synthetically generated for this project. It includes the following features:


Column	Description
date	Date of the entry
product_id	Product identifier (e.g., "google_product_001")
category	Product category (e.g., "Search")
daily_active_users	Daily active users (with trend, seasonality, and noise)
click_through_rate	Click-through rate (CTR)
avg_session_duration	Average session duration (in minutes)
conversion_rate	Conversion rate
is_anomaly	Flag indicating anomaly (1 = anomaly, 0 = normal)
Data Generation
The dataset was created using the following approach:

Trend: A linear increase in daily_active_users over the two-year period.

Seasonality: Weekly and yearly seasonal fluctuations were added to simulate real-world user behavior patterns.

Noise: Random noise was added to simulate unpredictable behavior.

Anomalies: A subset of the daily_active_users values were modified (with large positive or negative changes) to simulate outliers.

Anomaly Detection
Method 1: Z-Score Based Detection
The Z-score is calculated for daily_active_users and any data point with a Z-score above a threshold (typically ±3) is flagged as an anomaly.

Method 2: Prophet Model for Time Series Forecasting
The Prophet model is used for time-series forecasting, and anomalies are identified by comparing actual values against the predicted range (upper and lower bounds of the forecast).

Both methods will be applied to the dataset, and their results will be compared.

Analysis & Visualization
Tools and Libraries
Python for data manipulation and analysis

Pandas for data processing

NumPy for numerical calculations

Prophet for time-series forecasting and anomaly detection

Streamlit for building an interactive dashboard

Dashboard
The final dashboard visualizes the following:

Daily Active Users over time

Click-Through Rate, Average Session Duration, and Conversion Rate

Detected anomalies using both Z-score and Prophet models

Running the Code
Clone the Repository:

git clone https://github.com/your-username/product-engagement-anomaly-detection.git
cd anomaly-detection-for-product-metrics
Install Dependencies: Install the required libraries:
pip install -r requirements.txt
Generate the Dataset: Run the following script to generate the product_engagement_2yrs.csv dataset:

python data_prep.py
Run the Anomaly Detection: Run the anomaly detection script using Z-score and Prophet models:

python Zscore.py
python fbprophet.py
Run the Dashboard: Start the interactive dashboard using Streamlit:

streamlit run app.py
Example Output
Z-score Anomalies
Anomalies detected based on statistical deviation (Z-score above ±1.5).

Prophet Anomalies
Anomalies detected by comparing actual values against the forecasted range.

Conclusion
This project demonstrates the use of statistical and machine learning methods to detect anomalies in product engagement metrics. The comparison between Z-score and Prophet anomaly detection provides valuable insights into their effectiveness in real-world scenarios.

License
This project is licensed under the MIT License - see the LICENSE file for details.