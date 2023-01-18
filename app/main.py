from app.client.client import Services

s3 = Services("s3")


def get_buckets():
    response = s3.client.list_buckets()
    print(response)


get_buckets()

