from urllib.parse import urlparse
import boto3


def split_s3_path(s3_path):
    x = urlparse(s3_path.strip())
    print(x)
    return x.netloc, x.path[1:]


def copy_to_s3(dest_path, log_files):
    bucket, key = split_s3_path(dest_path)
    print('Bucket : %s , Key : %s' % (bucket, key))
    s3 = boto3.resource('s3')
    bkt = s3.Bucket(bucket)

    for log in log_files:
        filename = log.split('/')[-1]
        bkt.upload_file(log, key+filename)


def upload_file(content, s3_path):
    s3_client = boto3.client('s3')
    bucket, key = split_s3_path(s3_path)
    s3_client.put_object(Body=content, Bucket=bucket, Key=key)


def delete_file(s3_path):
    client=boto3.client('s3')
    bucket, key = split_s3_path(s3_path)
    client.delete_object(Bucket=bucket, Key=key)
    
