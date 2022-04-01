import datetime
import botocore.session
from botocore.stub import Stubber, ANY


def test_a():
    ses = botocore.session.get_session().create_client('ses')
    stubber = Stubber(ses)

    response = {
        'MessageId': ''
    }
    stubber.add_response('send_email', response)
    source = "{} <{}>".format("Career Tutor", 'admin@fractalslab.com')
    subject = "Thanks to reach us."

    text_body = f"""
                Hi azad, Thanks for your comment. We will respond as soon as possible.
            """
    destination = {
        "ToAddresses": ['to_email'],
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
    reply_addresses = ['admin@fractalaslab.com']

    # response = client.send_email(

    with stubber:
        service_response = ses.send_email(Source=source,
                                          Destination=destination,
                                          Message=message,
                                          ReplyToAddresses=reply_addresses,
                                          )
        print('A' * 100)
        print(service_response)

        print('A' * 100)
    assert service_response == response
