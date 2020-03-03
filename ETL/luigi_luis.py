#! /Users/czammar/opt/anaconda3/bin/python
# existe un bug con bot3 y luigi para pasar las credenciales
# necesitas enviar el parámetro AWS_PROFILE e indicar el profile
# con el que quieres que se corra
# PYTHONPATH='.' AWS_PROFILE=dpa luigi --module orquestador S3Task --local-scheduler ...
import luigi
import luigi.contrib.s3
import boto3
import os
import pyarrow
import pyarrow.parquet as pq

#importamos las librerias
import requests
import wget
import zipfile
#librerias para pasar a parquet
import pandas as pd
import pyarrow as pa


class LocalFileSystemTask(luigi.Task):

    def run(self):
        with self.output().open('w') as output_file:
        	extract = exec(open('download_rita_parquet.py').read())

    def output(self):
        return luigi.local_target.LocalTarget('On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_1987_10.csv')



class S3Task(luigi.Task):

    #Parametros
    task_name = "load"

    def requires(self):
        return LocalFileSystemTask()

    def run(self):
        ses = boto3.session.Session(profile_name='dpa', region_name='us-west-2')
        s3_resource = ses.resource('s3')

        bucket_name = "test-aws-boto"
        obj = s3_resource.Bucket("test-aws-boto")
        print(ses)

        file_to_upload = 'On_Time_Reporting.parquet'
        file_name = file_to_upload

        # accedemos a client desde el resource
        s3_resource.meta.client.upload_file(file_to_upload, bucket_name, file_name)


    def output(self):
        output_path = "s3://test-aws-boto/On_Time_Reporting.parquet"

        return luigi.contrib.s3.S3Target(path=output_path)
