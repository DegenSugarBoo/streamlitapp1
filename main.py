import streamlit as st 
 


from pandas_datareader import data as pdr
import pandas as pd

import yfinance as yf
yf.pdr_override()
nifty_50=['ADANIPORTS',
'ADANIENT',
'M&M',
'EICHERMOT',
'POWERGRID',
'BAJAJ-AUTO',
'BAJAJFINSV',
'BHARTIARTL',
'HEROMOTOCO',
'NESTLEIND',
'BRITANNIA',
'DRREDDY',
'HDFCLIFE',
'HDFC','HINDUNILVR',
'MARUTI',
'TITAN','ITC',
'RELIANCE',
'BAJFINANCE',
'AXISBANK',
'APOLLOHOSP',
'COALINDIA',
'ULTRACEMCO',
'KOTAKBANK',
'NTPC',
'SBILIFE',
'ASIANPAINT',
'CIPLA',
'TATACONSUM',
'HINDALCO',
'DIVISLAB',
'TATASTEEL',
'TECHM',
'JSWSTEEL',
'ICICIBANK',
'LT',
'HDFCBANK',
'GRASIM',
'SBIN',
'HCLTECH',
'WIPRO',
'BPCL',
'UPL',
'INDUSINDBK',
'SUNPHARMA',
'INFY',
'TATAMOTORS',
'ONGC',
'TCS']
dropdown=st.selectbox("Pick your Asset",nifty_50)
ab=dropdown
dropdown=dropdown+".NS"

start_date=st.date_input("Start",value=pd.to_datetime('2022-01-01'))
end_date=st.date_input("End",value=pd.to_datetime('today'))

if len(dropdown)>0 :
    df= pdr.get_data_yahoo(dropdown, start=start_date, end=end_date)
    
st.sidebar.subheader('Settings')
st.sidebar.caption('Adjust charts settings and then press apply')

with st.sidebar.form('settings_form'):
    show_nontrading_days = st.checkbox('Show non-trading days', True)
    
    chart_styles = [
        'default', 'binance', 'blueskies', 'brasil', 
        'charles', 'checkers', 'classic', 'yahoo',
        'mike', 'nightclouds', 'sas', 'starsandstripes'
    ]
    chart_style = st.selectbox('Chart style', options=chart_styles, index=chart_styles.index('yahoo'))
    chart_types = [
        'candle', 'ohlc', 'line', 'renko', 'pnf'
    ]
    chart_type = st.selectbox('Chart type', options=chart_types, index=chart_types.index('candle'))

    mav1 = st.number_input('Mav 1', min_value=3, max_value=300, value=3, step=1)
    mav2 = st.number_input('Mav 2', min_value=3, max_value=300, value=6, step=1)
    mav3 = st.number_input('Mav 3', min_value=3, max_value=300, value=9, step=1)

    st.form_submit_button('Apply')
import mplfinance as mpf 
fig, ax = mpf.plot(
        df,
        title=f'{ab} Chart',
        type=chart_type,
        show_nontrading=show_nontrading_days,
        mav=(int(mav1),int(mav2),int(mav3)),
        volume=True,

        style=chart_style,
        figsize=(15,10),
        
       
        returnfig=True
    )    
st.pyplot(fig)
