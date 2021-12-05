import boto3
import json
import uuid


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('career-tutor-contact-us')
    data = json.loads(event["body"])
    email = data["email"]
    name = data["name"]
    comment = data["comment"]
    response = table.put_item(Item={
        "id": str(uuid.uuid4()),
        "email": email, "name": name,
        "comment": comment, "phone": data["phone"] if "phone" in data else []
    })
    return {
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'statusCode': 200,
        'body': json.dumps(response)
    }
