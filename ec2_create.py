import boto3
kames_ec2 = boto3.resource('ec2',region_name='ap-south-1')
# create a file to store the key locally
outfile = open('ec2-keypair2.pem','w')

# call the boto ec2 function to create a key pair
key_pair = kames_ec2.create_key_pair(KeyName='ec2-keypair2')

# capture the key and store it in a file
KeyPairOut = str(key_pair.key_material)
print(KeyPairOut)
outfile.write(KeyPairOut)
instances = kames_ec2.create_instances(
     ImageId='ami-0b44050b2d893d5f7',
     MinCount=1,
     MaxCount=int(input("Enter the instance you need:")),
     InstanceType='t2.micro',
     KeyName='ec2-keypair'
 )

