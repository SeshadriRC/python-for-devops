```python
# Assume file name is test.py, After completing below code, just run `py test.py`. Below code will create a S3 bucket
import boto3

client = boto3.client('s3')

response = client.create_bucket(
    Bucket='sesha-demo-bucket-boto3',
    CreateBucketConfiguration={   
        'LocationConstraint': 'ap-south-1'
    }
)

# Get ACL

response = client.get_bucket_acl(
    Bucket='sesha-demo-bucket-boto3',
)

print (response)  # Output will be in the format of Json, so we need to convert that to Dictionary , so that we can read the value


```

<img width="1919" height="983" alt="image" src="https://github.com/user-attachments/assets/330664e4-c5f4-4b92-a807-24d8d7cfae67" />
