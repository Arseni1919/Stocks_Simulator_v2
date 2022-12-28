import streamlit as st
import matplotlib.pyplot as plt
import plotly.express as px
import pandas as pd
import numpy as np
# from alpaca.trading.client import TradingClient
from alpaca.data.historical import StockHistoricalDataClient
from alpaca.data.requests import StockBarsRequest
from alpaca.data.timeframe import TimeFrame
from alpaca.data.live import StockDataStream


API_KEY = st.secrets.alpaca_api_key
SECRET_KEY = st.secrets.alpaca_secret_key


@st.cache(allow_output_mutation=True)
def historical_data():
    client = StockHistoricalDataClient(API_KEY, SECRET_KEY)
    request_params = StockBarsRequest(
        symbol_or_symbols=["SPY"],
        timeframe=TimeFrame.Day,
        start="2022-01-01 00:00:00"
    )
    bars = client.get_stock_bars(request_params)
    return bars.df


st.write('# Stock Analysis')


bars_df = historical_data()
bars_df['index'] = list(range(len(bars_df['open'])))
# index_list = list(range(len(bars_df['open'])))
fig = px.line(
    bars_df,
    # x=index_list,
    x='index',
    y='open'
)
st.plotly_chart(fig, theme=None, use_container_width=True)

rsi_bool = st.sidebar.checkbox('rsi', value=True, disabled=False)
ma_bool = st.sidebar.checkbox('ma', value=False, disabled=False)

if rsi_bool:
    st.write('here RSI graph')

if ma_bool:
    st.write('here MA graph')