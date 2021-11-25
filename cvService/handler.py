import boto3
import json


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb', region_name='ap-southeast-1')

    table = dynamodb.Table('usersTable')
    data = json.loads(event["body"])
    email = data["email"]
    name = data["name"]
    comment = data["comment"]
    phone = data["phone"]
    response = table.put_item(Item={
        "email": email, "name": name,
        "comment": comment, "phone":phone
    })
    return {
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'statusCode': 200,
        'body': json.dumps(response)
    }
