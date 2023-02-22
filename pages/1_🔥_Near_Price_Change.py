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
st.set_page_config(page_title='Near Price Change - Insight of the Week',
                   page_icon=':bar_chart:', layout='wide')
st.title('🔥 Near Price Change')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Hourly_Price_change_Rate':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/76a71ec0-290b-4c3f-b4c9-6f4f01303ab5/data/latest')
    elif query == 'Daily_Price_change_Rate':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e017a263-f31f-4d98-a00a-7cd2e2abd89c/data/latest')
    elif query == 'Hourly_MA':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/b568b026-f8a7-42e5-87b5-1bf0f4199836/data/latest')
    elif query == 'Daily_MA':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/be6df498-2b06-42fb-ba8b-6b699047fb7d/data/latest')
    elif query == 'Hourly_VS_Tokens':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/f76adceb-291e-45b5-ba7e-a0b2a9286bef/data/latest')
    elif query == 'Daily_VS_Tokens':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/7338fdfa-b6a8-42f2-b829-e2181142a575/data/latest')
    elif query == 'Price_Change_Comparison_Hourly':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/b54dfa53-a913-40dd-ad5d-4fc65f88f820/data/latest')
    return None


Hourly_Price_change_Rate = get_data('Hourly_Price_change_Rate')
Daily_Price_change_Rate = get_data('Daily_Price_change_Rate')
Hourly_MA = get_data('Hourly_MA')
Daily_MA = get_data('Daily_MA')
Hourly_VS_Tokens = get_data('Hourly_VS_Tokens')
Daily_VS_Tokens = get_data('Daily_VS_Tokens')
Price_Change_Comparison_Hourly = get_data('Price_Change_Comparison_Hourly')

df = Hourly_Price_change_Rate
df2 = Daily_Price_change_Rate
df3 = Hourly_MA
df4 = Daily_MA
df5 = Hourly_VS_Tokens
df6 = Daily_VS_Tokens
df7 = Price_Change_Comparison_Hourly

#########################################################################################

st.write(""" ### Near Price Summary ##  """)

st.write("""
As of Feb 20, 2023, NEAR's current price is 2.67 USD, with a 24-hour trading volume of 237.32M. NEAR is +4.41% in the last 24 hours, with a circulating supply of 860.27M NEAR coins and a maximum supply of 1.00B NEAR coins.  NEAR ranks 33 by market cap.NEAR has an all-time high (ATH) of $20.44 , recorded on Jan 17, 2022. [[6]](https://www.bybit.com/en-US/coin-price/near/)   """)


st.info(""" ##### In This Near Price Change Section you can find: ####

 
* Near Price Correlation with Role Models [ Bitcoin - Ethereum ]
* Near Price Correlation with Rivals [ Matic - Solana - Optimism ]
* Price Change Rate Compare to others 
* Near Standard Moving Averages

""")


#########################################################################################

st.write(""" ## NEAR Price Correlation with Role Models ##  """)

# NEAR vs Bitcoin Price [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df5['DATE'], y=df5["NEAR_PRICE"],
                      name="NEAR PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df5['DATE'], y=df5["BTC_PRICE"],
                      name='Bitcoin Price'), secondary_y=True)
fig.update_layout(
    title_text='NEARvs Bitcoin Price [Hourly]')
fig.update_yaxes(
    title_text=' Hourly NEAR Price', secondary_y=False)
fig.update_yaxes(title_text=' Hourly Bitcoin Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Near vs Bitcoin Price [Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df6['DATE'], y=df6["NEAR_PRICE"],
                      name="NEAR PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df6['DATE'], y=df6["BTC_PRICE"],
                      name='Daily Price'), secondary_y=True)
fig.update_layout(
    title_text='NEAR vs Bitcoin Price [Daily]')
fig.update_yaxes(
    title_text=' Daily NEAR Price', secondary_y=False)
fig.update_yaxes(title_text=' Daily Bitcoin Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# NEAR vs Etheruem Price [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df5['DATE'], y=df5["NEAR_PRICE"],
                      name="NEAR PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df5['DATE'], y=df5["ETH_PRICE"],
                      name='Ethereum Price'), secondary_y=True)
fig.update_layout(
    title_text='NEAR vs Etherum Price [Hourly]')
fig.update_yaxes(
    title_text=' Hourly NEAR Price', secondary_y=False)
fig.update_yaxes(title_text=' Hourly Etherum Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# NEAR vs Etheruem Price [Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df6['DATE'], y=df6["NEAR_PRICE"],
                      name="NEAR PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df6['DATE'], y=df6["ETH_PRICE"],
                      name='Ethereum Price'), secondary_y=True)
fig.update_layout(
    title_text='NEAR vs Etherum Price [Daily]')
fig.update_yaxes(
    title_text=' Daily NEAR Price', secondary_y=False)
fig.update_yaxes(title_text=' Daily Etherum Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ## NEAR Price Correlation with Rivals ##  """)

# NEAR vs MATIC Price [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df5['DATE'], y=df5["NEAR_PRICE"],
                      name="NEAR PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df5['DATE'], y=df5["MATIC_PRICE"],
                      name='Matic Price'), secondary_y=True)
fig.update_layout(
    title_text='NEAR vs MATIC Price [Hourly]')
fig.update_yaxes(
    title_text=' Hourly NEAR Price', secondary_y=False)
fig.update_yaxes(title_text=' Hourly Matic Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# NEAR vs MATIC Price [Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df6['DATE'], y=df6["NEAR_PRICE"],
                      name="NEAR PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df6['DATE'], y=df6["MATIC_PRICE"],
                      name='Matic Price'), secondary_y=True)
fig.update_layout(
    title_text='NEAR vs MATIC Price [Daily]')
fig.update_yaxes(
    title_text=' Daily NEAR Price', secondary_y=False)
fig.update_yaxes(title_text=' Daily Matic Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# NEAR vs OP Price [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df5['DATE'], y=df5["NEAR_PRICE"],
                      name="NEAR PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df5['DATE'], y=df5["OP_PRICE"],
                      name='Optimism Price'), secondary_y=True)
fig.update_layout(
    title_text='NEAR vs Optimism Price [Hourly]')
fig.update_yaxes(
    title_text=' Hourly NEAR Price', secondary_y=False)
fig.update_yaxes(title_text=' Hourly Optimism Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# NEAR vs OP Price [Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df6['DATE'], y=df6["NEAR_PRICE"],
                      name="NEAR PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df6['DATE'], y=df6["OP_PRICE"],
                      name='Optimism Price'), secondary_y=True)
fig.update_layout(
    title_text='NEAR vs Optimism Price [Daily]')
fig.update_yaxes(
    title_text=' Daily NEAR Price', secondary_y=False)
fig.update_yaxes(title_text='Daily Optimism Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# NEAR vs Solana Price [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df5['DATE'], y=df5["NEAR_PRICE"],
                      name="NEAR PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df5['DATE'], y=df5["SOL_PRICE"],
                      name='Solana Price'), secondary_y=True)
fig.update_layout(
    title_text='NEAR vs Solana Price [Hourly]')
fig.update_yaxes(
    title_text=' Hourly NEAR Price', secondary_y=False)
fig.update_yaxes(title_text=' Hourly Solana Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# NEAR vs Solana Price [Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df6['DATE'], y=df6["NEAR_PRICE"],
                      name="NEAR PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df6['DATE'], y=df6["SOL_PRICE"],
                      name='Solana Price'), secondary_y=True)
fig.update_layout(
    title_text='NEAR vs Solana Price [Daily]')
fig.update_yaxes(
    title_text=' Daily NEAR Price', secondary_y=False)
fig.update_yaxes(title_text=' Daily Solana Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


##########################################################################################
st.write(""" ## NEAR Price Change Rate VS Role Models ##  """)

# Hourly Price Change Comprison
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df['DATE'], y=df["NEAR_CHANGE"],
                      name="NEAR CHANGE Rate"), secondary_y=False)
fig.add_trace(go.Line(x=df['DATE'], y=df["BTC_CHANGE"],
                      name="Bitcoin CHANGE Rate"), secondary_y=False)
fig.add_trace(go.Line(x=df['DATE'], y=df["ETH_CHANGE"],
                      name="Etherum CHANGE Rate"), secondary_y=False)
fig.update_layout(
    title_text='Hourly Price Change Rate Comprison')
fig.update_yaxes(
    title_text=' Price Change Rate', secondary_y=False)
fig.update_yaxes(title_text='Price Change Rate', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Price Change Comprison
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df2['DATE'], y=df2["NEAR_CHANGE"],
                      name="NEAR CHANGE Rate"), secondary_y=False)
fig.add_trace(go.Line(x=df2['DATE'], y=df2["BTC_CHANGE"],
                      name="Bitcoin CHANGE Rate"), secondary_y=False)
fig.add_trace(go.Line(x=df2['DATE'], y=df2["ETH_CHANGE"],
                      name="Etherum CHANGE Rate"), secondary_y=False)
fig.update_layout(
    title_text='Daily Price Change Rate Comprison')
fig.update_yaxes(
    title_text=' Price Change Rate', secondary_y=False)
fig.update_yaxes(title_text='Price Change Rate', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ## NEAR Price Change Rate VS Rivals ##  """)

# Hourly Price Change Comprison
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df['DATE'], y=df["NEAR_CHANGE"],
                      name="NEAR CHANGE Rate"), secondary_y=False)
fig.add_trace(go.Line(x=df['DATE'], y=df["SOL_CHANGE"],
                      name="Solana CHANGE Rate"), secondary_y=False)
fig.add_trace(go.Line(x=df['DATE'], y=df["MATIC_CHANGE"],
                      name="MATIC CHANGE Rate"), secondary_y=False)
fig.add_trace(go.Line(x=df['DATE'], y=df["OP_CHANGE"],
                      name="Optimism CHANGE Rate"), secondary_y=False)
fig.update_layout(
    title_text='Hourly Price Change Rate Comprison')
fig.update_yaxes(
    title_text=' Price Change Rate', secondary_y=False)
fig.update_yaxes(title_text='Price Change Rate', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Daily Price Change Comprison
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df2['DATE'], y=df2["NEAR_CHANGE"],
                      name="NEAR CHANGE Rate"), secondary_y=False)
fig.add_trace(go.Line(x=df2['DATE'], y=df2["SOL_CHANGE"],
                      name="Solana CHANGE Rate"), secondary_y=False)
fig.add_trace(go.Line(x=df2['DATE'], y=df2["MATIC_CHANGE"],
                      name="MATIC CHANGE Rate"), secondary_y=False)
fig.add_trace(go.Line(x=df2['DATE'], y=df2["OP_CHANGE"],
                      name="Optimism CHANGE Rate"), secondary_y=False)
fig.update_layout(
    title_text='Daily Price Change Comprison')
fig.update_yaxes(
    title_text=' Price Change Rate', secondary_y=False)
fig.update_yaxes(title_text='Price Change Rate', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

############################################################################

st.write(""" ## Near Price Standard Moving Averages ##  """)

# NEAR Price Moving averages [Hourly]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df3['DATE'], y=df3["NEAR_PRICE"],
                      name="NEAR PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df3['DATE'], y=df3['MA7'],
                      name='Hourly Moving average (MA7))'), secondary_y=True)
fig.add_trace(go.Line(x=df3['DATE'], y=df3['MA26'],
                      name='Hourly Moving average (MA26)'), secondary_y=True)
fig.add_trace(go.Line(x=df3['DATE'], y=df3['MA52'],
                      name='Hourly Moving average (MA52))'), secondary_y=True)
fig.add_trace(go.Line(x=df3['DATE'], y=df3['MA100'],
                      name='Hourly Moving average (MA100)'), secondary_y=True)
fig.add_trace(go.Line(x=df3['DATE'], y=df3['MA200'],
                      name='Hourly Moving average (MA200)'), secondary_y=True)
fig.update_layout(
    title_text='NEAR Price Moving averages [Hourly]')
fig.update_yaxes(
    title_text='Price', secondary_y=False)
fig.update_yaxes(title_text='Moving averages', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# NEAR Price Moving averages [Daily]
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Line(x=df4['DATE'], y=df4["NEAR_PRICE"],
                      name="NEAR PRICE"), secondary_y=False)
fig.add_trace(go.Line(x=df4['DATE'], y=df4['MA7'],
                      name='Hourly Moving average (MA7))'), secondary_y=True)
fig.add_trace(go.Line(x=df4['DATE'], y=df4['MA14'],
                      name='Hourly Moving average (MA14)'), secondary_y=True)
fig.update_layout(
    title_text='NEAR Price Moving averages [Daily]')
fig.update_yaxes(
    title_text='Price', secondary_y=False)
fig.update_yaxes(title_text='Moving averages', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


#############################################################
st.text(" \n")

st.info(""" #### Summary: ####

 * Near Price Corrolate with Ethereum more than Bitcoin Price
 * Among NEAR rivales Optimism showed the most similarity to NEAR Price
 * Matic was not corrolated with NEAR compared to other tokens
 * There were no Token which showed a negative corrolation with Bitcoin or Ethereum


""")
