import streamlit as st
import pandas as pd
import plotly.express as px

st.header('Panel de Control de Anuncios de Venta de Coches')
car_data = pd.read_csv('vehicles_us.csv')
hist_button = st.button('Construir Histograma')
if hist_button:
    st.write('Construyendo histograma...')
    fig = px.histogram(car_data, x="odometer")
    st.plotly_chart(fig, use_container_width=True)
scatter_button = st.button('Construir Gráfico de Dispersión')
if scatter_button:
    st.write('Construyendo gráfico de dispersión...')
    fig = px.scatter(car_data, x="odometer", y="price")
    st.plotly_chart(fig, use_container_width=True)