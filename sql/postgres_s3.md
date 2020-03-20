aws_s3.table_import_from_s3 (
   table_name text, 
   column_list text, 
   options text, 
   bucket text, 
   file_path text, 
   region text, 
   access_key text, 
   secret_key text, 
   session_token text 
) 




import time

import boto3
import botocore


def main():
    db_identifier = 'yourDBID'
    rds = boto3.client('rds')
    try:
        rds.create_db_instance(DBInstanceIdentifier=db_identifier,
                               AllocatedStorage=200,
                               DBName='yourdbname',
                               Engine='postgres',
                               # General purpose SSD
                               StorageType='gp2',
                               StorageEncrypted=True,
                               AutoMinorVersionUpgrade=True,
                               # Set this to true later?
                               MultiAZ=False,
                               MasterUsername='youruser',
                               MasterUserPassword='yourpassword',
                               VpcSecurityGroupIds=['YOUR_SECURITY_GROUP_ID'],
                               DBInstanceClass='db.m3.2xlarge',
                               Tags=[{'Key': 'MyTag', 'Value': 'Hawaii'}])
        print 'Starting RDS instance with ID: %s' % db_identifier
    except botocore.exceptions.ClientError as e:
        if 'DBInstanceAlreadyExists' in e.message:
            print 'DB instance %s exists already, continuing to poll ...' % db_identifier
        else:
            raise


    running = True
    while running:
        response = rds.describe_db_instances(DBInstanceIdentifier=db_identifier)

        db_instances = response['DBInstances']
        if len(db_instances) != 1:
            raise Exception('Whoa cowboy! More than one DB instance returned; this should never happen')

        db_instance = db_instances[0]

        status = db_instance['DBInstanceStatus']

        print 'Last DB status: %s' % status

        time.sleep(5)
        if status == 'available':
            endpoint = db_instance['Endpoint']
            host = endpoint['Address']
            # port = endpoint['Port']

            print 'DB instance ready with host: %s' % host
            running = False


if __name__ == '__main__':
    main()
