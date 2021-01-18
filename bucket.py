import os
import boto3

def connect_to_s3():
    s3 = boto3.resource(
    service_name = 's3',
    aws_access_key_id = os.getenv('AWS_ACCESS_KEY_ID'),
    aws_secret_access_key = os.getenv('AWS_SECRET_ACCESS_KEY')
    )
    return s3

def list_s3_objects(s3):
    bucket_name = os.getenv('AWS_BUCKET_NAME')
    for obj in s3.Bucket('development-test-bucket1').objects.all():
        print(obj.key)