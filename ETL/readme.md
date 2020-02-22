# ETL

Objetivo: Definir el mockup de ETL de su proyecto (sección ingestión de datos), este proceso se realizará con base en una serie especificaciones, a manera de preguntas que sirven como directrices del proyecto para la definición del ETL correspondiente al proyecto de la base de datos RITA.

En así que para dar contexto a como desarrollaremos el ETL del proyecto se abordan tales preguntas:

## Específicaciones
1) ¿Con qué frecuencia se publican los datos?
  - Como se ha mencionado previamente, para esta base de datos, se realizan actualizaciones de datos de manera mensual, sin embargo conocemos que la última publicación de los datos se realizó hasta Noviembre de 2019. Esto añade una consideración a la disponibilidad de la información, y los periodos en que se tiene que consultar para obtener el último tren de información disponible.
2) ¿Cada cuánto ingestaremos los datos?
  - Semanalmente.
3) ¿Cómo ingestaremos los datos?
  - Con un bash script que se corre semanalmente. 
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
En una instancia EC2  corre programa en python llamado update.py donde semanalmente usando CROM llama download_rita.sh, en este punto compara si hay actualizaciones por medio de PostgresSQL.

La función de PostgresSQL es con los parámetros mes y año buscar cuál fue el último mes cargado por medio de ordenar la tabla en forma descendente y comparar si el primer dato es igual o diferente, si este es diferente se actualiza la tabla, en caso de estar vacía la tabla carga el primer mes histórico.

### Load
En el paso Load corre un script de Bash en el cual los se cargan los datos en una cubeta S3 en formato zip, y estos datos están ordenados por fecha. Los datos son revisados semanalmente y se agregan los bloques nuevos de datos a la cubeta.

### Transform


## Diagrama

![Diagrama de flujo del ETL](images/etl2.png?raw=true "Title")
(https://drive.google.com/file/d/1aYgxZ5BnPjNXAMo6qNAPVHjWbP7cOrB9/view?usp=sharing)
