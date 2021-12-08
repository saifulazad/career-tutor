import boto3
import json
import uuid
import requests


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('career-tutor-contact-us')
    data = json.loads(event["body"])
    email = data["email"]
    name = data["name"]
    comment = data["comment"]
    url = "https://www.google.com/recaptcha/api/siteverify"
    params = {
        "secret": "6LeBJ30dAAAAANm4aX9wRTzSnbk-9d7iBMsJkwi9",
        "response": data["token"],
    }
    verify_rs = requests.post(url, data=params)
    recaptcha_rs = json.loads(verify_rs.text)
    if recaptcha_rs["success"] is True:
        table.put_item(Item={
            "id": str(uuid.uuid4()),
            "email": email, "name": name,
            "comment": comment, "phone": data["phone"] if "phone" in data else ""
        })
    return {
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'statusCode': 200,
    }
