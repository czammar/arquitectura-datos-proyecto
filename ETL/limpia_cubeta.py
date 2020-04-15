import boto3

ses = boto3.session.Session(profile_name="educate1", region_name='us-east-1')
s3 = ses.resource('s3')

# listar los buckets que están en este perfil y región.
for bucket in s3.buckets.all():
    print(bucket.name)

bucket_name = "test-aws-boto"
my_bucket = s3.Bucket(bucket_name )
for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object)

file_name = "On_Time_Reporting.parquet"
s3.Object(bucket_name, file_name).delete()

for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object)

s3.Bucket(bucket_name).delete()

# listar los buckets que están en este perfil y región.
for bucket in s3.buckets.all():
    print(bucket.name)
