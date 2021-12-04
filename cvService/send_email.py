import boto3


def lambda_handler(event, context):
    data = (event['Records'][0]['dynamodb']['NewImage'])
    to_email = data['email']['S']
    name = data['name']['S']
    client = boto3.client('ses')
    source = "{} <{}>".format("Career Tutor", 'admin@fractalslab.com')
    subject = "Thanks to reach us."

    html_body = f"""
            <h3>Hi {name}, Thanks for your comment. We will respond as soon as possible.</h3>
        """
    destination = {
        "ToAddresses": [to_email],
        "CcAddresses": [],
        "BccAddresses": [],
    }
    message = {
        "Subject": {"Data": subject},
        "Body": {
            "Html": {"Data": html_body, "Charset": "UTF-8"},
        },
    }
    reply_addresses = ['admin@fractalaslab.com']

    response = client.send_email(
        Source=source,
        Destination=destination,
        Message=message,
        ReplyToAddresses=reply_addresses,
    )

    return response.get("MessageId")


if __name__ == '__main__':
    lambda_handler({}, {})


