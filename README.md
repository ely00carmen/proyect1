# Proyecto de Análisis de Datos de Vehículos

Este proyecto presenta una aplicación web desarrollada con **Streamlit** que permite generar un análisis exploratorio de datos de vehículos. La aplicación utiliza el conjunto de datos de anuncios de vehículos (vehicles_us.csv) y permite generar un **histograma** de la columna "odometer" y un **gráfico de dispersión** entre el odómetro y el precio del vehículo.

## Funcionalidades:
- **Histograma**: Al marcar la casilla de verificación, se construye un histograma basado en la columna "odometer".
- **Gráfico de dispersión**: Al marcar la casilla de verificación, se construye un gráfico de dispersión que muestra la relación entre "odometer" y "price".

## Requisitos:
- **pandas**
- **plotly**
- **streamlit**

## Cómo ejecutar:
1. Clona el repositorio.
2. Crea un entorno virtual y activa el entorno.
3. Instala las dependencias: `pip install -r requirements.txt`.
4. Ejecuta la aplicación: `streamlit run app.py`.
