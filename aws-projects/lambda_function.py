import boto3

# Enter the region your instances are in. Include only the region without specifying Availability Zone; e.g., 'us-east-1'
region = 'us-east-1'

# Get the specific EC2 instance in a region.
ec2 = boto3.client('ec2', region_name=region)

# Define the instancelist
instancelist = []

# Get the EC2 instances with Tag Name Scheduler and Value True
response = ec2.describe_instances(
        Filters=[
            {
                'Name':'tag:Scheduler',
                'Values': ['True']

            }])

# Append InstanceIds in instancelist
for reservation in (response["Reservations"]):
        for instance in reservation["Instances"]:
            instancelist.append(instance["InstanceId"])

# Stop the EC2 instances in instancelist
ec2.stop_instances(InstanceIds=instancelist)
print ('Stopped your instances: ' + str(instancelist))
