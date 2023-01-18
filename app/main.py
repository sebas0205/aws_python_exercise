from app.client.client import Services

s3 = Services("s3")


def get_buckets():
    response = s3.client.list_buckets()
    for bucket in response['Buckets']:
        print(bucket['Name'])



get_buckets()

