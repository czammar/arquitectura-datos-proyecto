#CLASE MASTER DE AWS

from botocore.config import Config
import boto3
#import botocore
import sys
import random
import time
import os

# GLOBALS
os.environ['AWS_PROFILE'] = "dpa_Danahi_c"
os.environ['AWS_DEFAULT_REGION'] = "us-west-2"
boto_config = Config(retries=dict(max_attempts=20))
rds_client = boto3.client('rds',config=boto_config, region_name='us-west-2')

#METHODS
# get all of the db instances
def describe_db():
    try:
        dbs = rds_client.describe_db_instances()
        #print(dbs['DBInstances'])
        for db in dbs['DBInstances']:
            print(db)
            print ("User name: ", db['MasterUsername'], \
            ", Endpoint: ", db['Endpoint'],    \
            ", Address: ", db['Endpoint']['Address'],    \
            ", Port: ", db['Endpoint']['Port'],       \
            ", Status: ", db['DBInstanceStatus'],     \
            ", ID =", db['DBInstanceIdentifier'] )
    except Exception as error:
        print (error)

def create_db(nuevo_id):
    try:
        db_vars = {
            "DBInstanceIdentifier":nuevo_id,
             "MasterUsername":'dpa',
             "MasterUserPassword":'dpa01_largo',
             "DBInstanceClass":'db.t2.micro',
             "Engine":'postgres',
             "AllocatedStorage":5,
             "Port":5432#,
             #"DBName":'metadatos'
        }
        rds_client.create_db_instance(**db_vars)
    except Exception as error:
        print(error)

def delete_db(id_borrar):
    try:
        response = rds_client.delete_db_instance(
        DBInstanceIdentifier=id_borrar,
        SkipFinalSnapshot=True)
        print (response)
    except Exception as error:
        print (error)

# MAIN

#create_db('metadatos')
#describe_db()
#delete_db('metadatos')
#delete_db('postgres')
#describe_db()
#create_db()
#describe_db()

print("*************  Informacion relevante  *************")
dbs = rds_client.describe_db_instances()
host=dbs['DBInstances'][0].get('Endpoint').get('Address')
port=dbs['DBInstances'][0].get('Endpoint').get('Port')

# Obtiene Endpoint de la base de datos
#print (dbs['DBInstances'][0].get('Endpoint').get('Address'))
# Obtiene Port de la base de datos
#print (dbs['DBInstances'][0].get('Endpoint').get('Port'))

import psycopg2


connection = psycopg2.connect(user="dpa", # Usuario RDS
                              password="dpa01_largo", # password de usuario de RDS
                              host=host,#"127.0.0.1", # cambiar por el endpoint adecuado
                              port="5432", # cambiar por el puerto
                              database="postgres") # Nombre de la base de datos


cursor = connection.cursor()
postgreSQL_select_Query = "CREATE TABLE extract( fecha DATE, parametros CHAR(30), usuario CHAR(20),\
  ip_ec2 CHAR(20), num_renglones CHAR(10), nombre_archivo CHAR(20),\
  ruta_s3 CHAR(30), variable_datos CHAR(30) )"

cursor.execute(postgreSQL_select_Query)
cursor.close()
connection.close()
print("PostgreSQL connection is closed")