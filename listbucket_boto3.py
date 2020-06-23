import boto3
object_s3 = boto3.resource('s3',aws_access_key_id='*',aws_secret_access_key ='*')
for output in object_s3.buckets.all():
    print (output)
