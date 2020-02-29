#! /home/vagrant/.pyenv/shims/python
# existe un bug con bot3 y luigi para pasar las credenciales
# necesitas enviar el parámetro AWS_PROFILE e indicar el profile
# con el que quieres que se corra
# PYTHONPATH='.' AWS_PROFILE=dpa luigi --module orquestador.py S3Task --local-scheduler ...
import luigi
import luigi.contrib.s3
import boto3
import os

class LocalFileSystemTask(luigi.Task):
#Parametros 


    def run(self):
        with self.output().open('w') as output_file:
        	extract = exec(open('calling_bash.py').read())
        	output_file.write(extract)
        


    def output(self):
        return luigi.local_target.LocalTarget('./On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_1987_10.csv')


class S3Task(luigi.Task):

    #Parametros
    task_name = "load"

    bucket = luigi.Parameter()
    root_path = luigi.Parameter()
    etl_path = luigi.Parameter()
    year = luigi.Parameter()
    month = luigi.Parameter()

    def requires(self):
        return LocalFileSystemTask(self)

    def run(self):
        ses = boto3.session.Session(profile_name="dpa", region_name='us-west-2')
        s3_resource = ses.resource('s3')

        obj = s3_resource.Bucket(self.bucket)
        print(ses)

        with self.output().open('w') as output_file:
            output_file.write("raw,luigi,s3")


    def output(self):
        output_path = "s3://{}/{}/{}/{}/YEAR={}/MONTH={}/raw.csv".\
        format(self.bucket,
        self.root_path,
        self.etl_path,
        self.task_name,
        self.year,
        str(self.month))

        #return luigi.local_target.LocalTarget('/home/silil/Documents/itam/metodos_gran_escala/data-product-architecture/luigi/test.csv')
        return luigi.contrib.s3.S3Target(path=output_path)