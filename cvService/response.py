import json













class Response:

    defaults = {
        "headers": {
            "Access-Control-Allow-Origin": "*",
            "Access-Control-Allow-Methods": "*",
        },
    }

    def __init__(self, status_code=200, payload=None):
        self.status_code = status_code
        self.payload = payload

    def render(self):
        if self.status_code == 200:
            if self.payload is None:
                self.payload = {}
        return {
            **self.defaults,
            **{"statusCode": self.status_code, "body": json.dumps(self.payload)},
        }
