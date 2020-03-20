# Arquitectura de Productos de Datos
## Proyecto - Retrasos en vuelos de la DB RITA


**Profesora:** Arquitectura de Productos de Datos

**Fecha:** 9 de febrero de 2020

**Integrantes del equipo:**

| # | Alumn@                            |
|---|-----------------------------------|
| 1 | Danahi Ayzailadema Ramos Martínez |
| 2 | Paola Mejía Domenzaín             |
| 3 | León Manuel Garay Vásquez         |
| 4 | Luis Eugenio Rojón Jiménez        |
| 5 | Cesar Zamora Martínez             |


***

### 1. Descripción del repositorio

El presente repositorio contiene los archivos asociados al proyecto de la materia de Arquitectura de Productos de Datos, el cual versa sobre la predicción de retraso o cancelación de los vuelos de la base de datos denominada conocida como [RITA](http://stat-computing.org/dataexpo/2009/the-data.html) (ver también [transtats.bts.gov](https://www.transtats.bts.gov/OT_Delay/OT_DelayCause1.asp)); esta agrupa una serie de datos de vuelos que incluyen salidas a tiempo, llegadas a tiempo, demoras, vuelos cancelados de todo Estados Unidos del Departamento de Transporte.

Cabe destacar que RITA posee una frecuencia de actualización mensual, con datos desde junio del 2003.

En este sentido, para facilitar el entendimiento de los documentos y acciones desarrolladas para llevar a cabo este proyecto, la información del repositorio se ha organizado en la estructura de carpetas que se resume en seguida:

| # | Carpeta                       | Descripción  |
|---|-----------------------------------|--------|
| 1 | Docs | Refiere la documentación de los pasos realizados para las diferentes etapas del proyecto. |
| 2 | Diseño | Contiene un documento *mock-up* con de la conceptualización del proyecto a realizar. |
| 3 | EDA | Análisis exploratorio preeliminar para identificar potenciales transformaciones. |
| 4 | ETL | Primera versión del ETL, considerando la etapa de Luigi. |
| 5 | sql | Contiene propuestas para hacer la carga a una base PostgreSQL de los datos desde csv. |
| 6 | Linaje | Presenta una serie de esquemas que describe tanto los metadatos que se recopilarán en las diferentes fases del proyecto, así como el linaje de los datos generados en cada una de dichas etapas. |


**Nota:** La estructura del repositorio y su contenido se irá actualizando conforme el equipo avance en el desarrollo del multi-citado proyecto.
