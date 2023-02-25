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
st.set_page_config(page_title='Bridge - Insight of the Week',
                   page_icon=':bar_chart:', layout='wide')
st.title('🌉 Bridge')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Daily_Bridge_NEAR':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/f8ea8ebc-997b-4884-afcf-664a4c80fce6/data/latest')
    elif query == 'Weekly_Bridge_NEAR':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/8faad4ca-bbec-4652-a879-fb04f062a58c/data/latest')
    return None


Daily_Bridge_NEAR = get_data('Daily_Bridge_NEAR')
Weekly_Bridge_NEAR = get_data('Weekly_Bridge_NEAR')


df = Daily_Bridge_NEAR
df2 = Weekly_Bridge_NEAR


#################################################################################################
st.write(""" ### Bridge Concept ##  """)

st.write("""
A blockchain bridge is a tool that lets you port assets from one blockchain to another, solving one of the main pain points within blockchains – a lack of interoperability.
Since blockchain assets are often not compatible with one another, bridges create synthetic derivatives that represent an asset from another blockchain.Some bridges, known as unidirectional or one-way bridges, allow you to port assets only to the target blockchain and not the other way around.Other bridges like Wormhole and Multichain are bidirectional, or two-way, meaning you can freely convert assets to and from blockchains. [[8]](https://www.coindesk.com/learn/what-are-blockchain-bridges-and-how-do-they-work/)   
  
Here, we investigated if the price increase would be sufficient to persuade people to bridge to NEAR Blockchain.
  """)


st.info(""" ##### In This Bridge Section you can find: ####

* Rainbow Bridge to NEAR Number of Transactions
* Rainbow Bridge Volume
* Rainbow Bridge Number of Users



""")


#################################################################################################
st.write(""" ## Rainbow Bridge to NEAR Number of Transactions """)

st.write(""" On February 11, which was previously discussed as the day the NEAR price hit its monthly low, there was no bridge transaction. Moreover, February 12 came in second-to-last, while February 15—the day with the most bridge transactions to NEAR—saw a notable increase in the price of NEAR. 53% of these transaction was from USDC follow by USDT with 17% . As you can see, the number of bridge transactions on February 18 was the same as February 8 and 6, and the number of bridge transactions on the first week of the period when NEAR experienced a significant fall was not lower than February 16, which was the day after NEAR increased. As a result, this increase did not significantly alter the rhythm other than for one or two hype days.
""")
# Daily Bridge Transactions
fig = px.bar(df.sort_values(["DATE", "NUMBER_TRANSACTIONS"], ascending=[
    True, False]), x="DATE", y="NUMBER_TRANSACTIONS", color="SYMBOL", title='Daily Number of Bridge transactions from Ethereum to NEAR by Token')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


c1, c2 = st.columns(2)
with c1:
    # Weekly Bridge Transactions
    fig = px.bar(df2.sort_values(["DATE", "USD_VOLUME"], ascending=[
        True, False]), x="DATE", y="NUMBER_TRANSACTIONS", color="SYMBOL", title='Weekly Number of Bridge transactions from Ethereum to NEAR by Token')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Transaction')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    # Proportion of Volume Bridged From Ethereum to NEAR by Token
    fig = px.pie(df, values="NUMBER_TRANSACTIONS",
                 names="SYMBOL", title='Proportion of Number of Bridged From Ethereum to NEAR by Token', hole=0.4)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ## Rainbow Bridge to NEAR Volume [USD] """)
st.write(""" Although the NEAR price had little impact on the number of bridge transactions, the volume of bridge transactions was directly influenced, as the February 12 bridge volume was less than 2k, while February 15 bridge volume hit a record of half milion USD. Also, USDC ranked first in volume of bridges with 1.5 million (more than 85% of total bridges).
""")
# Daily Bridge Transactions
fig = px.bar(df.sort_values(["DATE", "USD_VOLUME"], ascending=[
    True, False]), x="DATE", y="USD_VOLUME", color="SYMBOL", title='Daily Volume (USD) of Bridge Transactions from Ethereum to NEAR by Token')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
with c1:
    # Weekly Bridge Transactions
    fig = px.bar(df2.sort_values(["DATE", "USD_VOLUME"], ascending=[
        True, False]), x="DATE", y="USD_VOLUME", color="SYMBOL", title='Weekly Volume (USD) of Bridge Transactions from Ethereum to NEAR by Token')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Transaction')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    # Proportion of Volume Bridged From Ethereum to NEAR by Token
    fig = px.pie(df, values="USD_VOLUME",
                 names="SYMBOL", title='Proportion of Volume Bridged From Ethereum to NEAR by Token', hole=0.4)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ## Rainbow Bridge to NEAR Number of Users """)
st.write(""" The number of users who bridge Ethereum to NEAR was also affected by the NEAR price, but this effect was not massive as far as volume; as you can see, the number of users even dropped after the NEAR rise and mostly showed a sinusoidal pattern.
""")
# Daily Bridge Transactions
fig = px.bar(df.sort_values(["DATE", "UNIQUE_WALLETS_FROM"], ascending=[
    True, False]), x="DATE", y="UNIQUE_WALLETS_FROM", color="SYMBOL", title='Daily Users of Bridge from Ethereum to NEAR by Token')
fig.update_layout(legend_title=None, xaxis_title=None,
                  yaxis_title='Daily Transaction')
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

c1, c2 = st.columns(2)
with c1:
    # Weekly Bridge Transactions
    fig = px.bar(df2.sort_values(["DATE", "UNIQUE_WALLETS_FROM"], ascending=[
        True, False]), x="DATE", y="UNIQUE_WALLETS_FROM", color="SYMBOL", title='Weekly Users of Bridge from Ethereum to NEAR by Token')
    fig.update_layout(legend_title=None, xaxis_title=None,
                      yaxis_title='Weekly Transaction')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)
with c2:
    # Proportion of Volume Bridged From Ethereum to NEAR by Token
    fig = px.pie(df, values="UNIQUE_WALLETS_FROM",
                 names="SYMBOL", title='Proportion of Users Bridged From Ethereum to NEAR by Token', hole=0.4)
    fig.update_layout(legend_title=None, legend_y=0.5)
    fig.update_traces(textinfo='percent+value', textposition='inside')
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##########################################################################

st.text(" \n")

st.info(""" #### Summary: ####

 * USDC was the top token bridged to NEAR with more than 50% of total Number of Bridges
 * USDT and WOO followed USDC wiht a Significant difference  
 * There was no Bridge transaction on 11 Feb which was the day that NEAR exprienced the whole period low
 * The Number of Bridge to NEAR significantly increased when NEAR prices rised



""")
