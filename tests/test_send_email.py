import unittest
from unittest.mock import patch

import boto3
import botocore.session
from botocore.stub import Stubber

from cvService.send_email import lambda_handler


class TestSESSendEmail(unittest.TestCase):
    @patch.object(boto3, "client")
    def test_ses_send_email(self, mock_client):
        stubbed_client = botocore.session.get_session().create_client("ses")
        stubber = Stubber(stubbed_client)
        response = {"MessageId": ""}
        stubber.add_response("send_email", response)
        stubber.activate()
        mock_client.return_value = stubbed_client
        assert (
            lambda_handler(
                event={
                    "Records": [
                        {
                            "dynamodb": {
                                "NewImage": {
                                    "email": {"S": "muazzem.mamun@gmail.com"},
                                    "name": {"S": "Mamun"},
                                },
                            },
                        }
                    ]
                },
                context={},
            )
            == ""
        )
