
import os
from threading import currentThread
from dotenv import load_dotenv
import boto3
import time

load_dotenv()  # take environment variables from .env

currentTime = time.strftime('%a, %d %b %Y %H:%M:%S %Z(%z)')

#Creating Session With Boto3.
session = boto3.Session()
#Creating S3 Resource From the Session.
s3 = session.resource('s3')
txt_data = 'This is the content of the file uploaded from python boto3: ' + currentTime

bucket = os.getenv('BUCKET', 'cor-local')

print(bucket)

company_id = os.getenv('COMPANY_ID', 000)
print("company_id: " + company_id) 

object = s3.Object(bucket, 'poc-python/test_python.txt')
result = object.put(Body=txt_data)

print("Done!")

