import pandas as pd
import plotly.express as px
import streamlit as st
import streamlit as st

st.header('App para ver gráficas de coches usados en EE.UU.')

st.write('Esta aplicación permite visualizar gráficas de coches usados en EE.UU.')

car_data = pd.read_csv('vehicles_us.csv') # leer los datos

# Crear casillas de verificación para generar los gráficos
build_histogram = st.checkbox('Construir un histograma')
build_scatter = st.checkbox('Construir un gráfico de dispersión')

hist_button = st.button('Construir histograma') # crear un botón
if hist_button: # al hacer clic en el botón
# escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')
    # crear un histograma
    fig = px.histogram(car_data, x="odometer")
    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)
# Crear un botón para construir un gráfico de dispersión
scatter_button = st.button('Construir gráfico de dispersión')
if scatter_button:  # Cuando se hace clic en el botón para el gráfico de dispersión

    st.write('Creación de un gráfico de dispersión para el conjunto de datos de anuncios de venta de coches')
    
    # Crear un gráfico de dispersión usando Plotly Express
    fig_scatter = px.scatter(car_data, x="odometer", y="price")
    
    # Mostrar el gráfico de dispersión
    st.plotly_chart(fig_scatter, use_container_width=True)