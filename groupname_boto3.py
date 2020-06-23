import boto3

iam = boto3.resource('iam')
group = iam.Group('name')
