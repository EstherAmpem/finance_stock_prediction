import streamlit as st

# List of tickers used for building the model
tickers = ['AAPL', 'GOOGL', 'MSFT', 'AMZN', 'FB']

# Create a dropdown menu for ticker selection
ticker = st.selectbox('Select a stock ticker', tickers)

# Create a date picker for date selection
date = st.date_input('Select a date for prediction')


