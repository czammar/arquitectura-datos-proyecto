import boto3

ses = boto3.session.Session(profile_name="dpa", region_name='us-west-2')
s3 = ses.resource('s3')

# listar los buckets que están en este perfil y región.
for bucket in s3.buckets.all():
    print(bucket.name)

bucket_name = "test-aws-boto"
my_bucket = s3.Bucket(bucket_name )
for my_bucket_object in my_bucket.objects.all():
    print(my_bucket_object, my_bucket_object.size)

#tam = my_bucket.Object(key='1988_10.zip').content_length
#print(tam)
