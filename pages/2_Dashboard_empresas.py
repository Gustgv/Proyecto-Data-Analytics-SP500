import pandas as pd
import yfinance as yf
from datetime import date, datetime
import streamlit as st
import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title= 'Real-Time Data Dashboard', page_icon= 'Active', layout= 'wide')

# Titulos 
st.title('Dashboard: Apple, Google, Microsoft')
st.markdown('Este dashboard te ayudara a obtener mas informacion sobre tres de las principales empresas que conforman el S&P 500, su movimiento historico, el movimiento del volumen y las variaciones del movimiento del precio.')


# Filtros de datos

col4, col5, col6, col7 = st.columns(4)
with col4:
    start_time = st.date_input('Ingrese fecha de inicio del grafico', datetime.date(2000, 1, 1))
    st.write('Fecha de inicio:', start_time)

with col5:
    end_time = st.date_input('Ingrese fecha de final del grafico', datetime.date(2022, 12, 31))
    st.write('Fecha final:', end_time)

with col6:
    frame = st.radio( "Ingresa marco de tiempo a analizar\n 1d: Intervalos diarios\n 1mo: Intervalos mensuales",  ('1d', '1mo'))

with col7:
    empresa = st.radio(
        "Elija el Activo a analizar",
        ('MSFT', 'AAPL', 'GOOG'))

# Descarga y preparacion del dataset

empresas_data = yf.download(empresa, start_time, end_time, interval= frame)

# Filtramos la fila necesaria

empresas_data = empresas_data[['Adj Close', 'Volume']]

# Agrego la columna de variacion porcentual
empresas_data['var'] = round(empresas_data['Adj Close'].pct_change(), 2)
empresas_data.fillna(0, inplace= True)
empresas_data.reset_index(drop= False, inplace= True)

# Reinicio indices
empresas_data = empresas_data.reset_index(drop= False)

# KPIs
var_mean = empresas_data['var'][empresas_data['var'] > 0].mean()
var_neg = empresas_data['var'][empresas_data['var'] < 0].mean()
var = yf.download(empresa, start= '2000-01-01', end= date.today(), interval= frame)
var['var'] = var['Adj Close'].pct_change()
variacion = round(var.iloc[-1]['var'] * 100, 2)

col1, col2, col3 = st.columns(3)
col1.metric(label = "Precio Actual", value= f"${round(var.iloc[-1]['Adj Close'], 2)}", delta= f'{variacion} %')
col2.metric(label = 'Variacion Positiva Promedio', value= f"{round(var_mean * 100, 2)}%")
col3.metric(label = 'Variacion Negativa Promedio', value= f"{round(var_neg * 100, 2)}%")

# Desarrollo de las graficas del dashboard
fig = make_subplots(rows=2, cols=2, start_cell="top-left", subplot_titles=(f"SP500: Movimiento del precio en marco {frame}", f"Grafica de variacion porcentual en marco {frame}", "Volumen", f'Distribucion de movimientos porcentuales Marco de {frame}'))

fig.add_trace(go.Scatter(x= empresas_data['Date'], y=empresas_data['Adj Close']),
              row=1, col=1)

fig.add_trace(go.Bar(x= empresas_data['Date'], y=empresas_data['var']),
              row=1, col=2)

fig.add_trace(go.Bar(x= empresas_data['Date'], y=empresas_data['Volume']),
              row=2, col=1)

fig.add_trace(go.Histogram (x=empresas_data['var']),
              row=2, col=2)

st.plotly_chart(fig, use_container_width=True)






