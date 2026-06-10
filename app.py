import numpy as np
import pandas as pd
import yfinance as yf
import streamlit as st
import matplotlib.pyplot as plt

st.set_page_config(page_title="Stock Market Predictor")

st.header("📈 Stock Market Predictor")

stock = st.text_input("Enter Stock Symbol", "GOOG")

start = "2012-01-01"
end = "2022-12-31"

try:
    data = yf.download(stock, start=start, end=end)

    if data.empty:
        st.error("Invalid Stock Symbol")
        st.stop()

    st.subheader("Stock Data")
    st.write(data)

    # Moving Averages
    ma_50 = data["Close"].rolling(50).mean()
    ma_100 = data["Close"].rolling(100).mean()
    ma_200 = data["Close"].rolling(200).mean()

    # Price vs MA50
    st.subheader("Price vs MA50")

    fig1 = plt.figure(figsize=(10, 5))
    plt.plot(data["Close"], label="Close Price")
    plt.plot(ma_50, label="MA50")
    plt.legend()
    st.pyplot(fig1)

    # Price vs MA50 vs MA100
    st.subheader("Price vs MA50 vs MA100")

    fig2 = plt.figure(figsize=(10, 5))
    plt.plot(data["Close"], label="Close Price")
    plt.plot(ma_50, label="MA50")
    plt.plot(ma_100, label="MA100")
    plt.legend()
    st.pyplot(fig2)

    # Price vs MA100 vs MA200
    st.subheader("Price vs MA100 vs MA200")

    fig3 = plt.figure(figsize=(10, 5))
    plt.plot(data["Close"], label="Close Price")
    plt.plot(ma_100, label="MA100")
    plt.plot(ma_200, label="MA200")
    plt.legend()
    st.pyplot(fig3)

    # Trend Prediction
    st.subheader("Predicted Trend")

    latest_price = float(data["Close"].iloc[-1])
    ma100_latest = float(ma_100.iloc[-1])

    if latest_price > ma100_latest:
        st.success("📈 Stock Trend: UPWARD")
    else:
        st.error("📉 Stock Trend: DOWNWARD")

    st.write("Latest Close Price:", round(latest_price, 2))
    st.write("100 Day Moving Average:", round(ma100_latest, 2))

except Exception as e:
    st.error(f"Error: {e}")

