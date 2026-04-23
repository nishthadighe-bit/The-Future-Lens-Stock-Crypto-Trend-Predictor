import streamlit as st

# --- 1. THE "SAFEGUARD" CHECK ---
try:
    import yfinance as yf
    import pandas as pd
    import numpy as np
    from sklearn.linear_model import LinearRegression
    from PIL import Image
    import datetime
except ImportError:
    st.error("🚀 **Hold on!** You haven't added the `requirements.txt` file to GitHub yet.")
    st.info("Create a file named `requirements.txt` on GitHub and add: `streamlit`, `yfinance`, `pandas`, `numpy`, `scikit-learn`, and `Pillow`.")
    st.stop()

# --- 2. APP CONFIG ---
st.set_page_config(page_title="Nishtha's DS Hub", page_icon="📊")

st.sidebar.title("🛠️ Project Selector")
choice = st.sidebar.radio("Go to:", ["Trend Predictor", "Scholar Bio-Sync"])

# --- PROJECT 1: FUTURE-LENS ---
if choice == "Trend Predictor":
    st.title("📈 Future-Lens Trend Predictor")
    ticker = st.text_input("Enter Ticker (e.g., BTC-USD, RELIANCE.NS)", "BTC-USD")
    
    if st.button("Predict"):
        data = yf.download(ticker, start="2024-01-01", progress=False)
        if not data.empty:
            st.line_chart(data['Close'])
            # Simple Regression
            df = data[['Close']].reset_index()
            df['Ordinal'] = df['Date'].map(datetime.date.toordinal)
            model = LinearRegression().fit(df[['Ordinal']].values, df['Close'].values)
            st.success(f"Model trained! Current Trend: {'📈 Upward' if model.coef_[0] > 0 else '📉 Downward'}")
        else:
            st.error("Ticker not found.")

# --- PROJECT 2: SCHOLAR BIO-SYNC ---
else:
    st.title("🎓 Scholar Bio-Sync")
    st.write("Manage that 9.28 SGPI & Kalyan commute.")
    sleep = st.slider("Sleep", 0, 12, 7)
    commute = st.slider("Commute Stress", 1, 10, 5)
    
    score = (sleep * 10) - (commute * 5) + 20
    st.metric("Focus Potential", f"{max(0, min(100, score))}%")

       
    




        
