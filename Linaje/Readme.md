# Linaje de Datos

A continuación se presenta una serie de esquemas que representan el linaje de datos que se piensa será de interés para el proyecto, hasta la fecha en que se elabora el presente documento.

## Etapa Raw

Esta estapa se refiere a cuando se obtienen los datos crudos (*Raw*) desde el API de la base de datos Rita, en formato .zip y son cargados a un servicio de almacenamiento S3.

| Nombre            | Función                                           	            |
|-----------------	|----------------------------------------------------------------	|
| fecha            	| fecha de ejecución                                              |
| parametros      	| parámetros con los que se ejecuto el task                      	|
| usuario         	| quien ejecuto el task*                                         	|
| ip_ec2          	| Corresponde a la dirección IP desde donde se ejecuto la tarea  	|
| tamano_zip       	| tamaño del zip                                                	|
| nombre_archivo  	| nombre del archivo nuevo generado                              	|
| ruta_s3         	| load ocurre en S3, ruta de almacenamiento incluyendo el bucket 	|
| variables_datos 	| variables en el orden en que aparecen                          	|



## Etapa Pre-processed

Corresponde a la etapa en que se realiza un pre-procesamiento de los datos obtenidos en la etapa previa.

| Nombre                    	| Función                                      	|
|---------------------------	|----------------------------------------------	|
| fecha                     	| fecha de ejecución                           	|
| usuario                   	| quien ejecuto el task*                       	|
| ejecucion                 	| cambio a csv, número de renglones           	|
| ip_preprocesed             	| donse se ejecuto (S3)                        	|
| status                    	| estatus de ejecución: Fallido, exitoso, etc. 	|

## Etapa Clean

En seguimiento a lo anterior, en esta etapa se realiza la limpieza de los datos pre-procesados.

| Nombre                     	| Función                                               	|
|----------------------------	|-------------------------------------------------------	|
| fecha                      	| fecha de ejecución                                    	|
| usuario                    	| quien ejecuto el task*                                	|
| tipo_columna               	| tipo de datos en cada columna                         	|
| ip_clean                   	| Corresponde a la dirección IP desde donde se ejecuto la tarea|
| ejecucion                  	| imprimirá nombre de funciones del script de transform 	|
| num_observaciones_cargadas 	| número de registros modificados                       	|
| status                     	| estatus de ejecución: Fallido, exitoso, etc.          	|
