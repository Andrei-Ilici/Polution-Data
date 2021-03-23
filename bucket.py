import os
import boto3


# Connect to the AWS S3 bucket using your account details
def connect_to_s3():
    s3=boto3.resource(
        service_name='s3',
        aws_access_key_id=os.getenv('AWS_ACCESS_KEY_ID'),
        aws_secret_access_key=os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    return s3


# This function is only used to test the connection to S3
# It lists the objects present in the bucket
def list_s3_objects(s3, bucket_name):
    text = 'Found the following files in the {bucket_name} bucket: '
    print(text.format(bucket_name=bucket_name))
    
    for obj in s3.Bucket(str(bucket_name)).objects.all():
        print(obj.key)
