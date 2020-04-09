# librerias para CopyToTable
# Requiere correr previamente: luigid --port 8082
from luigi.contrib.postgres import CopyToTable

import pandas as pd
import luigi

class InsertExtractMetada(CopyToTable):
    '''
    Task de luigi para insertar renglones en renglones en tabla de metadatos
    de la extraccion y load de metadatos a S3
    '''

    # Lectura de archivo de credenciales en directorio (no subirlo a git)
    credentials = pd.read_csv("postgres_credentials.csv")
    user = credentials.user[0]
    password = credentials.password[0]
    database = credentials.database[0]
    host = credentials.host[0]

    # Nombre de tabla donde se inserta info. Notas:
    # 1) si la tabla (sin esquema) no existe, luigi la crea con esquema publico,
    # 2) si el esquema de la tabla no existe, luigi devuelve error :(
    table = 'metadatos.extract'

    # Estructura de las columnas que integran la tabla (ver esquema)
    columns = [("fecha", "VARCHAR"),\
            ("nombre_task", "VARCHAR"),\
            ("parametros","VARCHAR"),\
            ("usuario","VARCHAR"),\
            ("ip_ec2","VARCHAR"),\
            ("tamano_zip","VARCHAR"),\
            ("nombre_archivo","VARCHAR"),\
            ("ruta_s3","VARCHAR"),\
            ("task_status", "VARCHAR")]

    def rows(self):
        # Funcion para insertar renglones en tabla

        # Renglon o renglones (separados por coma) a ser insertado
        r = [MiLinaje.to_upsert()]

        # Insertamos renglones en tabla
        for element in r:
            yield element
