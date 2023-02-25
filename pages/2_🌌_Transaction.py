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
st.set_page_config(page_title='Transactions - Insight of The Week',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('🌌 Transactions')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Transaction_Intervals':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/45b350c2-1a32-40b3-a846-ce57687ea395/data/latest')
    elif query == 'Transactions_VS_Prices':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/5680aacc-d8f1-4182-b9cf-b909fe32c776/data/latest')
    return None


Transaction_Intervals = get_data('Transaction_Intervals')
Transactions_VS_Prices = get_data('Transactions_VS_Prices')


df3 = Transaction_Intervals
df4 = Transactions_VS_Prices

######################################################################################################################


st.write(""" ### Crypto Transaction Concept ##  """)

st.write("""
Cryptocurrency transaction is a transfer of information made between blockchain addresses. These transfers have to be signed with a private key that corresponds to its address. Signed transactions are broadcast to the network of nodes, active computers that follow a specific set of rules to validate transactions and blocks. Valid transactions need to be confirmed by being included in blocks through the process of mining.[[7]](https://www.bitstamp.net/learn/crypto-101/how-do-cryptocurrency-transactions-work/)     

In this section, we looked into whether or not the 21% price increase had a considerable impact on NEAR transactions.

""")


st.info(""" ##### In This Transaction Section you can find: ####

 * Price change Impact on Number of Transaction 
 * Price change Impact on Number of Transaction Fees 
 * Price change Impact on Transaaction Per Seconds (TPS)
 



""")


#####################################################################################
st.text(" \n")
st.text(" \n")
st.write(
    """ ## Price Change Impact on Transaction Activity [Time Intervals] """)

st.write(""" In the hourly and daily charts, it is clear that on February 11, when the NEAR price hit a low of 2.16, the number of transactions dramatically reduced. And on February 14 at 5:00 AM, there was a two-hour hype in the number of transactions, which peaked at 35k hourly transactions just before the price began to rise. This hype did not last the rest of the day, as the total number of transactions on February 14  was 400k, which was even lower than the previous day. It was observed that the hourly number of transactions dramatically increased for a few hours before any abrupt price shift, whether bullish or bearish. The shift in the equilibrium between supply and demand brought on by the increase or decrease in the price of Bitcoin and Ethereum could be the cause of these hypes.

""")
interval = st.radio('**Time Interval**',
                    ['Hourly', 'Daily', 'Weekly'], key='fees_interval', horizontal=True)


if st.session_state.fees_interval == 'Daily':

    # Total Transaction over Time with Cumulative Value
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df3["DAY"], y=df3["TOTAL_TRANSACTIONS_OVER_TIME"],
                         name='Total Transaction'), secondary_y=False)
    fig.add_trace(go.Line(x=df3["DAY"], y=df3["CUMULATIVE_TRANSACTIONS_DAILY"],
                          name='CUMULATIVE Transactions'), secondary_y=True)
    fig.update_layout(
        title_text='Daily Transactions with Cumulative Value')
    fig.update_yaxes(
        title_text='Daily Transaction', secondary_y=False)
    fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Total Fees over Time with Cumulative Value
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df3["DAY"], y=df3["TOTAL_FEES_OVER_TIME"],
                         name='Daily Transaction Fees'), secondary_y=False)
    fig.add_trace(go.Line(x=df3["DAY"], y=df3["CUMULATIVE_FEE_DAILY"],
                          name='CUMULATIVE Fee'), secondary_y=True)
    fig.update_layout(
        title_text='Daily Transaction Fees with Cumulative Value [NEAR]')
    fig.update_yaxes(
        title_text='Total Fee', secondary_y=False)
    fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # TPs over Time
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df3["DAY"], y=df3["TPS_DAILY"],
                         name='TPS'), secondary_y=False)
    fig.update_layout(title_text='Daily Transaction per Second (TPS) ')
    fig.update_yaxes(title_text='TPS', secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

elif st.session_state.fees_interval == 'Weekly':

    # Total Transaction over Time with Cumulative Value
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df3["WEEK"], y=df3["TOTAL_TRANSACTIONS_OVER_TIME"],
                         name='Weekly Transaction'), secondary_y=False)
    fig.add_trace(go.Line(x=df3["WEEK"], y=df3["CUMULATIVE_BLOCK_WEEKLY"],
                          name='CUMULATIVE Transactions'), secondary_y=True)
    fig.update_layout(
        title_text='Weekly Transactions  with Cumulative Value')
    fig.update_yaxes(
        title_text='Weekly Transaction', secondary_y=False)
    fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Total Fees over Time with Cumulative Value
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df3["WEEK"], y=df3["TOTAL_FEES_OVER_TIME"],
                         name='Total Fee'), secondary_y=False)
    fig.add_trace(go.Line(x=df3["WEEK"], y=df3["CUMULATIVE_FEE_WEEKLY"],
                          name='CUMULATIVE Fee'), secondary_y=True)
    fig.update_layout(
        title_text=' Weekly Transaction Fees with Cumulative Value [NEAR]')
    fig.update_yaxes(
        title_text='Weekly Trnasaction Fee', secondary_y=False)
    fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Block Time over Time
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df3["WEEK"], y=df3["AVG_BLOCK_TIME_WEEKLY"],
                         name='Average Block Time'), secondary_y=False)
    fig.update_layout(title_text='AVG BLOCK TIME WEEKLY'.title())
    fig.update_yaxes(title_text='Average Block Time', secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


elif st.session_state.fees_interval == 'Hourly':

    # Total Transaction over Time with Cumulative Value
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df3["HOUR"], y=df3["TOTAL_TRANSACTIONS_OVER_TIME"],
                         name='Total Transaction'), secondary_y=False)
    fig.add_trace(go.Line(x=df3["HOUR"], y=df3["CUMULATIVE_TRANSACTIONS_HOURLY"],
                          name='CUMULATIVE Transactions'), secondary_y=True)
    fig.update_layout(
        title_text='Hourly Transactions Hourly with Cumulative Value')
    fig.update_yaxes(
        title_text='Hourly Transaction', secondary_y=False)
    fig.update_yaxes(title_text='CUMULATIVE Transaction', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # Total Fees over Time with Cumulative Value
    fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
    fig.add_trace(go.Bar(x=df3["HOUR"], y=df3["TOTAL_FEES_OVER_TIME"],
                         name='Total Fee'), secondary_y=False)
    fig.add_trace(go.Line(x=df3["HOUR"], y=df3["CUMULATIVE_BLOCK_HOURLY"],
                          name='CUMULATIVE Fee'), secondary_y=True)
    fig.update_layout(
        title_text='Hourly Transaction Fees with Cumulative Value [NEAR]')
    fig.update_yaxes(
        title_text='Hourly Fee', secondary_y=False)
    fig.update_yaxes(title_text='CUMULATIVE Fee', secondary_y=True)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

    # TPs over Time
    fig = sp.make_subplots(specs=[[{'secondary_y': False}]])
    fig.add_trace(go.Bar(x=df3["HOUR"], y=df3["TPS_HOURLY"],
                         name='TPS'), secondary_y=False)
    fig.update_layout(title_text='Hourly Transaction Per Second (TPS)')
    fig.update_yaxes(title_text='TPS', secondary_y=False)
    st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


###########################################################################
st.write(""" ## Transaction and Transaction Fees Comparison wiht NEAR Price """)

# Total Transaction over Time VS NEAR Price
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df4["DAY"], y=df4["TOTAL_TRANSACTIONS_OVER_TIME"],
                     name='Daily Transaction'), secondary_y=False)
fig.add_trace(go.Line(x=df4["DAY"], y=df4["Near Price"],
                      name="Near Price"), secondary_y=True)
fig.update_layout(
    title_text='Daily Transactions VS NEAR Price')
fig.update_yaxes(
    title_text='Daily Transaction', secondary_y=False)
fig.update_yaxes(title_text="Near Price", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

# Total Transaction over Time VS NEAR Price
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df4["DAY"], y=df4["TOTAL_FEES_OVER_TIME"],
                     name="TOTAL_FEES_OVER_TIME"), secondary_y=False)
fig.add_trace(go.Line(x=df4["DAY"], y=df4["Near Price"],
                      name="Near Price"), secondary_y=True)
fig.update_layout(
    title_text=' Daily Transactions Fees VS NEAR Price')
fig.update_yaxes(
    title_text="Daily Transaction fees", secondary_y=False)
fig.update_yaxes(title_text="Near Price", secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

########################################################################################

st.text(" \n")

st.info(""" #### Summary: ####

 * On February 11 when NEAR price hit the a low of 2.16 the Number of Transactions droped significantly
 * On the other hand the Transaction Fees was relatively high on very same day
 * Hourly Number of Transaction and TPS showed very good signal before NEAR rised on February 13 
 * Before each sudden drop or rise you can see the substantial change in number of Transactions



""")
