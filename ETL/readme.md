# ETL para el proyecto de la base de datos RITA

25 de febrero de 2019

## 1. Introducción

Este documento tiene como objetivo de describir, a manera de *mock-up*, el ETL para la ingestión de los datos de RITA para el diseño de un producto de datos encaminado a predecir intervalos de retraso de los vuelo de los usuarios de aerolíneas en Estados Unidos.

Dicho proceso se realizará con base en una serie especificaciones que se plantearán, a manera de preguntas, y que serán las directrices de ésta etapa del proyecto, mismas que se exponen a continuación.

## 2. Especificaciones para la definición del ETL y la ingesta de datos

**1) ¿Con qué frecuencia se publican los datos?**
  - Para esta base se realizan actualizaciones de datos de manera mensual. Sin embargo se identificó que la última publicación de los mismos se realizó hasta Noviembre de 2019. Esto añade un punto a considerar en el proyecto sobre la disponibilidad de la información, y los periodos en que se tiene que consultar para obtener el último tren de información disponible en razón de que se deberá realizar consultas periódicas en busca de nuevos trenes de datos disponibles, cuales podrían estar listos con un cierto desfase.

  En cualquier caso, el proceso de ingesta de datos se realizará con base en la información disponible más reciente.

**2) ¿Cada cuánto ingestaremos los datos?**
  - Considerando a la respuesta al pregunta previa, se plantea hacer una consulta de nuevos de manera semanal, para que una vez que se encuentren nuevas cargas de trenes de datos, podamos ingestar los procesos que permiten el funcionamiento del producto de datos.

**3) ¿Cómo ingestaremos los datos?**
  - El proceso de ingesta se plantea llevar a cabo a través de un script de Bash, que se corre semanalmente, se obtienen los datos en formato .zip, para periodos mensuales. Esto con miras a obtener la última información disponible.

**4) ¿Dónde guardaremos los datos?**
  - Se estima pertinente emplear en una cubeta S3 (*bucket*) para conservar historicidad de los mismos y detectar posibles errores en la dinámica del producto de datos. En este sentido, se considera realizar posteriormente transformaciones de este conjunto de datos hacia lam carga de una base de datos empleando PostGreSQL.

**5) ¿En qué formato?**
  -  Tal como se ha mencionado, se plantea guardarlos en el formato original de descarga, el cual corresponde archivos de extensión .zip (en la cubeta S3) los cuales son versiones comprimidas de archivos .csv de la base.
  - Este punto es relevante, dado que nos permitirá administra los nuevos datos correspondientes a entregas mensuales dentro de S3, tomando como referencia las fechas a las que corresponden.
  - Además, como una linea futura de trabajo, se plantea explorar el guardar los datos empleando el formato *parquet*.

**6) ¿Los transformamos antes de guardarlos?**
  - Se considera relevante mantener los datos en el formato y estructura en que son provistos desde la fuente de las aerolíneas, de manera que podamos considerar en el *pipeline* del producto de datos la historicidad de los mismo en una cubeta de S3. Sin embargo, se contempla realizar transformaciones a los mismos en el proceso de carga hacia la base de datos de PostGreSQL.

Con base en los puntos expuestos, a continuación explicaremos cada una de las etapas que integrarán el ETL.

## 3. Descripción de etapas

### 3.1 Extract

En dicha etapa se plantea que a través de una una instancia de Cómputo Elástico en la Nube (EC2, por sus siglas en inglés). A través de ella se correrá  semanalmente un programa de Python, denominado **update.py**, que nos permitirá emplear la herramienta CROM para activar un script de Bash (**download_rita.sh**) el cual se encargará de la descarga de la datos de la base RITA, al tiempo que permitirá determinar si hay actualizaciones de la información histórica, para actualizar el proceso de ingesta del producto de datos. Para ello se plantea la comunicación de una base en PostgresSQL, que contendrá la información que hemos ido agregando de manera histórica.

En este sentido, dicha base de PostgresSQL nos permitirá:

* Poblar la tabla de datos de la base, en su creación (dado que estará vacía en la construcción del primer mes histórico),
* Obtener los parámetros de mes y año respecto a los cuales se cargó la información del último mes, con el propósito de determinar si la ingesta de nuevos datos debe llevarse a cabo en dicho periodo de ejecución de este script. Para llevar a cabo esta acción, se plantea ordenar una tabla de la base de datos con respecto a la fecha, en forma descendente, y tras comparar si el primer dato es igual o diferente; de manera de que al encontrar diferencia entre ambos se extraerán nuevos datos, mismos que en etapas posteriores se añadirán al PostGreSQL.

### 3.2 Load

Este paso consiste en realizar la carga de los datos descargados en formato .zip hacia una cubeta S3 que nos permitirá tener historicidad de la información considerada para la ingesta del producto de datos. Para ello, se plantea emplear periódicamente un script de Bash, en el EC2 de la etapa previa, que permitirá cargar los últimos datos extraídos de la página de aerolíneas para un nuevo periodo, empleando comandos de *awscli*
de manera que sea posible la cargan de estos hacia una cubeta S3, caracterizando los mismos con un formato que considere la fecha en que se obtuvo la información.

Como se ha dicho anteriormente, se plantea realizar una revisión semanal en busca de nuevas publicaciones de datos, por lo que en caso de encontrarse nueva información disponible, con dicho proceso se agregaran a la cubeta de S3 bloques nuevos de datos en formato comprimido.

### 3.3 Transform

En la etapa de transformación de datos, se aplica una serie de reglas o funciones a los datos extraídos para prepararlos para la carga en el destino final, nuestro almacén de datos en PostGreSQL que vivirá en una instancia EC2.

Una función importante de esta etapa de transformación es la limpieza de datos, que tiene como objetivo pasar solo datos "adecuados" al entorno analítico. Para resolver el desafío de la interacción entre nuestra cubeta de S3 y nuestra base de PostGreSQL se incluirá en la rutina de orquestación de Python una sección con la librería Boto3 de Python, lo que permitirá recuperar los datos crudos, transformarlos con esa misma rutina y después utilizar la librería PsicoPG2 de Python para cargar en nuestro almacén de datos de PostGreSQL en nuestra instancia de EC2 destinada al entorno analítico.

Uno o más de los siguientes tipos de transformación pueden ser necesarios para satisfacer las necesidades del problema en cuestión:

* Seleccionar sólo ciertas columnas para cargar (o seleccionando columnas nulas para no cargar).
* Traducción de valores según su codificación (para hacer entendibles las etiquetas).
* Transformación de valores de forma libre: (por ejemplo, en un mapeo qué permita entender o describir su codificación, como "Macho" a "M").
*	Derivar un nuevo valor calculado: (por ejemplo, *sale_amount = qty * unit_price*).
* Ordenar los datos en función de una lista de columnas para mejorar el rendimiento de búsqueda (i.e.: escoger *sortkeys* y *distkeys* adecuadas).
* Agregación (por ejemplo, resumen - resumen de varias filas de datos - retrasos totales para cada aeropuerto, y para cada región, etc.)
* Transposición o pivote (convertir múltiples columnas en múltiples filas o viceversa).
* Dividir una columna en varias columnas (por ejemplo, convertir una lista separada por comas, especificada como una cadena en una columna, en valores individuales en diferentes columnas).

*  Aplicando cualquier forma de validación de datos; la validación fallida puede dar como resultado un rechazo total de los datos, un rechazo parcial o ningún rechazo y, por lo tanto, ninguno, algunos o todos los datos se transfieren al siguiente paso, según el diseño de la regla y el manejo de excepciones.

 Muchas de las transformaciones anteriores pueden dar lugar a excepciones, por ejemplo, cuando una traducción de código analiza un código desconocido un cambio súbito en los datos extraídos por lo que el último punto de validación es importante.

## 4. Diagrama

Para facilitar el entendimiento del proceso recién descrito, presentamos un diagrama que describe las actividades a realizar en cada una de las etapas del ETL.

![Diagrama de flujo del ETL](images/etl3.png?raw=true "Title")
(https://drive.google.com/file/d/1aYgxZ5BnPjNXAMo6qNAPVHjWbP7cOrB9/view?usp=sharing)
(https://www.draw.io/#G17QEIJYjJwGIPJViHqTRJg0UPf8I40m2j)

EL hasta el momento

![Diagrama de flujo del EL](images/EL.png?raw=true "Title")

## 5. Implicaciones éticas del proyecto

Al respecto, se identifican posibles implicaciones éticas del producto de datos hasta aquí planteando:

**Eje de usuarios:**

* Hacer que pierdan vuelos y deban hacer doble gasto en un viaje,
* Sesgar a que los usuarios viajen o no en una aerolínea,

**Eje de aerolíneas:**

* Perjudicar la reputación  de una aerolínea,
* Proyectar la responsabilidad de eventos fuera de su control,
* Dañar su estabilidad económica y empleos,
* Aumentar quejas injustificadas del servicio.

## 6. Contenido la carpeta

| # | Carpeta                       | Descripción  |
|---|-----------------------------------|--------|
| 1 | download_rita_parquet.py | Archivo que extrae una fracción de los datos, para convertirla a formato .parquet |
| 2 | orquestador.py | Programa que funge como orquestador |
| 3 | prueba.py | Script que lista el contenido del bucket, junto con su peso. No forma parte del pipeline, solo se usa como acción ilustrativa para probar que al bucket se han cargado exitosamentente los datos. |
| 4 | limpia_cubeta.py | Script que vacía el bucket que se ha subido a la cubeta; nuevamente no forma parte del pipeline, solo se emplea como una acción ilustrativa para enseñar en clase el corrector funcionamiento del orquestador |
| 5 | rita_pyenv.sh | Script de Bash para descargar pyenv y pyenv virtualenv, de modo que sea posible crear un ambiente virtial denominado *Rita*, con todas las dependencias de Python necesarias para la ejecución de proyecto.  |




Para correr el orquestador, se debe ejecutar la instrucción:

```
PYTHONPATH='.' AWS_PROFILE=dpa luigi --module orquestador S3Task --local-scheduler
```

**Notas**

* Para la correcta ejecución, se debe asegurar que se ha corrido el archivo *limpia_cubeta.py*, posteriormente correr el orquestador, y verificar el contenido con el script *prueba.py*
* El archivo Bash es un script implementado para instalar un ambiente virtual de Python 3.7.3, denominado "rita" que posee las dependencias necesarias para el proceso recién descrito.


Ello baja un fracción de los datos, para convertirlos a .parquet y subirlos al bucket. Además se debe considerar lo siguiente:


