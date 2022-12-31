import streamlit as st
from PIL import Image
import pandas as pd
import base64
import matplotlib.pyplot as plt
from bs4 import BeautifulSoup
import requests
import json
import time

# Page layout
## Page expands to full width
st.set_page_config(layout="wide")

# Title
image = Image.open('crypto-logo.jpg')
st.image(image, width=500)

st.title('Crypto Price App')
st.markdown("""
This app retrieves cryptocurrency prices for the top 100 cryptocurrency from the **CoinMarketCap**!
""")

# About
expander_bar = st.expander("About")
expander_bar.markdown("""
* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn, BeautifulSoup, requests, json, time
* **Data source:** [CoinMarketCap](http://coinmarketcap.com).
* **Credit:** Web scraper adapted from the Medium article *[Web Scraping Crypto Prices With Python](https://towardsdatascience.com/web-scraping-crypto-prices-with-python-41072ea5b5bf)* written by [Bryan Feng](https://medium.com/@bryanf).
""")

# Page layout (continued)
## Divide page to 3 columns (col1 = sidebar, col2 and col3 = page contents)
col1 = st.sidebar
col2, col3 = st.columns((2, 1))

# Sidebar + Main panel
col1.header('Input Options')

## Sidebar - Currency price unit
currency_price_unit = col1.selectbox('Select currency for price', ('USD', 'BTC', 'ETH'))

# Web scraping of CoinMarketCap data
# @st.cache
def load_data():
    cmc = requests.get("https://coinmarketcap.com")
    soup = BeautifulSoup(cmc.content, "html.parser")

    data = soup.find("script", id="__NEXT_DATA__", type="application/json")
    coins = {}
    coin_data = json.loads(data.contents[0])
    # listings = coin_data["props"]["initialState"]["cryptocurrency"]["listingLatest"]["data"]
    listings = coin_data["props"]["initialState"]
    listings
    # for i in listings:
    #   coins[str(i['id'])] = i['slug']

load_data()
