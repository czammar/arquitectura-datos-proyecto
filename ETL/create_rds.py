#CLASE MASTER DE AWS

import boto3
from botocore.config import Config
import boto3
import botocore
import sys
import random
import time
import os

# GLOBALS
os.environ['AWS_PROFILE'] = "dpa"
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
             "port":5432
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
describe_db()
#create_db("metadatos")
delete_db('metadatos')
describe_db()
#create_db()
#describe_db()
