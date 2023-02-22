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
st.set_page_config(page_title='Aknowledgement - Insight of the Week',
                   page_icon=':bar_chart:', layout='wide')
st.title('🪔 Refrences')

# Style
with open('style.css')as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Aknowledgement
st.write(""" ##     Aknowledgement 
We are grateful to all who helped us develop this project specially [**Mr. Ali Taslimi**](https://twitter.com/AliTslm) with comprehensive streamlit open source project [Cross chain Monitoring](https://github.com/alitslm/cross_chain_monitoring) that provides streamlit functions and tools and 0xHaM☰d Near Mega Dashboard top20 users query that helped us a lot.
And also ****Flipside Crypto**** with massive database and last but not least ****MetricsDao**** that is the reason behind this project.
""")


# SQL Codes
st.write(""" ## SQL Codes ## """)

st.write("""
At the following links, you can find the SQL codes that are used in this dashboard: 

""")


c1, c2 = st.columns(2)

with c1:
    st.write("""
    1. [New & Active Users](https://flipsidecrypto.xyz/edit/queries/b434e42b-2d29-40a1-a498-8b7d6db372a0/visualizations/8dbf51ef-68f5-44da-ae25-ada6f1dc67e5)  
    2. [Bridge to Near Weekly](https://flipsidecrypto.xyz/edit/queries/8faad4ca-bbec-4652-a879-fb04f062a58c/visualizations/d21ab5b3-14d7-44a7-91ad-f683f7874a1f)  
    3. [Bridge to Near Daily](https://flipsidecrypto.xyz/edit/queries/f8ea8ebc-997b-4884-afcf-664a4c80fce6/visualizations/b2a85682-4a82-4521-9deb-180c02b909d0)  
    4. [Transaction Vs Price ](https://flipsidecrypto.xyz/edit/queries/5680aacc-d8f1-4182-b9cf-b909fe32c776/visualizations/c58291a9-51f2-4ccb-abfe-dc879aee0b83)  
    5. [Transaction and Fees (Hour-Day_Weekly) ](https://flipsidecrypto.xyz/edit/queries/45b350c2-1a32-40b3-a846-ce57687ea395/visualizations/c9b3fcd6-db9e-4d0e-b58e-2ac36b90071d)  
    6. [Price Daily Vs Tokens](https://flipsidecrypto.xyz/edit/queries/7338fdfa-b6a8-42f2-b829-e2181142a575)  
    7. [The Whale Impact prices CEX to](https://flipsidecrypto.xyz/edit/queries/f76adceb-291e-45b5-ba7e-a0b2a9286bef/visualizations/45d83e16-de7c-4e43-88aa-9be9188475ca)  

    """)

with c2:

    st.write("""
    
   
    8. [Transaction Type in each wallet](https://flipsidecrypto.xyz/edit/queries/a89edfff-1085-4954-a859-6f2abd0b639f/visualizations/79de6764-7c8f-4d00-86ed-d9fe4b159a8f)  
    9. [Price Daily Moving Averages](https://flipsidecrypto.xyz/edit/queries/be6df498-2b06-42fb-ba8b-6b699047fb7d/visualizations/ad1211ac-c9ab-40ad-9a84-bb721df3a139)  
    10. [Price Hourly Moving averages](https://flipsidecrypto.xyz/edit/queries/b568b026-f8a7-42e5-87b5-1bf0f4199836/visualizations/b974a947-a641-4d8d-95c1-b36262026e87)  
    11. [Price Daily Change Rate Vs Tokens](https://flipsidecrypto.xyz/edit/queries/e017a263-f31f-4d98-a00a-7cd2e2abd89c)  
    12. [Price Hourly Change Rate VS Tokens](https://flipsidecrypto.xyz/edit/queries/76a71ec0-290b-4c3f-b4c9-6f4f01303ab5/visualizations/2b87e9e2-28d4-4d52-a0e6-5b3ae20845e2)    
    13. [Whale Impact CEX from](https://flipsidecrypto.xyz/edit/queries/c3564371-6a84-400c-bfa3-977a0368e01c)  
    14. [The Whale Impact prices CEX to](https://flipsidecrypto.xyz/edit/queries/4272c321-66da-4f53-8929-e91d99fe70c6)  
    """)


# Sources
st.write(""" ## Sources ## """)

st.write("""
1.https://www.coindesk.com/learn/what-is-near-protocol-and-how-does-it-work/      
        2.https://cointelegraph.com/news/bitcoin-price-hits-25k-in-new-2023-high      
        3.https://www.linkedin.com/pulse/relationship-between-bitcoin-altcoins-charles-j-phua/    
        4.https://www.youtube.com/watch?v=lyCohdodgo8     
        5.https://www.coindesk.com/tech/2023/02/08/bitcoin-nfts-explode-in-popularity-as-bitmex-research-shows-13000-ordinals/    
        6.https://www.bybit.com/en-US/coin-price/near/)        
        7.https://www.bitstamp.net/learn/crypto-101/how-do-cryptocurrency-transactions-work/  
        8.https://www.coindesk.com/learn/what-are-blockchain-bridges-and-how-do-they-work/  
        9.https://www.coinbase.com/learn/crypto-basics/what-is-a-crypto-wallet  
        10.https://www.investopedia.com/terms/b/bitcoin-whale.asp#:~:text=A%20crypto%20whale%20is%20a,also%20create%20price%20volatility%20increases.   

""")
