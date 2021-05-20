import streamlit as st
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re

def extract(ticker):
    url = 'https://finance.yahoo.com/quote/'+ticker+'/profile?p='+ticker
    page = urlopen(url)
    soup = BeautifulSoup(page)
    desc = soup.find('p',attrs={'class':'Mt(15px) Lh(1.6)'}).text
    institutionUrl = 'https://finance.yahoo.com/quote/'+ticker+'/holders?p='+ticker
    intPage=urlopen(institutionUrl)
    soup = BeautifulSoup(intPage)
    inst = soup.find('td',attrs={'class':'Py(10px) Va(m) Fw(600) W(15%)','data-reactid':'30'}).text
    line = re.sub('[%]', '', inst)
    insUrl = 'https://finance.yahoo.com/quote/'+ticker+'/insider-transactions?p='+ticker
    insPage=urlopen(insUrl)
    soup = BeautifulSoup(insPage)
    ins = soup.find('td',attrs={'class':'Py(10px)','data-reactid':'54'}).text
    return(desc,line,ins)

def show_explore_page():
    st.title('Insider and Institutional Buying')

    st.write("Input the stock ticker symbol to get company description \
            along with institutional holdings and insider transactions over \
             the past 6 months.")

    ticker_symbol = st.text_input('Ticker','AAPL')

    action = st.button("Info:")

    if action:
        ans = extract(ticker_symbol)
        st.write(ans[0])
        st.write('Institutional ownership: {}% '.format(ans[1]))
        st.write('% Net Shares Purchased(Sold): ',ans[2])