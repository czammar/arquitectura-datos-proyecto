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
En una instancia EC2  corre programa en python llamado update.py donde semanalmente usando CROM llama download_rita.sh, en este punto compara si hay actualizaciones por medio de PostgresSQL.

La función de PostgresSQL es con los parámetros mes y año buscar cuál fue el último mes cargado por medio de ordenar la tabla en forma descendente y comparar si el primer dato es igual o diferente, si este es diferente se actualiza la tabla, en caso de estar vacía la tabla carga el primer mes histórico.

### Load

### Transform

En la etapa de transformación de datos, se aplica una serie de reglas o funciones a los datos extraídos para prepararlos para la carga en el destino final, nuestro almacen de datos en PostGreSQL que vivirá en una instancia de Cómputo Elástico en la Nube (EC2, por sus siglas en inglés).

Una función importante de esta etapa de transformación es la limpieza de datos, que tiene como objetivo pasar solo datos "adecuados" al entorno analítico. Para resolver el desafío de la interacción entre nuestra cubeta de S3 y nuestra base de PostGreSQL se incluirá en la rutina de orquestación de Python una sección con la librería Boto3 para recuperar los datos crudos, transformarlos con esa misma rutina y después utilizar la librería PsicoPG2 para cargar en nuestro almacen de datos de PostGreSQL en nuestra instancia de EC2 destinada al entorno analítico.

Uno o más de los siguientes tipos de transformación pueden ser necesarios para satisfacer las necesidades del problema en cuestión:

* Seleccionar sólo ciertas columnas para cargar (o seleccionando columnas nulas para no cargar).

* Traducción de valores codificados (hacer entendibles las etiquetas).

*  Codificación de valores de forma libre: (por ejemplo, mapeo "Macho" a "M").
*	Derivar un nuevo valor calculado: (por ejemplo, sale_amount = qty * unit_price).
*   Ordenar los datos en función de una lista de columnas para mejorar el rendimiento de búsqueda (i.e.: escoger sortkeys y distkeys adecuadas).
*   Agregación (por ejemplo, resumen - resumen de varias filas de datos - retrasos totales para cada aereopuerto, y para cada región, etc.)
*    Transposición o pivote (convertir múltiples columnas en múltiples filas o viceversa).
*    Dividir una columna en varias columnas (por ejemplo, convertir una lista separada por comas, especificada como una cadena en una columna, en valores individuales en diferentes columnas).

*   Aplicando cualquier forma de validación de datos; la validación fallida puede dar como resultado un rechazo total de los datos, un rechazo parcial o ningún rechazo y, por lo tanto, ninguno, algunos o todos los datos se transfieren al siguiente paso, según el diseño de la regla y el manejo de excepciones.

 Muchas de las transformaciones anteriores pueden dar lugar a excepciones, por ejemplo, cuando una traducción de código analiza un código desconocido un cambio súbito en los datos extraídos por lo que el último punto de validación es importante.




## Diagrama

![Diagrama de flujo del ETL](images/etl2.png?raw=true "Title")
(https://drive.google.com/file/d/1aYgxZ5BnPjNXAMo6qNAPVHjWbP7cOrB9/view?usp=sharing)
