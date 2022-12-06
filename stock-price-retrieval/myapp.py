import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Price App

Shown are the **closing prices** and **volume** of Google stock

""")

tickerSymbol = 'GOOGL'
tickerData = yf.Ticker(tickerSymbol)

tickerDf = tickerData.history(period = '1d', start = '2004-8-19', end = '2022-8-19')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)