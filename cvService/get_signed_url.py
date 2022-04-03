import boto3
from botocore.client import Config
from response import Response

s3_client = boto3.client("s3", config=Config(signature_version="s3v4"))


def create_presigned_post(bucket_name, object_name, expiration=3600):
    response = s3_client.generate_presigned_post(
        bucket_name, object_name, ExpiresIn=expiration
    )
    return response


def lambda_handler(event, context):
    import uuid

    name = str(uuid.uuid4())
    ext = event["queryStringParameters"]["extension"]
    key = f"{name}.{ext}"
    response = create_presigned_post("cv-maker", key)
    return Response(status_code=200, payload=response).render()
