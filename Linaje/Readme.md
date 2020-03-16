# Linaje de Datos

A continuación se presenta una serie de esquemas que representan el linaje de datos que se piensa será de interés para el proyecto, hasta la fecha en que se elabora el presente documento.

## Etapa Raw

Se refiere a la etapa en que se obtienen los datos crudos (*Raw*) desde el API de la base de datos Rita, en formato .zip. Al respecto se estima pertinente que los metadatos de esta fase se agrupen en torno a los siguientes campos:

[**Pendiente:** No estoy seguro del alcance de esta etapa, describe la carga de los zips a s3? si es asi tiene sentido que consideremos el "número de renglones que se añadieron"? ]

| Nombre            | Función                                           	            |
|-----------------	|----------------------------------------------------------------	|
| fecha            	| fecha de ejecución                                              |
| parametros      	| parámetros con los que se ejecuto el task                      	|
| usuario         	| quien ejecuto el task*                                         	|
| ip_ec2          	| Corresponde a la dirección IP desde donde se ejecuto la tarea  	|
| num_renglones   	| número de renglones que se añadieron                           	|
| nombre_archivo  	| nombre del archivo nuevo generado                              	|
| ruta_s3         	| load ocurre en S3, ruta de almacenamiento incluyendo el bucket 	|
| variables_datos 	| variables en el orden en que aparecen                          	|

## Etapa Pre-processed

Corresponde a la etapa en que se realiza un pre-procesamiento de los datos obtenidos en la etapa previa, realizando una serie de acciones sobre los mismos consistentes en [**Pendiente:** No estoy seguro del alcance de esta etapa, por favor precisar]. En líne con ellolos metadatos de esta fase se agruparán como sigue:

| Nombre                    	| Función                                      	|
|---------------------------	|----------------------------------------------	|
| fecha                     	| fecha de ejecución                           	|
| usuario                   	| quien ejecuto el task*                       	|
| num_observaciones_limpias 	| número de registros que fueron limpiados     	|
| status                    	| estatus de ejecución: Fallido, exitoso, etc. 	|

## Etapa Clean

En seguimiento a lo anterior, en esta etapa se realiz la limpieza de los datos pre-procesados, consistentes en [**Pendiente:** No estoy seguro del alcance de esta etapa, por favor precisar]. 

| Nombre                     	| Función                                               	|
|----------------------------	|-------------------------------------------------------	|
| fecha                      	| fecha de ejecución                                    	|
| usuario                    	| quien ejecuto el task*                                	|
| tipo_columna               	| tipo de datos en cada columna                         	|
| ip_ec2                     	| Corresponde a la dirección IP desde donde se ejecuto la tarea|
| ejecucion                  	| imprimirá nombre de funciones del script de transform 	|
| num_observaciones_cargadas 	| número de registros modificados                       	|
| status                     	| estatus de ejecución: Fallido, exitoso, etc.          	|
