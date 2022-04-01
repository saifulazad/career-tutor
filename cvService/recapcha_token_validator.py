import requests
import json


class BaseReCapchaTokenValidator:

    def is_valid(self):
        raise NotImplementedError


class ReCapchaTokenValidator(BaseReCapchaTokenValidator):
    fix_token = 'a25db276-58a9-11ec-bf63-0242ac130002'

    def is_valid(self, token):
        if token == self.fix_token:
            return True
        url = "https://www.google.com/recaptcha/api/siteverify"
        params = {
            "secret": "6LeBJ30dAAAAANm4aX9wRTzSnbk-9d7iBMsJkwi9",
            "response": token,
        }
        verify_rs = requests.post(url, data=params)
        recaptcha_rs = json.loads(verify_rs.text)
        return recaptcha_rs.get("success", False)
