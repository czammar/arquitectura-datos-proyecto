
#! /Users/czammar/opt/anaconda3/bin/python
# existe un bug con bot3 y luigi para pasar las credenciales
# necesitas enviar el parámetro AWS_PROFILE e indicar el profile
# con el que quieres que se corra
# PYTHONPATH='.' AWS_PROFILE=dpa luigi --module orquestador downloadDataS3 --local-scheduler ...
import luigi
import luigi.contrib.s3
import boto3

#importamos las librerias
import requests

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

        #Formamos url_act que es el url actualizado
        url_act = self.BASE_URL+str(self.YEAR)+"_"+str(self.MONTH)+".zip"
        
        #Leemos los datos de la API, relativos al archivo en formato zip del periodo en cuestion
        r=requests.get(url_act)

        # Escribimos el archivo al bucket
        # Nota: r.content es el resultado de la peticion a la API de Rita, en binario
        obj.put_object(Key=str(self.YEAR)+"_"+str(self.MONTH)+".zip",Body=r.content)

    def output(self):
        # Ruta en donde se guarda el archivo solicitado
        output_path = "s3://test-aws-boto/" + str(self.YEAR)+"_"+str(self.MONTH)+".zip"
        return luigi.contrib.s3.S3Target(path=output_path)
