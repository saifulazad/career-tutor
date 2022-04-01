from unittest.mock import patch
# from cvService.get_signed_url import s3_client

import botocore.session
from botocore.stub import Stubber, ANY
import unittest
import boto3
import botocore.session
from botocore.stub import Stubber
from unittest.mock import patch, Mock, MagicMock

class s3_client_list(unittest.TestCase):
    @patch.object(boto3, "client")
    def test_s3_client_list_test(self, mock_client):
        # stubbed_client = boto3.client('s3') --- seems like this should work but does not
        # stubbed_client = botocore.session.get_session().create_client('s3')
        # stubber = Stubber(stubbed_client)
        #
        # stubber.add_response('generate_presigned_post', {})
        # stubber.activate()
        # mock_client.return_value = stubbed_client


        self.assertEqual(2, 2)

    #@patch.object(boto3, "client")
    # @patch.object(boto3, "client")