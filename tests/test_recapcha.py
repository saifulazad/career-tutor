import unittest
import json
import requests
from cvService.recapcha_token_validator import ReCapchaTokenValidator
from unittest.mock import patch
from cvService.get_signed_url import Response

class TestRecapcha(unittest.TestCase):
    @patch.object(requests, "post")
    def test_is_valid_success(self, mock_post):
        validator = ReCapchaTokenValidator()

        class FakeSuccess:
            text = json.dumps({'success': True})

        fake = FakeSuccess()
        mock_post.return_value = fake
        assert validator.is_valid("") == True

    @patch.object(requests, "post")
    def test_is_valid_failed(self, mock_post):
        validator = ReCapchaTokenValidator()

        class FakeSuccess:
            text = json.dumps({'success': False})

        fake = FakeSuccess()
        mock_post.return_value = fake
        assert validator.is_valid("") is False

    def test_is_valid_by_fixed_token(self):
        validator = ReCapchaTokenValidator()
        assert validator.is_valid('a25db276-58a9-11ec-bf63-0242ac130002') is True
