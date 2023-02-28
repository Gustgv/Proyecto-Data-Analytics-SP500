import streamlit as st


st.image('https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcTNZpRUPTzR8kW7oiGLBfa128-ENsSyxS-46w&usqp=CAU')

st.title('Que es el SP500?')
st.text('''El índice Standard & Poors 500, también conocido como S&P 500, es uno de los índices bursátiles más importantes de
Estados Unidos.

Al S&P 500 se lo considera el índice más representativo de la situación real del mercado. El índice se basa en la capitalización
bursátil de 500 grandes empresas que poseen acciones que cotizan en las bolsas NYSE o NASDAQ, y captura aproximadamente el 80% de
toda la capitalización de mercado en Estados Unidos.

''')

st.markdown('### - Sobre el proyecto')
st.text('''El proyecto tiene como finalidad informar al cliente sobre el Standard & Poors 500, ya que es el activo que esta tomando
en consideracion para invertir.

El SP500 es uno de los indices preferidos para invertir, esto, debido a que al ser conformado por 500 empresas de gran capital, esta 
no presenta alta volatilidad como otros activos por lo tanto presenta menos riesgo de perdida de inversion.

El enfoque del analisis sera sobre los movimientos del precio del SP500 a partir del año 2000 hasta la actualidad, asi mismo, se tomara
en consideracion indicadores como volumen y variacion porcentual, en intervalos mensuales y diarios.

A lo largo de los años el indice al igual que todo activo, ha sufrido sus bajos, en el año 2000 el activo sufrio una caida del 20%
al reventar la burbuja puntocom, asi mismo en los años 2007, 2008 durante la crisis financiera global, la ultima caida significativa que
sufrio el activo fue durante la pandemia del COVID19 en 2020.


 ''')

st.markdown('### - Herramientas utilizadas')
st.write('''Para la elaboracion de este proyecto, se recurrio a las siguientes herramientas:''')
st.write('- Python [https://www.python.org/](https://www.python.org/)')
st.write('- Streamlit [https://streamlit.io/](https://streamlit.io/)')
         

st.markdown('### - Librerias Utilizadas')
st.write('Plotly - [https://plotly.com/python/](https://plotly.com/python/)')
st.write('Pandas - [https://pandas.pydata.org/](https://pandas.pydata.org/)')
st.write('Streamlit - [https://docs.streamlit.io/](https://docs.streamlit.io/)')
st.write('yfinance - [https://pypi.org/project/yfinance/](https://pypi.org/project/yfinance/)')