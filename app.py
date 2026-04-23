import streamlit as st
import yfinance as yf
import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
import datetime

# --- PAGE CONFIG ---
st.set_page_config(page_title="Nishtha's DS Portfolio", page_icon="📊", layout="wide")

# --- SIDEBAR NAVIGATION ---
st.sidebar.title("🚀 Project Hub")
app_mode = st.sidebar.selectbox("Choose a Project:", 
                                ["Future-Lens (Trend Predictor)", "Scholar Bio-Sync (Performance)"])

# --- PROJECT 1: FUTURE-LENS ---
if app_mode == "Future-Lens (Trend Predictor)":
    st.title("📈 Future-Lens: AI Trend Predictor")
    st.write("### Real-time Market Analysis")
    
    ticker = st.text_input("Enter Ticker (e.g., BTC-USD, GOOGL, RELIANCE.NS)", "BTC-USD")
    days = st.slider("Forecast Days", 1, 30, 7)

    if st.button("Analyze Trend"):
        try:
            data = yf.download(ticker, start="2024-01-01", progress=False)
            if not data.empty:
                # Prediction Logic
                df = data[['Close']].reset_index()
                df['Date_Ordinal'] = df['Date'].map(datetime.date.toordinal)
                X = df[['Date_Ordinal']].values
                y = df['Close'].values
                
                model = LinearRegression().fit(X, y)
                last_date = df['Date_Ordinal'].max()
                future_dates = np.array([last_date + i for i in range(1, days + 1)]).reshape(-1, 1)
                preds = model.predict(future_dates)

                # Visuals
                st.line_chart(data['Close'])
                
                c1, c2 = st.columns(2)
                c1.metric("Current Price", f"${y[-1]:.2f}")
                c2.metric("Predicted Price", f"${preds[-1]:.2f}", 
                          delta=f"{preds[-1]-y[-1]:.2f}")
            else:
                st.error("Invalid Ticker.")
        except Exception as e:
            st.error(f"Error: {e}")

# --- PROJECT 2: SCHOLAR BIO-SYNC ---
elif app_mode == "Scholar Bio-Sync (Performance)":
    st.title("🎓 Scholar Bio-Sync")
    st.write("### Optimization for the 9.28 SGPI Hustle")
    
    col1, col2 = st.columns(2)
    with col1:
        sleep = st.slider("Sleep Hours", 0.0, 12.0, 6.0)
        commute = st.slider("Commute Fatigue (1-10)", 1, 10, 5)
    with col2:
        load = st.number_input("Assignments Pending", 0, 10, 2)
    
    if st.button("Predict Focus"):
        score = int(np.clip((sleep * 10) - (commute * 4) - (load * 5) + 30, 0, 100))
        st.metric("Focus Capacity", f"{score}%")
        st.progress(score / 100)
        
        if score > 70:
            st.success("🔥 High performance mode! Focus on ML assignments.")
        else:
            st.warning("😴 High burnout risk. Rest for the Kalyan commute.")

st.sidebar.markdown("---")
st.sidebar.info("Built by Nishtha Dighe | 2nd Year Data Science")

        
