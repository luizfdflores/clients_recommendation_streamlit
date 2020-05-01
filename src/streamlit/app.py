import streamlit as st
from PIL import Image
import pandas as pd
import numpy as np
import time

market_data_path = '../../data/raw/estaticos_market.csv'

st.markdown("""
<style>
body {
    background-color: #ECBB1A;
    }
</style>
    """, unsafe_allow_html=True)

image = Image.open('logo3.png')

st.image(image, use_column_width=True, format='PNG')

st.markdown('## **Would you like to upload a new market data?**')
fl_market = st.checkbox('Yes', value=False, key='market')
fl_new_market = None
uploaded_market = None
if fl_market:
    uploaded_market = st.file_uploader("Please, choose a valid market data CSV file", type="csv", key='market')
    if uploaded_market is not None:
        # TODO CHECK IF LOADED MARKET DATA IS VALID
        st.write('File loaded successfully!')
        fl_new_market = True
    else:
        st.write('Please load a valid file')

st.markdown('## **Would you like to upload a portfolio data?**')
fl_portfolio = st.checkbox('Yes', value=False, key='portfolio')
fl_new_portfolio = None
uploaded_portfolio = None
if fl_portfolio:
    uploaded_portfolio = st.file_uploader("Please, choose a valid portfolio data CSV file", type="csv", key='portfolio')
    if uploaded_portfolio is not None:
        # TODO CHECK IF LOADED PORTFOLIO IS VALID
        st.write('File loaded successfully!')
        fl_new_portfolio = True
    else:
        st.write('Please load a valid file')
else:
    st.markdown("### A new random portfolio will be generated from the market data")
    n_companies = st.number_input('How many companies should the new portfolio have?',
                                  max_value=500000, min_value=100, format='%i', value=20000, step=10)

# TODO MODIFICAR CONFIG PARA SUBIR ARQUIVOS MAIORES QUE 200MB

st.subheader('Would you like to run the model? Check the box below!')
fl_run = st.checkbox('Get lead recommendations', value=False, key='recomend')
if fl_run:
    st.write('Running')
    if fl_new_market:
        st.write('Loading new market data...')
        df_new_market = pd.read_csv(uploaded_market)
        # TODO IMPLEMENT SANITIZE FUNCTION
        # df_market = sanitize(df_new_market)
        st.write('Market data loaded successfully!')
    else:
        st.write('Loading saved market data...')
        df_market = pd.read_csv(market_data_path)
        st.write('Market data loaded successfully!')
    if fl_new_portfolio:
        st.write('Loading new portfolio data...')
        data_portfolio = pd.read_csv(uploaded_portfolio)
        st.write('Portfolio data loaded successfully!')
    else:
        st.write('Generating new portfolio data...')
        data_portfolio = pd.DataFrame(np.random.choice(df_market['id'].values, n_companies), columns=['id'])
        st.write('Portfolio data generated successfully!')
# TODO RUN MODEL
# TODO SHOW RESULTS
    latest_iteration = st.empty()
    bar = st.progress(0)

    for i in range(100):
        # Update the progress bar with each iteration.
        latest_iteration.text(f'Iteration {i + 1}')
        bar.progress(i + 1)
        time.sleep(0.1)
