import boto3
from decouple import config

# AWS credentials
aws_access_key_id = config('AWS_ACCESS_KEY_ID')
aws_secret_access_key = config('AWS_SECRET_ACCESS_KEY')
aws_region = 'us-east-1'

# EC2 instance ID
instance_id = config('EC2_INSTANCE_ID')

# Create EC2 client
ec2 = boto3.client('ec2',
                   aws_access_key_id=aws_access_key_id,
                   aws_secret_access_key=aws_secret_access_key,
                   region_name=aws_region)

# Start the instance
def start_instance():
    ec2.start_instances(InstanceIds=[instance_id])
    print(f'Starting EC2 instance {instance_id}')

# Stop the instance
def stop_instance():
    ec2.stop_instances(InstanceIds=[instance_id])
    print(f'Stopping EC2 instance {instance_id}')

if __name__ == '__main__':
    stop_instance()
