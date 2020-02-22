# ETL

Objetivo: Definir el mockup de ETL de su proyecto (sección ingestión de datos), este proceso se realizará con base en una serie especificaciones, a manera de preguntas que sirven como directrices del proyecto para la definición del ETL correspondiente al proyecto de la base de datos RITA.

En así que para dar contexto a como desarrollaremos el ETL del proyecto se abordan tales preguntas:

## Específicaciones
1) ¿Con qué frecuencia se publican los datos?
  - Como se ha mencionado previamente, para esta base de datos, se realizan actualizaciones de datos de manera mensual, sin embargo conocemos que la última publicación de los datos se realizó hasta Noviembre de 2019. Esto añade una consideración a la disponibilidad de la información, y los periodos en que se tiene que consultar para obtener el último tren de información disponible.
2) ¿Cada cuánto ingestaremos los datos?
  - Considerando a la respuesta al pregunta 1), se plantea hacer una consulta de nuevos de manera semanal, para que una vez que se encuentren nuevas cargas de trenes de datos, podamos ingestar los procemos que permiten la modelación.
3) ¿Cómo ingestaremos los datos?
  - El proceso de ingesta se plantea llevar a cabo a través de una serie de pasos:
    * A través de un script de Bash, que se corre semanalmente, se obtienen los datos en formato .zip, para periodos mensuales. Esto con miras a obtener la última información disponible.
    * El proceso de ejecución
4) ¿Dónde guardaremos los datos?
  - En primera instancia en una cubeta S3, después los transformaremos en una base de datos postgres
5) ¿En qué formato?
  - Se guardan en formato .zip (en la cubeta S3). 
  - En un futuro exploraremos guardarlo en parquet.
  - Dentro de S3 se organizaran por fechas.
6) ¿Los transformamos antes de guardarlos?
  - No.

## Descripción de étapas
### Extract

### Load

### Transform


## Diagrama

![Diagrama de flujo del ETL](images/etl.png?raw=true "Title")
(https://drive.google.com/file/d/1aYgxZ5BnPjNXAMo6qNAPVHjWbP7cOrB9/view?usp=sharing)
