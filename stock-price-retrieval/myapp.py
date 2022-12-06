import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the **closing prices** and **volume** of the entered stock

""")


tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)

st.sidebar.header("Stock Selection")
tickerSymbol = st.sidebar.text_input("Enter your ticker below")
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d', start = '2004-8-19', end = '2022-8-19')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)