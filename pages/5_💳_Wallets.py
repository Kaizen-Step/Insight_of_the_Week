# Libraries
import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import plotly.subplots as sp

# Global Variables
theme_plotly = None  # None or streamlit
week_days = ['Monday', 'Tuesday', 'Wednesday',
             'Thursday', 'Friday', 'Saturday', 'Sunday']

# Layout
st.set_page_config(page_title='Wallet - Insight of the Week',
                   page_icon=':bar_chart:', layout='wide')
st.title('💳 Wallets')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'USers_NEAR':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/b434e42b-2d29-40a1-a498-8b7d6db372a0/data/latest')
    return None


USers_NEAR = get_data('USers_NEAR')

df = USers_NEAR


#########################################################################################

st.write(""" ### Crypto Wallet Concept ##  """)

st.write("""
A crypto wallet (cryptocurrency wallet) is software or hardware that enables users to store and use cryptocurrency.Crypto wallets keep your private keys – the passwords that give you access to your cryptocurrencies – safe and accessible, allowing you to send and receive cryptocurrencies like Bitcoin and Ethereum. They come in many forms, from hardware wallets like Ledger (which looks like a USB stick) to mobile apps like Coinbase Wallet, which makes using crypto as easy as shopping with a credit card online. [[9]](https://www.coinbase.com/learn/crypto-basics/what-is-a-crypto-wallet)  
In this Dashboard each Wallet represent each user who use the wallet, and these two notions used interchangably.   """)


st.info(""" ##### In This Wallet (User) Section you can find: ####


* Near New Wallet 
* Near Active Wallet

""")


#########################################################################################

st.write(""" ## Near New Wallets Recently  ##  """)

# Total Transaction over Time with Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["daily"], y=df["New Users"],
                     name='New Wallet'), secondary_y=False)
fig.add_trace(go.Line(x=df["daily"], y=df["DAILY_CUMULATIVE_NEW_WALLET"],
                      name='CUMULATIVE New Wallets'), secondary_y=True)
fig.update_layout(
    title_text='Near New Wallets with Cumulative Value')
fig.update_yaxes(
    title_text='New Wallets', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE New Wallets', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ## Near New Wallets Recently ##  """)
# Total Transaction over Time with Cumulative Value
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["daily"], y=df["ACTIVE_USER"],
                     name='Active Wallet'), secondary_y=False)
fig.add_trace(go.Line(x=df["daily"], y=df["DAILY_CUMULATIVE_ACTIVE_WALLET"],
                      name='CUMULATIVE Active Wallets'), secondary_y=True)
fig.update_layout(
    title_text='Near Active Wallets with Cumulative Value')
fig.update_yaxes(
    title_text='Active Wallets', secondary_y=False)
fig.update_yaxes(title_text='CUMULATIVE Active Wallets', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#################################################################################################

st.text(" \n")

st.info(""" #### Key Finding: ####

 * New Users also showed positive corrolation with NEAR prices especially on 14 and 15 of February 
 * while Active Useres did not showed any corrolation wiht price and remained relatively stable for the whole period


""")
