# Linaje de Datos

## Raw

| Nombre            | Función                                           	            |
|-----------------	|----------------------------------------------------------------	|
| fecha            	| fecha de ejecución                                              |
| parametros      	| parámetros con los que se ejecuto el task                      	|
| usuario         	| quien ejecuto el task*                                         	|
| ip_ec2          	| desde donde se ejecuto                                         	|
| num_renglones   	| número de renglones que se añadieron                           	|
| nombre_archivo  	| nombre del archivo nuevo generado                              	|
| ruta_s3         	| load ocurre en S3, ruta de almacenamiento incluyendo el bucket 	|
| variables_datos 	| variables en el orden en que aparecen                          	|

## Preprocesed

| Nombre                    	| Función                                      	|
|---------------------------	|----------------------------------------------	|
| fecha                     	| fecha de ejecución                           	|
| usuario                   	| quien ejecuto el task*                       	|
| num_observaciones_limpias 	| número de registros que fueron limpiados     	|
| status                    	| estatus de ejecución: Fallido, exitoso, etc. 	|

## Clean

| Nombre                     	| Función                                               	|
|----------------------------	|-------------------------------------------------------	|
| fecha                      	| fecha de ejecución                                    	|
| usuario                    	| quien ejecuto el task*                                	|
| tipo_columna               	| tipo de datos en cada columna                         	|
| ip_ec2                     	| donde se ejecuto                                      	|
| ejecucion                  	| imprimirá nombre de funciones del script de transform 	|
| num_observaciones_cargadas 	| número de registros modificados                       	|
| status                     	| estatus de ejecución: Fallido, exitoso, etc.          	|
