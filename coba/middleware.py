from functools import wraps
from .jwt import JWTAuth
from rest_framework.response import Response


def jwtRequired(fn):
    @wraps(fn)
    def wrapper(request, *args, **kwargs):
        try:
            user = decode(request.headers.get('Authorization'))
            request.user = user
            return fn(request, *args, **kwargs)
        except Exception as e:
            return Response({"message": "Invalid tokennnn"}, status=401)
    return wrapper


def decode(token):
    token = str(token).split(' ')
    return JWTAuth().decode(token[1])