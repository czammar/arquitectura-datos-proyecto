import boto3

ses = boto3.session.Session(profile_name="dpa_Danahi_c", region_name='us-west-2')
s3 = ses.resource('s3')


bucket = s3.Bucket('test-aws-boto')
#  
bucket.objects.all().delete()
