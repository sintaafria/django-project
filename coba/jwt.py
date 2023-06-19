import jwt

class JWTAuth:
    def __init__(self):
        self.secret = "c&%z@j8am*w-@7+&tc4&z7if^x+a&sdtt"

    def encode(self, payload):
        return jwt.encode(payload, self.secret, algorithm='HS256')

    def decode(self, token):
        return jwt.decode(token, self.secret, algorithms=['HS256'])