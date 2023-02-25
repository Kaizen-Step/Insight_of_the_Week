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
st.set_page_config(page_title='Price -Insight of the Week',
                   page_icon=':bar_chart:📈', layout='wide')
st.title('💸 Near Price VS Whales ')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


# Data Sources
@st.cache()
def get_data(query):
    if query == 'Near_From_CX':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/c3564371-6a84-400c-bfa3-977a0368e01c/data/latest')
    elif query == 'Near_TO_CX':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/4272c321-66da-4f53-8929-e91d99fe70c6/data/latest')
    elif query == 'NEAR_top20_whales_EXcluded':
        return pd.read_json('https://api.flipsidecrypto.com/api/v2/queries/e352c3a7-bd07-45c0-8ef9-4aa30ffe51b3/data/latest')
    return None


Near_From_CX = get_data('Near_From_CX')
Near_TO_CX = get_data('Near_TO_CX')
NEAR_top20_whales_EXcluded = get_data('NEAR_top20_whales_EXcluded')

df = Near_From_CX
df2 = Near_TO_CX
df3 = NEAR_top20_whales_EXcluded

############################################################################################################

st.write(""" ### Whale Impact Concept ##  """)

st.write("""
The community and investors watch crypto whales because they can significantly influence price movements.
Whales can also create price volatility increases, especially when they move a large quantity of cryptocurrency in one transaction. For example, if an owner is trying to sell their bitcoin for fiat currency, the lack of liquidity and large transaction size creates downward pressure on Bitcoin's price because other market participants see the transaction. When whales sell, other investors go on high alert, watching for indicators that whales are "dumping" their holdings. [[10]](https://www.investopedia.com/terms/b/bitcoin-whale.asp#:~:text=A%20crypto%20whale%20is%20a,also%20create%20price%20volatility%20increases.)  

Exchanges and custody wallets were taken out before compiling the top 20 NEAR whales. In light of the most recent price changes, we strive to keep an eye on these top 20 whale activities (last 2 weeks).     """)


st.info(""" ##### In This Price VS Whales Section you can find: ####

* List of top 20 Whales 
* Whale Transfer From CEX Impact on NEAR Price
* Whale Transfer to CEX Impact on NEAR Price


""")


######################################################################################

st.write(""" ## List of top 20 Whales and Exchanges and Custodials Excluded """)

st.write(""" By estimating the amount going in and coming out of each wallet, we were able to identify the top 20 whales of NEAR. We next tried to filter out exchanges and custodials to locate only individual whales. The following tables show the final list as well as the list of exchanges that were skipped:

""")

c1, c2 = st.columns(2)

with c2:
    st.text(" \n")
    st.write("""
    **Wallets ommited from the Top 20 Whales list:**  
    * binancecold3.near    
    * f6bd6ba459446b7b6fca71707779de9473af56f8.lockup.near    
    * nfendowment03.near    
    * proximity-prime.near  
    * nfendowment01.near    
    * nfendowment05.near  
    * linear-protocol.near
    * v2-nearx.stader-labs.near  
    * e-near.near  
    * binance1.near  
    * d391f37d5a889a724170f44b2b1eff818c7e20bd.lockup.near  
    * marketplace.paras.near  
    * bitkubhwallet.near  
    * app.nearcrowd.near  
    * kucoinc.near  
    * token.sweat  
    * bitkubhwallet2.near  
    * multisender.app.near  
    * 0a2fb468f797b1049841328d4dadc868ca1dcab9.lockup.near  
    * nearcoldtree.near  
    * ec838c99348c4b5a8859a3ca9f44eb136bfa9a01.lockup.near  

            """)

with c1:
    st.table(df3)

############################################################################################################
st.write(""" ## Wales Transfer From CEX Vs Near Price """)

st.write("""  The top 20 whales made a massive number of transactions on the CX exchange on February 8, but the volume did not confirm. Although the number of from CEX exchanges on February 9 was lower than the previous day, the volume of these transfers was three times higher than on February 8, and as expected, on February 11 and 12, the volume of transfers dropped significantly. The top 20 whales' behaviour over the course of these two weeks was often difficult to comprehend, and we were unable to identify any consistent pattern in their behaviour. """)

# Transfer from CEX Vs Near Price
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["AMOUNT"],
                     name='Transfer From CEX Volume'), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["PRICE"],
                      name='Near Price'), secondary_y=True)
fig.update_layout(
    title_text='Transfer From CEX Volume Vs Near Price')
fig.update_yaxes(
    title_text='Volume [Near]', secondary_y=False)
fig.update_yaxes(title_text='Near Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Transfer from CEX Vs Near Price
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df["DATE"], y=df["number of transactions"],
                     name='Transfer From CEX Num TX'), secondary_y=False)
fig.add_trace(go.Line(x=df["DATE"], y=df["PRICE"],
                      name='Near Price'), secondary_y=True)
fig.update_layout(
    title_text='Transfer From CEX Number of Transaction Vs Near Price')
fig.update_yaxes(
    title_text='Number of Transaction', secondary_y=False)
fig.update_yaxes(title_text='Near Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


st.write(""" ## Whales Transfer To CEX Vs Near Price """)

# Transfer To CEX Vs Near Price
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["DATE"], y=df["AMOUNT"],
                     name='Transfer From CEX Volume'), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["PRICE"],
                      name='Near Price'), secondary_y=True)
fig.update_layout(
    title_text='Transfer To CEX Volume Vs Near Price')
fig.update_yaxes(
    title_text='Volume [Near]', secondary_y=False)
fig.update_yaxes(title_text='Near Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)


# Transfer To CEX Vs Near Price
fig = sp.make_subplots(specs=[[{'secondary_y': True}]])
fig.add_trace(go.Bar(x=df2["DATE"], y=df2["number of transactions"],
                     name='Transfer From CEX Num TX'), secondary_y=False)
fig.add_trace(go.Line(x=df2["DATE"], y=df2["PRICE"],
                      name='Near Price'), secondary_y=True)
fig.update_layout(
    title_text='Transfer To CEX Number of Transaction Vs Near Price')
fig.update_yaxes(
    title_text='Number of Transaction', secondary_y=False)
fig.update_yaxes(title_text='Near Price', secondary_y=True)
st.plotly_chart(fig, use_container_width=True, theme=theme_plotly)

########################################################################
st.text(" \n")

st.info(""" #### Summary: ####

 * Top 20 Whales had a huge impact on NEAR price fall in April and September of 2022
 * Each time whales transfer a significant amount of NEAR from exchanges, it was likely to transfer it back in only a couple of days  
 * NEAR price experienced the rise from the start of 2023, and whales confirm this increase
""")
