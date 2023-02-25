# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Insight of the Week',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' Insight of the Week 🪔')


# Content
c1, c2 = st.columns(2)


with c1:
    st.text(" \n")
    st.text(" \n")
    st.video('https://www.youtube.com/watch?v=lyCohdodgo8')

with c2:
    st.text(" \n")
    st.text(" \n")
    st.image(Image.open('Images/Bitcoin.jpg'))


st.write("""
### What Is NEAR Blockchain ? ###
NEAR Protocol is software that aims to incentivize a network of computers to operate a platform for developers to create and launch decentralized applications.
Central to NEAR Protocol’s design is the concept of sharding, a process that aims to split the network’s infrastructure into several segments in order for computers, also known as nodes, to only have to handle a fraction of the network’s transactions.  
By distributing segments of the blockchain, rather than the complete blockchain across network participants, sharding is expected to create a more efficient way to retrieve network data and scale the platform.  
NEAR operates in a similar manner to other centralized data storage systems like Amazon Web Services (AWS) that serve as the base layer on which applications are built. But rather than being run by a single entity, NEAR is operated and maintained by a distributed network of computers.  
Just as AWS allows developers to deploy code in the cloud without needing to create their own infrastructure, NEAR Protocol facilitates a similar architecture built around a network of computers and its native cryptocurrency, the NEAR token.[[1]](https://www.coindesk.com/learn/what-is-near-protocol-and-how-does-it-work)

### Bitcoin price hits $25K in new 2023 high  ###
Despite macroeconomic headwinds and regulatory crackdowns on crypto, Bitcoin has hit a new high for the year. The price of Bitcoin BTC has reached a new 2023 high of $25,000 after surging over much of January. The last time Bitcoin’s price was around 25,000 was around mid-June, on its way down to between 19,000 and 21,000, where it then hovered for several months, according to data from CoinGecko.  
The price of BTC then took a big dip in November following the FTX crisis, which saw BTC drop to a 2022 low of 15,742 on Nov. 10. Its price began to surge in early January, increasing over 14 consecutive days from Jan. 4-17. That daily green candle streak was its second longest in the cryptocurrency’s 14-year history — having fallen one day short of its 15-day record set in November 2013.[[2]](https://cointelegraph.com/news/bitcoin-price-hits-25k-in-new-2023-high)

### Bitcoin Price Correlation With Cryptocurrencies ###
 Bitcoin movement tends to determine the overall direction of crypto currencies, just as the S&P 500 index tends to determine overall stock market direction.This symbiotic relationship means that the value of different crypto currencies is often tied to Bitcoin. As a result, an crypto currencies value is often measured against the price of Bitcoin, so the price of crypto currencies could go down if Bitcoin goes down, and conversely, the price of crypto currencies could go up if Bitcoin goes up. [[3]](3.https://www.linkedin.com/pulse/relationship-between-bitcoin-altcoins-charles-j-phua/)  
 

""")
c1, c2 = st.columns(2)
with c1:
    st.image(Image.open('Images/Near_Price.jpg'))
with c2:
    st.image(Image.open('Images/BTC_Price.jpg'))

st.write("""
## Methodology ##  

The price of Bitcoin surged sharply during the past 14 days, hitting the 25K resistance line. This abrupt increase had an impact on the entire market as well as this week's sharp increase in the price of the NEAR token.The data above from last week show how NEAR pricing followed Bitcoin's upward trend and increased by more than 21% over the course of the week. As weekly "Insight of the Week" series is being run by the NEAR Foundation, We decided to take steps to investigate if whether increased price has an effect on how NEAR users behave and to identify any additional factors that may be contributing to it. In order to better comprehend the market, we first tracked the NEAR Price during the previous two weeks and compared it to the prices of Bitcoin and Ethereum as well as Matic, Solana, and Optimism, and try to find a correlation between the NEAR Price and other tokens. Then, we examine whether or not this NEAR price rise has an appreciable influence on transactions made on the NEAR blockchain and bridges to NEAR. Finally, we look for patterns that support the price increase by tracking the top 20 whales on NEAR over the course of the previous 14 days' transactions to and from CEX exchanges.In this dashboard, we calculated and labelled transactions using the tables "near.core.fact transactions" and "near.core.fact transactions." We extract hourly NEAR prices using "near.core.fact prices" , and all of the metrics shown on this dashboard were calculated between "2023-02-05" and "2023-02-20."




""")
st.text(" \n")
st.write("""   
#### Sources ####  """)
st.write("""    1.https://www.coindesk.com/learn/what-is-near-protocol-and-how-does-it-work/    
        2.https://cointelegraph.com/news/bitcoin-price-hits-25k-in-new-2023-high    
        3.https://www.linkedin.com/pulse/relationship-between-bitcoin-altcoins-charles-j-phua/  
        4.https://www.youtube.com/watch?v=lyCohdodgo8
              """)
st.text(" \n")
c1, c2 = st.columns(2)
with c2:
    st.info(
        '**Data:  [Flipside Crypto](https://flipsidecrypto.xyz/)**', icon="🧠")
    st.info(
        '**Project Github:  [Insight of The Week](https://github.com/Kaizen-Step/The_Whales_of_Near)**', icon="💻")

with c1:
    st.info(
        '**Project Supervisor:  [MetricsDao](https://metricsdao.notion.site/)**', icon="👨🏻‍💼")
    st.info(
        '**Twitter:  [Ludwig.1989](https://flipsidecrypto.xyz/)**', icon="🕊️")
