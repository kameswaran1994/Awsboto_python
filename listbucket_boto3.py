import boto3
object_s3 = boto3.resource('s3')
for output in object_s3.buckets.all():
    print (output)
