import json
import uuid

import boto3
from recapcha_token_validator import ReCapchaTokenValidator
from response import Response


def lambda_handler(event, context):
    data = json.loads(event["body"])
    email = data["email"]
    name = data["name"]
    comment = data["comment"]
    phone = data.get("phone", "")
    validation = ReCapchaTokenValidator()
    if validation.is_valid(data["token"]):
        dynamodb = boto3.resource("dynamodb")
        table = dynamodb.Table("career-tutor-contact-us")
        table.put_item(
            Item={
                "id": str(uuid.uuid4()),
                "email": email,
                "name": name,
                "comment": comment,
                "phone": phone,
            }
        )
        response = Response(status_code=200, payload={})
    else:
        response = Response(
            status_code=400, payload={"error": "Invalid reCapcha token."}
        )
    return response.render()
