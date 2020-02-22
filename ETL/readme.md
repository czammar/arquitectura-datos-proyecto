# ETL

Objetivo: Definir el mockup de ETL de su proyecto (sección ingestión de datos), este proceso se realizará con base en una serie especificaciones, a manera de preguntas que sirven como directrices del proyecto para la definición del ETL correspondiente al proyecto de la base de datos RITA.

A continuación se abordan tales preguntas:

## Específicaciones
1) ¿Con qué frecuencia se publican los datos?
  - "Mensualmente".
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

### Load

### Transform


## Diagrama


(https://drive.google.com/file/d/1aYgxZ5BnPjNXAMo6qNAPVHjWbP7cOrB9/view?usp=sharing)
