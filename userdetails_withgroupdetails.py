import  boto
from boto.iam.connection import IAMConnection
cfn = IAMConnection(aws_access_key_id='*',aws_secret_access_key ='*')
data = cfn.get_all_users()
for user in data.users:
    print (user,"\n")
group=cfn.get_groups_for_user("kousalya")
print (group)
