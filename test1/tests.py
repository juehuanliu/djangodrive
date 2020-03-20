from django.test import TestCase

# Create your tests here.
import boto3

# Let's use Amazon S3
s3 = boto3.resource('s3')
for bucket in s3.buckets.all():
    print(bucket.name)

data = open('test.txt', 'rb')
s3.Bucket('cloudjuehuanliudjango').put_object(Key='test.txt', Body=data)