import json
import unittest
from unittest.mock import patch

import requests






from cvService.config import FIXED_RECAPTCHA_SECRET
from cvService.recapcha_token_validator import ReCaptchaTokenValidator


class TestRecaptcha(unittest.TestCase):
    @patch.object(requests, "post")
    def test_is_valid_success(self, mock_post):
        validator = ReCaptchaTokenValidator()

        class FakeSuccess:
            text = json.dumps({"success": True})

        fake = FakeSuccess()
        mock_post.return_value = fake
        assert validator.is_valid("") is True

    @patch.object(requests, "post")
    def test_is_valid_failed(self, mock_post):
        validator = ReCaptchaTokenValidator()

        class FakeFail:
            text = json.dumps({"success": False})

        fake = FakeFail()
        mock_post.return_value = fake
        assert validator.is_valid("") is False

    def test_is_valid_by_fixed_token(self):
        validator = ReCaptchaTokenValidator()
        assert validator.is_valid(FIXED_RECAPTCHA_SECRET) is True
