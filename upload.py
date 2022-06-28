
import os
from dotenv import load_dotenv
import boto3

load_dotenv()  # take environment variables from .env

#Creating Session With Boto3.
session = boto3.Session()
#Creating S3 Resource From the Session.
s3 = session.resource('s3')
txt_data = b'This is the content of the file uploaded from python boto3!!!'

bucket = os.getenv('BUCKET', 'cor-local')

print(bucket)

object = s3.Object(bucket, 'test_python.txt')
result = object.put(Body=txt_data)

print("Done!")

