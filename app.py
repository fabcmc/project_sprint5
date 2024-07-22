import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv') # lendo os dados

st.header('Dashboard - Sprint 5')
hist_button = st.button('Criar histograma') # criar botão de histograma
scat_button = st.button('Criar dispersão') # criar botão de gráfico de dispersão

if hist_button: # se o botão de histograma for clicado
    # escrever uma mensagem
    st.write('Criando um histograma para o conjunto de dados de anúncios de vendas de carros')
    
    # criar um histograma
    fig = px.histogram(car_data, x="odometer")

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig, use_container_width=True)

if scat_button: # se botão de gráfico de dispersão for clicado
    # escrever uma mensagem
    st.write('Criando um gráfico de dispersão para relação entre odômetro e preço')

    # criar dispersão
    fig = px.scatter(car_data, x="odometer", y="price") # criar um gráfico de dispersão

    # exibir um gráfico Plotly interativo
    st.plotly_chart(fig)
