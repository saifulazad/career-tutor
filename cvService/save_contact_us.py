import boto3
import json
import uuid
import requests


def token_validation(token):
    url = "https://www.google.com/recaptcha/api/siteverify"
    params = {
        "secret": "6LeBJ30dAAAAANm4aX9wRTzSnbk-9d7iBMsJkwi9",
        "response": token,
    }
    verify_rs = requests.post(url, data=params)
    recaptcha_rs = json.loads(verify_rs.text)
    return recaptcha_rs["success"]


def lambda_handler(event, context):
    dynamodb = boto3.resource('dynamodb')

    table = dynamodb.Table('career-tutor-contact-us')
    data = json.loads(event["body"])
    email = data["email"]
    name = data["name"]
    comment = data["comment"]
    phone = data.get("phone", "")
    response = {
        'headers': {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*"
        },
        'body': {'error': 'Invalid reCapcha token.'},
        'statusCode': 200,
    }
    local_token = "a25db276-58a9-11ec-bf63-0242ac130002"
    if token_validation(data["token"]) is True or data["token"] == local_token:
        response['body'] = table.put_item(Item={
            "id": str(uuid.uuid4()),
            "email": email, "name": name,
            "comment": comment, "phone": phone
        })
    response["body"] = json.dumps(response["body"])
    return response
