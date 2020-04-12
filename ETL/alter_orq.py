# PYTHONPATH='.' AWS_PROFILE=dpa luigi --module alter_orq downloadDataS3 --local-scheduler
import luigi
import luigi.contrib.s3
from luigi import Event, Task, build # Utilidades para acciones tras un task exitoso o fallido
import boto3
import getpass # Usada para obtener el usuario
from datetime import date, datetime
import psycopg2
from psycopg2 import extras
import socket #import publicip
import requests
from io import BytesIO
from zipfile import ZipFile
import os
from luigi.contrib.postgres import CopyToTable #luigid --port 8082
import pandas as pd
from task_insert_extract_metadata_luigi_postgres import InsertExtractMetada, EL_verif_query, EL_metadata

# Preparamamos una clase para reunir los metadatos de la etapa Raw
class Linaje_raw():
    def __init__(self, url = 0, fecha=0, year=0, month=0, usuario=0, ip_ec2=0, tamano_zip=0, nombre_archivo=0, ruta_s3=0,task_status=0):
        self.url = url
        self.fecha = fecha # time stamp
        self.nombre_task = self.__class__.__name__#nombre_task
        self.year = year #
        self.month = month #
        self.usuario = usuario # Usuario de la maquina de GNU/Linux que corre la instancia
        self.ip_ec2 = ip_ec2
        self.tamano_zip = tamano_zip
        self.nombre_archivo = nombre_archivo
        self.ruta_s3= ruta_s3
        self.task_status= task_status

    def to_upsert(self):
        return (self.fecha, self.nombre_task, self.year, self.month, self.usuario,\
         self.ip_ec2, self.tamano_zip, self.nombre_archivo, self.ruta_s3,\
          self.task_status)

# Inicializamos la clase que reune los metadatos
MiLinaje = Linaje_raw()

# Tasks de Luigi
class downloadDataS3(luigi.Task):
    #Definimos los URL base para poder actualizarlo automaticamente despues
    BASE_URL="https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_"

    # Recolectamos fecha y usuario para metadatos
    MiLinaje.fecha =  datetime.now()
    MiLinaje.usuario = getpass.getuser()

    def run(self):

        # Obtiene anio y mes correspondiente fecha actual de ejecucion del script
        now = datetime.datetime.now()
        current_year = now.year
        current_month = now.month

        # Obtiene anio y mes base (tres anios hacia atras)
        base_year = current_year - 3
        base_month = current_month

        # Recolectamos parametros de mes y anio de solicitud descarga a API Rita para metadatos
        MiLinaje.year = str(base_year)
        MiLinaje.month = str(base_month)

        # Recolectamos IP para metadatos
        MiLinaje.ip_ec2 = str(socket.gethostbyname(socket.gethostname()))

        for anio in reversed(range(base_year,current_year+1)):
            for mes in reversed(range(1,12+1)):

                # Verificamos si en metadatos ya hay registro de esta anio y mes
                # En caso contario, se intenta descarga
                tam = EL_verif_query()

                if tam == 0:

                    #Leemos los datos de la API en binario, relativos al archivo en formato zip del periodo en cuestion
                    url_act = self.BASE_URL+str(anio)+"_"+str(mes)+".zip" #url actualizado
                    r=requests.get(url_act)

                    if r.status_code == 200:

                        data=r.content # Peticion a la API de Rita, en binario

                        ## Escribimos los archivos que se consultan al API Rita en S3
                        # Autenticación en S3 con boto3
                        ses = boto3.session.Session(profile_name='dpa', region_name='us-west-2')
                        s3_resource = ses.resource('s3')
                        obj = s3_resource.Bucket("test-aws-boto")
                        print(ses)

                        # Escribimos el archivo al bucket, usando el binario
                        output_path = "RITA/YEAR="+str(anio)+"/"+str(anio)+"_"+str(mes)+".zip"
                        obj.put_object(Key=output_path,Body=r.content)`

                        # Recolectamos nombre del .zip y path con el que se guardara consulta a
                        # API de Rita en S3 para metadatos
                        MiLinaje.ruta_s3 = "s3://test-aws-boto/"+"RITA/YEAR="+str(self.year)+"/"
                        MiLinaje.nombre_archivo =  str(anio)+"_"+str(mes)+".zip"

                        # Recolectamos tamano del archivo recien escrito en S3 para metadatos
                        ses = boto3.session.Session(profile_name="dpa", region_name='us-west-2')
                        s3 = ses.resource('s3')
                        bucket_name = "test-aws-boto"
                        my_bucket = s3.Bucket(bucket_name)
                        MiLinaje.tamano_zip = my_bucket.Object(key=MiLinaje.ruta_s3+MiLinaje.nombre_archivo).content_length

                        # Recolectamos tatus para metadatos
                        MiLinaje.task_status = "Successful"

                        # Insertamos metadatos a DB
                        #InsertExtractMetada()
                        EL_metadata()


        os.system('echo OK > Tarea_EL.txt')

    def output(self):
        # Ruta en donde se guarda el archivo solicitado
        output_path = "Tarea_EL.txt"
        return luigi.LocalTarget(output_path)