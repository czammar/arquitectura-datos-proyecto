# Diseño de producto de datos

## 1. Definición de proyecto a realizar

Como se ha mencionado previamente, el interés de este proyecto gira en torno a la base de datos denominada conocida como [RITA](http://stat-computing.org/dataexpo/2009/the-data.html), la cual provee una serie de datos de vuelos que incluyen salidas a tiempo, llegadas a tiempo, demoras, vuelos cancelados de todo Estados Unidos del Departamento de Transporte, poseyendo una frecuencia de actualización mensual, con datos históricos desde junio del 2003.

Ahora bien, dado que los tiempos de viaje de los usuarios se encuentran sujetos a la disponibilidad y viabilidad de los vuelos de las aerolíneas comerciales, los cuales a su vez se encuentran estrechamente ligados a otros factores (por ejemplo, políticas comerciales, incidentes de seguridad o eventos climáticos), los pasajeros experimentan cierto nivel de incertidumbre sobre si sus vuelos serán retrasados o cancelados en definitiva.

Una forma de poder atacar la incertidumbre de los viajeros, sería contar con una sistema que pueda dar elementos a los usuarios acerca de 1) si existirá retraso en su vuelo, 2) en caso de que exista retraso, pueda informar el lapso de tiempo  equivalente a dicho evento, o 3) indique si su vuelo se cancelará. 

Ello permitirá no solo que **los usuarios prevean la administración de su tiempo al realizar viajes**, sino que puedan diseñar estrategia que les permita continuar con su viaje en caso de una probable cancelación de un vuelo.

Con ello en mente, el problema que pretende abordar el presente proyecto, a través del desarrollo de producto de datos, es la incertidumbre de los viajeros ante retraso en los vuelos, siendo la pregunta que guía el proyecto es **¿que intervalo de tiempo se va a retrasar mi vuelo, o si bien será cancelado?**.

El objetivo, por tanto, será desarrollar un sistema que permita predecir retrasos en vuelos de forma precisa para que los viajeros puedan planear su agenda de viaje de acuerdo a los probables retrasos o cancelaciones de las aerolíneas. Este sistema estará dirigido a los pasajeros de la aerolínea. Es decir, el público en general que va a viajar dentro de Estados Unidos. 

## 2. Diagrama (mock-up)

En línea con la exposición anterior, el problema planteado se abordará desde la perspectiva de predicción. Para ello, se planteará, dentro del contexto de aprendizaje de máquina, un problema de clasificación con intervalos de tiempo secuenciales (*bins*), con amplitud 15 minutos. Es decir, si el vuelo estará retrasado de 1 a 15 minutos, de 16 minutos a 30 minutos, en incrementos de 15 minutos, o bien si el vuelo será cancelado, para que este pueda prever una estrategia que le permita continuar con su viaje.

En tales términos, el siguiente diagrama muestra una propuesta para el diseño del producto de datos, donde la solución propuesta será una aplicación web a través de la cuál el usuario ingresará la clave del vuelo para recibir una predicción del lapso tiempo de retraso predecido, o la posible cancelación del mismo.

![Diagrama de flujo del producto](Imagenes/disenyo.png?raw=true "Title")


## 3. Descripción de la base de datos

Como ya se mencionó, esta base de datos contiene los tiempos planeados y verdaderos de despegue, así como de llegada, reportados por aerolíneas certificadas de Estados Unidos que acumulan al menos $1\%$ de las ganancias provenientes de pasajeros domésticos planeados. Tales datos se recolectan por la Oficina de Información Aérea del Departamento de Estadísticas de Transporte (*US DOT*, por sus siglas en inglés).

Con referencia a su historicidad, este conjunto de datos comprende desde 1987, hasta 2019 (a la fecha de elaboración del presente documento), actualizándose mes con mes. 

Sobre tales, es dable mencionar que las aerolíneas reportan, muchas veces voluntariamente, una serie de datos generales relativos a los vuelos que operan, en los términos siguientes términos: llegadas y salidas a tiempo para vuelos por mes y por año, por aerolínea, por aeropuertos de origen y de destino; lo cual incluye salidas y llegadas planeadas y verdaderas, vuelos cancelados o desviados, los tiempos de *taxi-in* y *taxi-out*, las causas de retraso y cancelación, tiempo de vuelo, así como distancia continua.

A continuación se muestra un consolidado de las variables de la base de datos que fueron truncadas hasta 2008:

![Descripción de las variables](Imagenes/data_var.jpeg?raw=true "Title")

Para facilitar el entendimiento de la información recién expuesta, la siguiente tabla muestra un resumen no exhaustivo de las variables en comento.

| Variable                                        | Descripción   |
|-------------------------------------------------|---|
| Actual Arrival Times                            |La hora de llegada a la puerta es el caso cuando el piloto pone el freno de estacionamiento de la aeronave después de llegar a la puerta del aeropuerto o al área de descarga de pasajeros. Si el freno de estacionamiento no está activado, registre el tiempo de apertura de la puerta del pasajero. Además, los transportistas que utilizan un Sistema de guía de acoplamiento (DGS, por sus siglas en inglés) pueden registrar el tiempo oficial de llegada de la puerta cuando el avión se detiene en la marca de estacionamiento adecuada.   |
| Actual Departure Times                          |   La hora de salida de la puerta es el caso en que el piloto suelta el freno de estacionamiento de la aeronave después de que los pasajeros se hayan cargado y las puertas de la aeronave se hayan cerrado. En los casos en que el vuelo regresó a la puerta de salida antes de la hora de salida de las ruedas y salió por segunda vez, informe la última hora de salida de la puerta antes de la hora de salida de las ruedas. En caso de retorno aéreo, informe la última hora de salida de la puerta antes del regreso de la puerta. Si los pasajeros fueron abordados sin poner el freno de estacionamiento, registre la hora en que se cerró la puerta del pasajero. Además, los transportistas que utilizan un Sistema de guía de atraque pueden registrar el tiempo oficial de salida de la puerta en función del movimiento de la aeronave. Por ejemplo, un DGS registra el tiempo de salida de la puerta cuando la aeronave se mueve a más de 1 metro de la marca de estacionamiento apropiada en 15 segundos. Luego se restan quince segundos del tiempo registrado para obtener el tiempo de salida apropiado.|
| Airline ID                                      |Un número de identificación asignado por US DOT para identificar una aerolínea (compañía aérea) única. Una aerolínea (aerolínea) única se define como una tenedora e informa bajo el mismo certificado DOT, independientemente de su Código, Nombre o compañía / corporación controladora. Use este campo para el análisis en un rango de años.   |
| Airport Code                                    | Un código alfanumérico de tres caracteres emitido por el Departamento de Transporte de EE. UU., Que es la designación oficial del aeropuerto. El código de aeropuerto no siempre es exclusivo de un aeropuerto específico porque los códigos de aeropuerto pueden cambiar o pueden reutilizarse.  |
| Airport ID                                      | Un número de identificación asignado por US DOT para identificar un aeropuerto único. Utilice este campo para el análisis del aeropuerto a lo largo de varios años porque un aeropuerto puede cambiar su código de aeropuerto y los códigos de aeropuerto pueden reutilizarse.  |
| Arrival Delay                                   | El retraso de llegada es igual a la diferencia de la hora de llegada real menos la hora de llegada programada. Un vuelo se considera a tiempo cuando llega menos de 15 minutos después de su hora de llegada publicada.  |
| CRS                                             |   Sistema de reserva por computadora. CRS proporciona información sobre horarios de aerolíneas, tarifas y disponibilidad de asientos a agencias de viajes y permite a los agentes reservar asientos y emitir boletos.|
| Cancelled Flight                                |  Un vuelo que figuraba en el sistema de reserva de computadoras de un transportista durante los siete días calendario anteriores a la salida programada pero que no fue operado. |
| Carrier Code                                    |  Código asignado por IATA y comúnmente utilizado para identificar un operador. Como el mismo código puede haber sido asignado a diferentes operadores a lo largo del tiempo, el código no siempre es único. |
| Certificate Of Public Convenience And Necessity |Un certificado emitido a una compañía aérea menor de 49 U.S.C. 41102, por el Departamento de Transporte que autoriza al transportista a participar en el transporte aéreo.   |
| Certificated Air Carrier                        | Una compañía aérea que posee un Certificado de Conveniencia Pública y Necesidad emitido por el DOT para realizar servicios inter-estatales programados. Las operaciones no programadas o charter también pueden ser realizadas por estos transportistas. (igual que el transportista aéreo certificado)  |
| Certified Air Carrier                           |  Una compañía aérea que posee un Certificado de Conveniencia Pública y Necesidad emitido por el DOT para realizar servicios inter-estatales programados. Las operaciones no programadas o charter también pueden ser realizadas por estos transportistas. (igual que el transportista aéreo certificado). |
| City Market ID                                  |  Un número de identificación asignado por US DOT para identificar un mercado de la ciudad. Use este campo para consolidar aeropuertos que presten servicio al mismo mercado de la ciudad. |
| Departure Delay                                 |   La diferencia entre la hora de salida programada y la hora de salida real desde la puerta del aeropuerto de origen.|
| Diverted Flight                                 |  Un vuelo que debe aterrizar en un destino que no sea el destino programado original por razones que escapan al control del piloto / compañía. |
| Domestic Operations                             |  Todas las operaciones de compañías aéreas que tienen destinos dentro de los 50 Estados Unidos, el Distrito de Columbia, el Estado Libre Asociado de Puerto Rico y las Islas Vírgenes de los Estados Unidos. |
| Elapsed Time                                    |El tiempo calculado desde la hora de salida de la puerta hasta la hora de llegada de la puerta.   |
| FIPS                                            |  Normas federales de procesamiento de información. Por lo general, se refiere a un código asignado a cualquiera de una variedad de entidades geográficas (por ejemplo, condados, estados, áreas metropolitanas, etc.). Los códigos FIPS están destinados a simplificar la recopilación, el procesamiento y la difusión de datos y recursos del Gobierno Federal. |
| Flight Number                                   |  Un código alfanumérico de uno a cuatro caracteres para un vuelo en particular. |
| In-Flight Time                                  | El tiempo total que una aeronave está en el aire entre un par de aeropuertos de origen a destino, es decir, desde las ruedas en el aeropuerto de origen hasta las ruedas en el aeropuerto de destino.  |
| Late Flight                                     |  Un vuelo que llega o sale 15 minutos o más después de la hora programada. |
| Passenger Revenues                              |  Ingresos del transporte aéreo de pasajeros.|
| Scheduled Departure Time                        |  La hora programada en que un avión debe despegar del aeropuerto de origen.|
| Scheduled Time Of Arrival | La hora programada en que un avión debe cruzar un cierto punto (aterrizaje o corrección de medición).|
| Taxi-In Time                                    |El tiempo transcurrido entre las ruedas hacia abajo y la llegada a la puerta del aeropuerto de destino.|
| Taxi-Out Time                                   |  El tiempo transcurrido entre la salida de la puerta del aeropuerto de origen y las ruedas. |
| Unique Carrier                                  |  Código de transportista único. Es el código de operador más recientemente utilizado por un operador. Se utiliza un sufijo numérico para distinguir códigos duplicados, por ejemplo, PA, PA (1), PA (2). Use este campo para realizar el análisis de los datos informados por un solo operador. |
| World Area Code (WAC)                           |  Códigos numéricos utilizados para identificar áreas geopolíticas como países, estados (EE. UU.), Provincias (Canadá) y territorios o posesiones de ciertos países. Los códigos se utilizan dentro de los diversos bancos de datos mantenidos por la Oficina de Información de Aerolíneas (OAI) y son creados por OAI. |

Finalmente, incluimos la distribución  durante el último año de los datos (2019) respecto a si los vuelos salieron a tiempo o se retrasaron (diferenciando la razón del retraso) en un gráfico de pay expuesto fuente de la base de datos(ver [https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp](https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp)).

![Composición de los datos durante 2019](Imagenes/data_ytd.jpeg?raw=true "Title")
