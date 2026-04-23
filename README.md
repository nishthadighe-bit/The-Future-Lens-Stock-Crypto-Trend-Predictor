📈 Future-Lens: AI Trend Predictor
Time-Series Analysis & Predictive Forecasting
🎯 The Vision
In a world of volatile data, the ability to separate noise from signal is essential. I developed Future-Lens to demonstrate how statistical modeling and machine learning can be applied to financial time-series data. This tool allows users to ingest live market data and visualize potential future trends based on historical performance and mathematical regression.

🚀 The "Out of the Box" Features
Live API Integration: Utilizes yfinance to pull real-time market data for stocks, crypto, and indices globally.

Hybrid Trend Analysis: Combines 20-Day Simple Moving Averages (SMA) for historical smoothing with Linear Regression for future forecasting.

Interactive Forecast Windows: Users can dynamically adjust the prediction horizon (1–30 days) to see how the model's confidence and trajectory shift.

🧠 Technical Deep Dive
The Engine: Powered by Scikit-Learn’s Linear Regression, the model maps date ordinals to closing prices to identify the underlying growth or decay trajectory.

Feature Engineering: Implements rolling window calculations to provide context on short-term volatility versus long-term trends.

Data Pipeline: A streamlined end-to-end pipeline: Data Ingestion -> Feature Transformation -> Model Fitting -> Future Extrapolation -> Visualization.

🛠️ Tech Stack
Python: Core programming and logic.

yfinance: For robust, real-time financial data sourcing.

Scikit-Learn: For predictive trend modeling.

Matplotlib & Streamlit: For creating clear, interactive data narratives and dashboards.
