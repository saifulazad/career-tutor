import boto3


def lambda_handler(event, context):
    # data = (event['Records'][0]['dynamodb']['NewImage'])
    # to_email = data['email']['S']
    # name = data['name']['S']
    name = "Azad"
    to_email = "asas"
    client = boto3.client("ses")
    source = "{} <{}>".format("Career Tutor", "admin@fractalslab.com")
    subject = "Thanks to reach us."

    text_body = f"""
            Hi {name}, Thanks for your comment. We will respond as soon as possible.
        """
    destination = {
        "ToAddresses": [to_email],
        "CcAddresses": [],
        "BccAddresses": [],
    }
    message = {
        "Subject": {"Data": subject},
        "Body": {
            "Text": {"Data": text_body, "Charset": "UTF-8"},
            # "Html": {"Data": html_body, "Charset": "UTF-8"},
        },
    }
    reply_addresses = ["admin@fractalaslab.com"]

    response = client.send_email(
        Source=source,
        Destination=destination,
        Message=message,
        ReplyToAddresses=reply_addresses,
    )

    return response.get("MessageId")


if __name__ == "__main__":
    lambda_handler({}, {})
