import pandas as pd
import yfinance as yf
from datetime import date, datetime
import streamlit as st
import datetime
import plotly.graph_objects as go
from plotly.subplots import make_subplots

st.set_page_config(page_title= 'Real-Time Data Dashboard', page_icon= 'Active', layout= 'wide')

# Titulos 
st.title('S&P 500 Dashboard')
st.markdown('Este dashboard te ayudara a obtener mas informacion sobre el S&P 500, su movimiento historico, el movimiento del volumen y las variaciones del movimiento del precio.')


# Filtros de datos

col4, col5, col6 = st.columns(3)
with col4:
    start_time = st.date_input('Ingrese fecha de inicio del grafico', datetime.date(2000, 1, 1))
    st.write('Fecha de inicio:', start_time)

with col5:
    end_time = st.date_input('Ingrese fecha de final del grafico', datetime.date(2022, 12, 31))
    st.write('Fecha final:', end_time)

with col6:
    frame = st.radio( "Ingresa marco de tiempo a analizar\n 1d: Intervalos diarios\n 1mo: Intervalos mensuales",  ('1d', '1mo'))

# Descarga y preparacion del dataset
sp_data = yf.download('^GSPC', start_time, end_time, interval= frame)

# Ahora calculare el rendimiento mensual del activo agregando columna de performance por share.
sp_data['share_perfomance'] = sp_data['Adj Close'].pct_change()

# Agregamos las medias moviles
sp_data['MA50'] = sp_data['Adj Close'].rolling(50).mean()

# Reinicio indices
sp_data = sp_data.reset_index(drop= False)

# KPIs
var = yf.download('^GSPC', start= '2000-01-01', end= date.today(), interval= frame)
var['share_perfomance'] = var['Adj Close'].pct_change()
variacion = round(var.iloc[-1]['share_perfomance'] * 100, 2)

col1, col2, col3 = st.columns(3)
col1.metric(label = "Precio Actual", value= f"${round(var.iloc[-1]['Adj Close'], 2)}", delta= f'{variacion} %')
col2.metric(label = 'Precio mas alto del periodo', value= f"${round(var.iloc[-1]['High'], 2)}")
col3.metric(label = 'Precio mas bajo del periodo', value= f"${round(var.iloc[-1]['Low'], 2)}")

# Desarrollo de las graficas del dashboard
fig = make_subplots(rows=2, cols=2, start_cell="top-left", subplot_titles=(f"SP500: Movimiento del precio en marco {frame}", f"Grafica de variacion porcentual en marco {frame}", "Volumen", f'Distribucion de movimientos porcentuales Marco de {frame}'))

fig.add_trace(go.Scatter(x= sp_data['Date'], y=sp_data['Adj Close']),
              row=1, col=1)

fig.add_trace(go.Bar(x= sp_data['Date'], y=sp_data['share_perfomance']),
              row=1, col=2)

fig.add_trace(go.Bar(x= sp_data['Date'], y=sp_data['Volume']),
              row=2, col=1)

fig.add_trace(go.Histogram (x=sp_data['share_perfomance']),
              row=2, col=2)

st.plotly_chart(fig, use_container_width=True)






