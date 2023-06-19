import json
from .models import custom_users
from rest_framework.response import Response
import base64
import bcrypt
from coba.jwt import JWTAuth
from django.views.decorators.csrf import csrf_exempt

from django.http import JsonResponse

@csrf_exempt
def auth(request):
    if request.method == 'POST':
        json_data = json.loads(request.body)
        uname = json_data['uname']
        password = json_data['upassword']
        try:
            obj = custom_users.objects.filter(uname=uname).first()
            if obj:
                password = f"{password}@@@{uname}"
                encoded_password = base64.b64encode(password.encode('utf-8'))
                isAutenticated = bcrypt.checkpw(encoded_password, obj.upassword.encode('utf-8'))
                if isAutenticated:
                    token = JWTAuth().encode({
                        "id": obj.id,
                        "uname": obj.uname
                    })
                    return JsonResponse({"token":str(token)})
            return JsonResponse({
                "error": True,
                "message": "Invalid username atau password"
            })
        except custom_users.DoesNotExist:
            return JsonResponse({
                "error": True,
                "message": "Invalid username atau password"
            })