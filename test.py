import streamlit as st
import yfinance as yf

# App title
st.write(""" ## Simple Stock Price App that shows NDAQ stock price.""")

try:
    # Define the ticker symbol (removed the space before 'NDAQ')
    tickerSymbol = 'NDAQ'
    
    # Get data on this ticker
    tickerData = yf.Ticker(tickerSymbol)
    
    # Get the historical prices for this ticker
    tickerDf = tickerData.history(period='1d', start='2010-05-31', end='2020-05-31')
    
    # Check if data is available
    if not tickerDf.empty:
        # Plot Close price
        st.line_chart(tickerDf.Close)
        
        # Plot Volume
        st.line_chart(tickerDf.Volume)
    else:
        st.write("No data available for the selected period.")

except Exception as e:
    # Use Streamlit to display the error in the app
    st.error(f"Error fetching data: {e}")
