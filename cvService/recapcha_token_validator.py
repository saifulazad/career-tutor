import json

import config
import requests


class BaseReCaptchaTokenValidator:
    def is_valid(self, token):
        raise NotImplementedError


class ReCaptchaTokenValidator(BaseReCaptchaTokenValidator):
    fix_token = config.FIXED_RECAPTCHA_SECRET

    def is_valid(self, token):
        if token == self.fix_token:
            return True
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            "secret": config.RECAPTCHA_SECRET,
            "response": token,
        }
        verify_rs = requests.post(url, data=params)
        recaptcha_rs = json.loads(verify_rs.text)
        return recaptcha_rs.get("success", False)
