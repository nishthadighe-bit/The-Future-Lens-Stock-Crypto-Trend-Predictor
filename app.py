import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import datetime

# 1. Page Config
st.set_page_config(page_title="Future-Lens AI", page_icon="📈")

st.title("📈 Future-Lens: Trend Predictor")
st.write("### AI-Powered Market & Trend Analysis")

# 2. Sidebar Inputs
st.sidebar.header("Target Parameters")
ticker = st.sidebar.text_input("Enter Ticker (e.g., BTC-USD, GOOGL, TSLA)", "BTC-USD")
days_to_predict = st.sidebar.slider("Days to Forecast", 1, 30, 7)

# 3. Fetch Data
try:
    data = yf.download(ticker, start="2023-01-01", end=datetime.date.today().strftime('%Y-%m-%d'))
    
    if not data.empty:
        st.subheader(f"Analysis for {ticker}")
        
        # Calculate Moving Average
        data['MA20'] = data['Close'].rolling(window=20).mean()
        
        # --- ML PREDICTION LOGIC ---
        # Prepare data for Linear Regression
        df = data[['Close']].reset_index()
        df['Date_Ordinal'] = df['Date'].map(datetime.date.toordinal)
        
        X = df[['Date_Ordinal']].values
        y = df['Close'].values
        
        model = LinearRegression()
        model.fit(X, y)
        
        # Predict the future
        last_date = df['Date_Ordinal'].max()
        future_dates = np.array([last_date + i for i in range(1, days_to_predict + 1)]).reshape(-1, 1)
        future_preds = model.predict(future_dates)
        
        # 4. Visuals
        st.line_chart(data[['Close', 'MA20']])
        
        st.success(f"Predicted Price in {days_to_predict} days: **${future_preds[-1]:.2f}**")
        
        # Impact Metrics
        col1, col2 = st.columns(2)
        col1.metric("Current Price", f"${y[-1]:.2f}")
        trend = "UP" if future_preds[-1] > y[-1] else "DOWN"
        col2.metric("Forecasted Trend", trend, delta=f"{future_preds[-1] - y[-1]:.2f}")
        
    else:
        st.error("Invalid Ticker or No Data Found.")

except Exception as e:
    st.error(f"System Error: {e}")

st.markdown("---")
st.caption("A Predictive Analytics Tool | Built by Nishtha Dighe")
