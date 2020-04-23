# Linaje de Datos para la fase ETL

A continuación se presenta una serie de esquemas que representan el linaje de datos que se piensa será de interés para el proyecto, hasta la fecha en que se elabora el presente documento.

## Etapa Raw

Esta estapa se refiere a cuando se obtienen los datos crudos (*Raw*) desde el API de la base de datos Rita, en formato .zip y son cargados a un servicio de almacenamiento S3.

| Nombre            | Función                                           	            |
|-----------------	|----------------------------------------------------------------	|
| fecha            	| fecha de ejecución                                              |
| nombre_task      	| nombre del task que se ejecuto                                	|
| parametros      	| parámetros con los que se ejecuto el task                      	|
| usuario         	| quien ejecuto el task*                                         	|
| ip_ec2          	| Corresponde a la dirección IP desde donde se ejecuto la tarea  	|
| tamano_zip       	| tamaño del zip                                                	|
| nombre_archivo  	| nombre del archivo nuevo generado                              	|
| ruta_s3         	| load ocurre en S3, ruta de almacenamiento incluyendo el bucket 	|




## Etapa Pre-processed

Corresponde a la etapa en que se realiza un pre-procesamiento de los datos obtenidos en la etapa previa. Básicamente este preprocesado es la descompresión del archivo, el cambio a formato CSV.

| Nombre                    	| Función                                      	|
|---------------------------	|----------------------------------------------	|
| fecha                     	| fecha de ejecución                           	|
| usuario                   	| quien ejecuto el task*                       	|
| nombre_task               	| nombre del task que se ejecuto                |
| ejecucion                 	| cambio a CSV                                 	|
| num_observaciones_cargadas 	| número de registros cargados                	|
| ip_preprocesed             	| dónde se ejecutó (S3)                        	|
| variables_datos           	| variables en el orden en que aparecen        	|
| status                    	| estatus de ejecución: Fallido, exitoso, etc. 	|

## Etapa Clean

En seguimiento a lo anterior, en esta etapa se realiza la limpieza de los datos pre-procesados.

| Nombre                     	| Función                                               	|
|----------------------------	|-------------------------------------------------------	|
| fecha                      	| fecha de ejecución                                    	|
| nombre_task               	| nombre del task que se ejecuto                          |
| year                      	| año de los datos                               	        |
| month                   	  | mes de los datos                              	        |
| usuario                    	| quien ejecuto el task*                                	|
| ip_clean                   	| Corresponde a la dirección IP desde donde se ejecuto la tarea|
| num_filas_modificadas     	| número de registros modificados                       	|
| variables_limpias          	| variables con las que se realizará la siguiente tarea (feature engineering) 	|
| status                     	| estatus de ejecución: Fallido, exitoso, etc.          	|



## Etapa Transform


En esta etapa se realiza la tranfromación de los datos.

| Nombre                        | Función                                                       |
|----------------------------   |-------------------------------------------------------        |
| fecha                         | fecha de ejecución                                            |
| usuario                       | quien ejecuto el task*                                        |
| nombre_task                   | nombre del task que se ejecuto                                |
| tipo_columna                  | tipo de datos en cada columna                                 |
| ip_clean                      | Corresponde a la dirección IP desde donde se ejecuto la tarea |
| ejecucion                     | imprimirá nombre de funciones del script de transform         |
| num_observaciones_cargadas    | número de registros modificados                               |
| status                        | estatus de ejecución: Fallido, exitoso, etc.                  |

