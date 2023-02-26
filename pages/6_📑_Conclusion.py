# Libraries
import streamlit as st
from PIL import Image

# Layout
st.set_page_config(page_title='Insight of the Week',
                   page_icon=':bar_chart:📈', layout='wide')
st.title(' Conclusion 📑 ')

st.write("""

Except for one or two days, the NEAR price exhibited the anticipated positive correlation with Bitcoin and Ethereum prices. For a few days, the NEAR price fluctuated as Bitcoin fought to surpass the 25k barrier. The independence of the NEAR price from other tokens was noticeable for one or two days, but in general, the NEAR price follows the entire market flow and cannot be considered an independent character. In comparison to Bitcoin, Ethereum prices had a stronger correlation with NEAR. There were spikes in the quantity of transactions just before the price rise, and it was not clear which one was the reason for another. Are these transactions changing the demand-supply equilibrium and causing the price to rise, or are users attracted to NEAR because of the price increase?   
The metrics most influenced by NEAR price changes were bridges volume and new users; however, the number of active users was not significantly influenced by price changes.
The activity of the top 20 whales was vague, making it difficult to connect it to trends in recent price changes, but there were some confirmation points that the whales' activity accelerated the price change.
Last but not least, we attempted to track the effect of the Bitcoin price surge on the various characteristics of NEAR Blockchain over a 2-week period, and generalizing these notions is not correct.
It is better to create a completely new bounty for NEAR Blockchain independancy on market events and pivot points over long time periods.
 """)
