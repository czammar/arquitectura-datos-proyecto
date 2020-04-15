import boto3

ses = boto3.session.Session(profile_name="educate1", region_name='us-east-1')
s3 = ses.resource('s3')


bucket = s3.Bucket('test-aws-boto')

total_size = 0
for k in bucket.objects.all():
    total_size = k.size
    print(k.size)
