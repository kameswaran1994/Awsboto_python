import boto3
ec2_instance = boto3.resource('ec2',region_name = 'ap-south-1')
for i in ec2_instance.instances.all():
    print (i)
