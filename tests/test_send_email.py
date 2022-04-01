import botocore.session
import unittest
import boto3
import botocore.session
from cvService.send_email import lambda_handler
from botocore.stub import Stubber
from unittest.mock import patch


class TestSESSendEmail(unittest.TestCase):
    @patch.object(boto3, "client")
    def test_ses_send_email(self, mock_client):
        stubbed_client = botocore.session.get_session().create_client('ses')
        stubber = Stubber(stubbed_client)
        response = {
            'MessageId': ''
        }
        stubber.add_response('send_email', response)
        stubber.activate()
        mock_client.return_value = stubbed_client
        assert lambda_handler({}, {}) == ''
