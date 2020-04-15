# librerias para CopyToTable
# Requiere correr previamente: luigid --port 8082
from luigi.contrib.postgres import CopyToTable

import pandas as pd
import luigi
import psycopg2

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
            ("year","VARCHAR"),\
            ("month","VARCHAR"),\
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

def EL_verif_query(url):
    # Conexion a BD y query para verificacion
    # Lectura de archivo de credenciales en directorio (no subirlo a git)
    credentials = pd.read_csv("postgres_credentials.csv")
    user = credentials.user[0]
    password = credentials.password[0]
    database = credentials.database[0]
    host = credentials.host[0]

    # Conexion y cursor para query
    connection = psycopg2.connect(user=user, # Usuario RDS
                                 password=password, # password de usuario de RDS
                                 host=host,# endpoint
                                 port="5432", # cambiar por el puerto
                                 database=database) # Nombre de la base de datos
    cursor = connection.cursor()

    # Query para verificacion a la base de datos
    postgreSQL_select_Query = "SELECT * from metadatos.extract WHERE task_status = '" + str(url) + "';"
    cursor.execute(postgreSQL_select_Query)
    print("Query de verificacion")
    select_Query = cursor.fetchall()
    tam = len(select_Query)
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")

    return tam

def EL_metadata(record_to_insert):

    # Lectura de archivo de credenciales en directorio (no subirlo a git)
    credentials = pd.read_csv("postgres_credentials.csv")
    user = credentials.user[0]
    password = credentials.password[0]
    database = credentials.database[0]
    host = credentials.host[0]

    connection = psycopg2.connect(user=user, # Usuario RDS
                                 password=password, # password de usuario de RDS
                                 host=host,# endpoint
                                 port="5432", # cambiar por el puerto
                                 database=database) # Nombre de la base de datos
    cursor = connection.cursor()

    # Query para insertar metadatos
    postgres_insert_query = """ INSERT INTO metadatos.extract (fecha, nombre_task, year, month, usuario, ip_ec2, tamano_zip, nombre_archivo, ruta_s3, task_status) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s, %s ) """
    cursor.execute(postgres_insert_query, record_to_insert)
    connection .commit()
    cursor.close()
    connection.close()

    return print("Metadadata Insertion Done - PostgreSQL connection is closed")
