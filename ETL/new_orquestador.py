
#! /Users/czammar/opt/anaconda3/bin/python
# existe un bug con bot3 y luigi para pasar las credenciales
# necesitas enviar el parametro AWS_PROFILE e indicar el profile
# con el que quieres que se corra
# PYTHONPATH='.' AWS_PROFILE=dpa luigi --module new_orquestador downloadDataS3 --local-scheduler --year 1988 --month 11
import luigi
import luigi.contrib.s3
from luigi import Event, Task, build # Utilidades para acciones tras un task exitoso o fallido
import boto3
import getpass # Usada para obtener el usuario
from datetime import date, datetime
import psycopg2
from psycopg2 import extras

#importamos las librerias
import requests
from io import BytesIO
from zipfile import ZipFile


usuario = getpass.getuser() # Obtenemos el usuario


#print(usuario)

def create_bucket():
    ses = boto3.session.Session(profile_name='dpa', region_name='us-west-2')
    s3_resource = ses.resource('s3')



    bucket_name = "test-aws-boto"

    s3_resource.create_bucket(Bucket=bucket_name,
                CreateBucketConfiguration={'LocationConstraint': 'us-west-2'},
                ACL='private')

#create_bucket():



# Preparamamos una clase para reunir los metadatos de la etapa Raw


class Linaje_raw():
    def __init__(self, fecha=0, parametros=0, usuario=0, ip_ec2=0, tamano_zip=0, nombre_archivo=0, ruta_s3=0,task_status=0):
        self.fecha = fecha # time stamp
        self.nombre_task = self.__class__.__name__#nombre_task
        self.parametros = parametros # ver si se obtiene como lista
        self.usuario = usuario # Usuario de la maquina de GNU/Linux que corre la instancia
        self.ip_ec2 = ip_ec2
        self.tamano_zip = tamano_zip
        self.nombre_archivo = nombre_archivo
        self.ruta_s3= ruta_s3
        self.task_status= task_status

    def to_upsert(self):
        return (self.fecha, self.nombre_task, self.parametros, self.usuario, self.ip_ec2, self.tamano_zip, self.nombre_archivo, self.ruta_s3, self.task_status)

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
    MiLinaje.fecha =  datetime.now()
    MiLinaje.usuario = getpass.getuser()



    def run(self):
        MiLinaje.parametros = 'Year='+str(self.year)+'-'+'Month='+str(self.month)

        # Autenticación en S3
        ses = boto3.session.Session(profile_name='dpa', region_name='us-west-2')
        s3_resource = ses.resource('s3')


        ec2 = ses.client('ec2')
        MiLinaje.ip_ec2 = ec2.describe_addresses(Filters=[{'Name': 'domain','Values': ['standard']}])

        obj = s3_resource.Bucket("test-aws-boto")
        print(ses)

        #Formamos url_act que es el url actualizado
        url_act = self.BASE_URL+str(self.year)+"_"+str(self.month)+".zip"

        #Leemos los datos de la API, relativos al archivo en formato zip del periodo en cuestion
        r=requests.get(url_act)
        data=r.content # resultado de la peticion a la API de Rita, en binario

        # Escribimos el archivo al bucket
        output_path = "s3://test-aws-boto/YEAR="+str(self.year)+"/MONTH="+str(self.month)+"/"+str(self.year)+"_"+str(self.month)+".zip"

        # Guardamos las rutas
        MiLinaje.ruta_s3 = "s3://test-aws-boto/YEAR="+str(self.year)+"/MONTH="+str(self.month)+"/"
        MiLinaje.nombre_archivo =  str(self.year)+"_"+str(self.month)+".zip"# Pendiente

        obj.put_object(Key=output_path,Body=r.content)

    def output(self):
        # Ruta en donde se guarda el archivo solicitado
        output_path = "s3://test-aws-boto/YEAR="+str(self.year)+"/MONTH="+str(self.month)+"/"+str(self.year)+"_"+str(self.month)+".zip"

        return luigi.contrib.s3.S3Target(path=output_path)

 # Decoradores para escribir el status del task
@downloadDataS3.event_handler(Event.SUCCESS)
def on_success(self):

    # Cambiamos statius del task a exitoso
    MiLinaje.task_status = "Successful"

    # Escribimos el tamano del archivo recien escrito
    ses = boto3.session.Session(profile_name="dpa", region_name='us-west-2')
    s3 = ses.resource('s3')
    bucket_name = "test-aws-boto"
    my_bucket = s3.Bucket(bucket_name)

    MiLinaje.tamano_zip = my_bucket.Object(key=MiLinaje.ruta_s3+MiLinaje.nombre_archivo).content_length


    import psycopg2

    host="rita-db.clx22b04cf2j.us-west-2.rds.amazonaws.com"

    connection = psycopg2.connect(user="postgres", # Usuario RDS
                                  password="i8cOE6l7bntarIEWfxAu", # password de usuario de RDS
                                  host=host,#"127.0.0.1", # cambiar por el endpoint adecuado
                                  port="5432", # cambiar por el puerto
                                  database="postgres") # Nombre de la base de datos


    cursor = connection.cursor()
    postgres_insert_query = """ INSERT INTO metadatos.extract (fecha, nombre_task, parametros, usuario, ip_ec2, tamano_zip, nombre_archivo, ruta_s3, task_status) VALUES ( %s, %s, %s, %s, %s, %s, %s, %s, %s ) """
    record_to_insert = MiLinaje.to_upsert() #(5, 'One Plus 6', 950, 'some_spec')
    cursor.execute(postgres_insert_query, record_to_insert)
    connection .commit()
    cursor.close()
    connection.close()
    print("PostgreSQL connection is closed")


@downloadDataS3.event_handler(Event.FAILURE)
def on_failure(self):
    MiLinaje.tamano_zip = "Failure"
    MiLinaje.task_status = "Unknown"
    MiLinaje.to_upsert()
