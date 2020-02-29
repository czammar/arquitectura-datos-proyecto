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

class LocalFileSystemTask(luigi.Task):
#Parametros


    def run(self):
        with self.output().open('w') as output_file:
        	extract = exec(open('download_rita_parquet.py').read())
        	#output_file.open(extract)

    def output(self):
        return luigi.local_target.LocalTarget('./On_Time_Reporting.parquet')


class S3Task(luigi.Task):

    #Parametros
    task_name = "load"

    def requires(self):
        return LocalFileSystemTask()

    def run(self):
        ses = boto3.session.Session(profile_name='dpa', region_name='us-west-2')
        s3_resource = ses.resource('s3')

        obj = s3_resource.Bucket("test-aws-boto")
        print(ses)

        #with self.output().open('w') as output_file:
        	#file =  pq.read_table('On_Time_Reporting.parquet')
            #output_file.write("raw,luigi,s3")

        with self.output().open('w') as output_file:
            output_file.write("On_Time_Reporting,luigi,s3")


    def output(self):
        output_path = "s3://test-aws-boto/On_Time_Reporting.parquet"

        return luigi.contrib.s3.S3Target(path=output_path)
