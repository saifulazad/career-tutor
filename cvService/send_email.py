from email_service import send_email


def lambda_handler(event, context):
    try:
        for record in event['Records']:
            if record['eventName'] == 'INSERT':
                handle_insert(record)
            elif record['eventName'] == 'MODIFY':
                handle_modify(record)
    except Exception as e:
        print(e)


def handle_insert(record):
    newImage = record['dynamodb']['NewImage']
    email = newImage['email']['S']
    send_email(user_mail=email)


def handle_modify(record):
    newImage = record['dynamodb']['NewImage']
    email = newImage['email']['S']
    send_email(user_mail=email)


