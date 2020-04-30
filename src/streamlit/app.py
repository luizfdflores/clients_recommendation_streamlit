import streamlit as st
import numpy as np
from PIL import Image

st.markdown("""
<style>
body {
    background-color: #ECBB1A;
    }
</style>
    """, unsafe_allow_html=True)
	

image = Image.open('logo3.png')

st.image(image,	use_column_width=True, format='PNG')

st.subheader('Gostaria de atualizar a base do mercado?')
fl_market = st.checkbox('Sim', value=False, key='market')
if fl_market:
	uploaded_market = st.file_uploader("Choose a CSV file", type="csv", key='market')
	if uploaded_market is not None:
		#data = pd.read_csv(uploaded_file)
		#st.write(data)
		st.write('Arquivo carregado com sucesso!')
		fl_new_market = True
	else:
		st.write('Por favor, carregue um arquivo')
		
st.subheader('Gostaria de carregar um portfolio?')
fl_portfolio = st.checkbox('Sim', value=False, key='portfolio')
if fl_portfolio:
	uploaded_market = st.file_uploader("Choose a CSV file", type="csv", key='portfolio')
	if uploaded_market is not None:
		#data = pd.read_csv(uploaded_file)
		#st.write(data)
		st.write('Arquivo carregado com sucesso!')
		fl_new_market = True
	else:
		st.write('Por favor, carregue um arquivo')
else:
	st.write('Será gerado um portfolio aleatório a partir do mercado.')
	number = st.number_input('Quantidade de empresas no portfolio aleatório', max_value=20000, format='%i', value=0)

# TODO FUNCAO PARA VALIDAR INPUT DO MERCADO
# TODO FUNCAO PARA VALIDAR INPUT DO PORTFOLIO
# TODO FUNCAO PARA GERAR PORTFOLIO ALEATORIO
# TODO MODIFICAR CONFIG PARA SUBIR ARQUIVOS MAIORES QUE 200MB