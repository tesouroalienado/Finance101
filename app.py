import datetime
import streamlit as st
import investpy
import pandas as pd
from streamlit_autorefresh import st_autorefresh

# update every 5 mins

st.set_page_config(
    page_title="Real-Time Score Dashboard",
    page_icon="✅",
    layout="wide",
)

df_portfolio = pd.read_csv('portfolio.csv', header=0)

data = []

date_buy = st.date_input('date_buy')
name = st.text_input('Name')
quantity = st.number_input('Quantity', min_value=1, step=1)
isin = st.text_input('isin')

data.append([date_buy, name, quantity, isin])

if st.button('Add to portfolio'):
    pd.DataFrame(data).to_csv('portfolio.csv', mode='a')
    st.write('Added to portfolio')
    st_autorefresh(interval=1000, limit=2, key="dataframerefresh")
else:
    st.write('CLick to add to portfolio')

st.dataframe(df_portfolio)

df = investpy.stocks.get_stock_recent_data(stock='AAPL', country='United States')
print(df)



