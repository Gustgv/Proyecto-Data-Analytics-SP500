# Proyecto-Data-Analytics-SP500
**_Licenciado: Gustavo Rafael Gonzalez_**

<p align="justify"> Recientemente se me ha solicitado de una semana a otra realizar un proceso de transformacion de datos y desarrollar una API, adicional a eso, me han encargado elaborar un modelo de ML de recomendacion de peliculas, basandose en el usuario y la pelicula. En este README encontrarán toda la documentación, e instrucciones necesarias, para poder utilizar la API que se me solicitó desarrollar y su enlace de acceso en **DETA**, asi mismo brindare los enlaces correspondientes al sistema de recomendaciones desplegado en **STREAMLIT** y la notebook que corresponde al desarrollo del modelo. </p>


🟣**MENU:** 🟣

🔹 **Fastapideta** - Carpeta con con paquetes requeridos para deployment de la API en depa.<br>
🔹 **Raw** - las bases de datos que recibí para trabajar.<br>
🔹 **ML_proyecto.ipynb** - notebook del proyecto de Machine Learning.<br>
🔹 **transformacion.ipynb** - notebook que contiene el trabajo de ETL de los datos.<br>
🔹 **querys.ipynb** - notebook que contienen el proceso de desarrollo de las queries.<br>
🔹 **rating_data.parquet** - dataset que contiene registros de rating de peliculas por usuario.<br>
🔹 **movie_data.csv** - dataset con tiene peliculas por plataforma como netfli, disney, entre otros.<br>

## API

🟣 **Enlaces de acceso** 🟣

🔹 API: https://deta.space/discovery/r/cffsroh2qj7qft8c<br>

🟣 **Las funciones que componen la API son:** 🟣

🔹 **get_max_duration**: Consulta de pelicula con mayor duration, expresado en min o season.<br>
🔹 **get_score_count**: Conteo de peliculas por plataforma con un puntaje mayor a X valor en determinado año.<br>
🔹 **get_count_platform**: Conteo de películas por plataforma.<br>
🔹 **get_actor**: Presentar el actor que mas se repite segun plataforma y año.<br>


## Modelo de Machine Learning

🟣 **Enlaces de acceso** 🟣

🔹 APP Streamlit: https://gustgv-primer-proyecto-ml-reco-movies-4insnc.streamlit.app/<br>
🔹 Repositorio de sistema en Streamlit: https://github.com/Gustgv/Primer-Proyecto-ML.git<br>
🔹 Carpeta de Ratings el cual se tomo para entrenamiento del modelo: https://drive.google.com/drive/folders/1b49OVFJpjPPA1noRBBi1hSmMThXmNzxn<br>

🟣 **Las funciones del sistema de recomendaciones:** 🟣

La funcion solo necesita de tres variables:
* La id del usuario al cual quiere recomendar.
* La id de la pelicula que desea recomendar.
* El puntaje que estima que el usuario dara a la pelicula en caso de verla.

Como resultado al ingresar estas variable el sistema le dira si la pelicula es recomendada o no y de serlo estimara la puntuacion que le dara.

🟣 **Recursos Utilizados:** 🟣

[Streamlit](https://streamlit.io/) - Para desplegar el sistema de recomendaciones.<br>
[Deta](https://deta.space/) - Para desplegar API.<br>
[SDV Surprise](https://surpriselib.com/) - Libreria utilizada para implementar el modelo de ML.<br>
[Pandas](https://pandas.pydata.org/) - Libreria para la manipulacion de los dataset.




