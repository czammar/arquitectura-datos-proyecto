
#! /Users/czammar/opt/anaconda3/bin/python
# existe un bug con bot3 y luigi para pasar las credenciales
# necesitas enviar el parámetro AWS_PROFILE e indicar el profile
# con el que quieres que se corra
# PYTHONPATH='.' AWS_PROFILE=dpa luigi --module orquestador S3Task --local-scheduler ...
import luigi
import luigi.contrib.s3
import boto3
import os
#import pyarrow
#import pyarrow.parquet as pq

#importamos las librerias
import requests
#import wget
#import zipfile
#librerias para pasar a parquet
#import pandas as pd
#import pyarrow as pa

def create_bucket():
    ses = boto3.session.Session(profile_name='dpa_Danahi_c', region_name='us-west-2')
    s3_resource = ses.resource('s3')

    bucket_name = "test-aws-boto"

    s3_resource.create_bucket(Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': 'us-west-2'},
                ACL='private')

#create_bucket()

class downloadDataS3(luigi.Task):
    #Definimos los URL base para poder actualizarlo automaticamente despues
    BASE_URL="https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_"

    #Definimos el mes y el anio base
    YEAR=1988
    MONTH=10

    def run(self):
        # Autenticación en S3
        ses = boto3.session.Session(profile_name='dpa_Danahi_c', region_name='us-west-2')
        s3_resource = ses.resource('s3')

        obj = s3_resource.Bucket("test-aws-boto")
        print(ses)
        # Autenticación del cliente:

        #Definimos los URL base para poder actualizarlo automaticamente despues
        #BASE_URL="https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_"

        #Definimos el mes y el anio base
        #YEAR=1988
        #MONTH=10

        #url_act es el url actualizado
        url_act = self.BASE_URL+str(self.YEAR)+"_"+str(self.MONTH)+".zip"
        #descargamos el archivo en formato zip
        r=requests.get(url_act)

        obj.put_object(Key=str(self.YEAR)+"_"+str(self.MONTH)+".zip",Body=r.content)

    def output(self):
        output_path = "s3://test-aws-boto/" + str(self.YEAR)+"_"+str(self.MONTH)+".zip"
        return luigi.contrib.s3.S3Target(path=output_path)
