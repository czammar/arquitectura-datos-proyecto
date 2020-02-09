# Diseño de producto de datos

## 1. Definición de proyecto a realizar

Como se ha mencionado previamente, el interés de este proyecto gira en torno a la base de datos denominada conocida como [RITA](http://stat-computing.org/dataexpo/2009/the-data.html), la cual provee una serie de datos de vuelos que incluyen salidas a tiempo, llegadas a tiempo, demoras, vuelos cancelados de todo Estados Unidos del Departamento de Transporte, poseyendo una frecuencia de actualización mensual, con datos históricos desde junio del 2003.

Ahora bien, dado que los tiempos de viaje de los usuarios se encuentran sujetos a la disponibilidad y viabilidad de los vuelos de las aerolíneas comerciales, los cuales a su vez se encuentran estrechamente ligados a otros factores (por ejemplo, políticas comerciales, incidentes de seguridad o eventos climáticos), los pasajeros experimentan cierto nivel de incertidumbre sobre si sus vuelos serán retrazados o cancelados en definitiva.

Una forma de poder atacar la incertidumbre de los viajeros, sería contar con una sistema que pueda dar elementos a los usuarios acerca de 1) si existirá retraso en su vuelo, 2) en caso de que exista retraso, pueda informar el lapso de tiempo  equivalente a dicho evento, o 3) indique si su vuelo se cancelará. 

Ello permitirá no solo que los usuarios preveean la administración de su tiempo al realizar viajes, sino que puedan diseñar estrategia que les permita continuar con su viaje en caso de una probable cancelación de un vuelo.

Con ello en mente, el problema que pretende abordar el presente proyecto, a través del desarollo de producto de datos, es la incertidumbre de los viajeros ante retrazo en los vuelos, siendo la pregunta que guía el proyecto es ¿que intervalo de tiempo se va a retrazar mi vuelo?.

El objetivo, por tanto, será desarollar un sistena que permita predecir retrazos en vuelos de forma precisa para que los viajeros puedan planear su agenda de viaje de acuerdo a los probables retrazos o cancelaciónes de las aerolíneas. Este sistema estará dirigido a los pasajeros de la aerolínea. Es decir, el público en general que va a viajar dentro de Estados Unidos. 

## 2. Diagrama (mock-up)

En línea con la exposición anterior, el problema planteado se abordará desde la perspectiva de predicción. Para ello, se planteará, dentro del contexto de aprendizaje de máquina, un problema de clasificación con intervalos de tiempo secuenciales (*bins*), con amplitudd 15 minutos. Es decir, si el vuelo estará retrazado de 1 a 15 minutos, de 16 minutos a 30 minutos, en incrementos de 15 minutos, o bien si el vuelo será cancelado, para que este pueda preveer una estrategia que le permita continuar con su viaje.

En tales términos, el siguiente diagrama muestra una propuesta para el diseño del producto de datos, donde la solución propuesta será una aplicación web a través de la cuál el usuario ingresará la clave del vuelo para recibir una predicción del lapso tiempo de retrazo predecido, o la posible cancelación del mismo.

![Alt text](Imagenes/disenyo.png?raw=true "Title")


## 3. Descripción de la base de datos

[LUIS EUGENIO]
