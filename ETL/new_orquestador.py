
#! /Users/czammar/opt/anaconda3/bin/python
# existe un bug con bot3 y luigi para pasar las credenciales
# necesitas enviar el parámetro AWS_PROFILE e indicar el profile
# con el que quieres que se corra
# PYTHONPATH='.' AWS_PROFILE=dpa_Danahi_c luigi --module new_orquestador downloadDataS3 --local-scheduler --year 1988 --month 11
import luigi
import luigi.contrib.s3
import boto3
import getpass # Usada para obtener el usuario

#importamos las librerias
import requests
from io import BytesIO
from zipfile import ZipFile


usuario = getpass.getuser() # Obtenemos el usuario


#print(usuario)

def create_bucket():
    ses = boto3.session.Session(profile_name='dpa_Danahi_c', region_name='us-west-2')
    s3_resource = ses.resource('s3')

    bucket_name = "test-aws-boto"

    s3_resource.create_bucket(Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': 'us-west-2'},
                ACL='private')

#create_bucket():



# Preparamamos una clase para reunir los metadatos de la etapa Raw


class Linaje_raw():
    def __init__(self, fecha=0, nombre_task=0, parametros=0, usuario=0, ip_ec2=0, tamano_zip=0, nombre_archivo=0, ruta_s3=0):
        self.fecha = fecha # time stamp
        self.nombre_task = nombre_task
        self.parametros = parametros # ver si se obtiene como lista
        self.usuario = usuario # Usuario de la maquina de GNU/Linux que corre la instancia
        self.ip_ec2 = ip_ec2
        self.tamano_zip = tamano_zip
        self.nombre_archivo = nombre_archivo
        self.ruta_s3= ruta_s3

    def to_upsert(self):
        print (self.fecha, self.nombre_task, self.parametros, self.usuario, self.ip_ec2, self.tamano_zip, self.nombre_archivo, self.ruta_s3)

# Inicializamos
MiLinaje = Linaje_raw()

#MiLinaje.to_upsert()



class downloadDataS3(luigi.Task):
    #Definimos los URL base para poder actualizarlo automaticamente despues
    BASE_URL="https://transtats.bts.gov/PREZIP/On_Time_Reporting_Carrier_On_Time_Performance_1987_present_"

    #Definimos el mes y el anio base
    year = luigi.Parameter()
    month = luigi.Parameter()

    # Intentamos recoger parametros
    MiLinaje.fecha = "Ya tengo hambre :("#luigi.Parameter().parse(year)# :D :D :D
    MiLinaje.usuario = getpass.getuser()
    MiLinaje.to_upsert()

    def run(self):
        # Autenticación en S3
        ses = boto3.session.Session(profile_name='dpa_Danahi_c', region_name='us-west-2')
        s3_resource = ses.resource('s3')

        obj = s3_resource.Bucket("test-aws-boto")
        print(ses)

        #Formamos url_act que es el url actualizado
        url_act = self.BASE_URL+str(self.year)+"_"+str(self.month)+".zip"

        #Leemos los datos de la API, relativos al archivo en formato zip del periodo en cuestion
        r=requests.get(url_act)
        data=r.content # resultado de la peticion a la API de Rita, en binario

        # Escribimos el archivo al bucket
        output_path = "s3://test-aws-boto/YEAR="+str(self.year)+"/MONTH="+str(self.month)+"/"+str(self.year)+"_"+str(self.month)+".zip"
        obj.put_object(Key=output_path,Body=r.content)

    def output(self):
        # Ruta en donde se guarda el archivo solicitado
        output_path = "s3://test-aws-boto/YEAR="+str(self.year)+"/MONTH="+str(self.month)+"/"+str(self.year)+"_"+str(self.month)+".zip"

        return luigi.contrib.s3.S3Target(path=output_path)


class WritingCSVtoS3(luigi.Task):

    #Parametros
    task_name = "load"
    #Definimos el mes y el anio base
    year = luigi.Parameter()
    month = luigi.Parameter()

    #def requires(self):
        #return downloadDataS3()

    def run(self):

        zip_key = "s3://test-aws-boto/YEAR="+str(self.year)+"/MONTH="+str(self.month)+"/"+str(self.year)+"_"+str(self.month)+".zip"

        ses = boto3.session.Session(profile_name='dpa_Danahi_c', region_name='us-west-2')
        s3_resource = ses.resource('s3')

        bucket_name = "test-aws-boto"
        obj = s3_resource.Bucket("test-aws-boto")
        print(ses)

        # hola
        s3_resource = boto3.resource('s3')
        zip_obj = s3_resource.Object(bucket_name=bucket_name, key=zip_key)
        buffer = BytesIO(zip_obj.get()["Body"].read())

        z = ZipFile(buffer)

        zip_name="On_Time_Reporting_Carrier_On_Time_Performance_(1987_present)_"+str(self.year)+"_"+str(self.month)+".csv"

        s3_resource.meta.client.upload_fileobj(z.open(zip_name), Bucket=bucket_name, Key=f'{zip_name}')


    def output(self):
        output_path = "s3://test-aws-boto/YEAR="+str(self.year)+"/MONTH="+str(self.month)+"/"+str(self.year)+"_"+str(self.month)+".zip"

        return luigi.contrib.s3.S3Target(path=output_path)
