from rest_framework import serializers
from .models import z_users
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer
from rest_framework_simplejwt.tokens import RefreshToken
import bcrypt
import base64

class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = get_user_model()
        fields = ["id", "email", "uname", "password"]

    def create(self, validated_data):
        user = z_users.objects.create(
                email=validated_data['email'],
                uname=validated_data['uname']
            )
        print(user)
        user.set_password(validated_data['password'])
        user.save()
        return user
    
class CustomJWTSerializer(TokenObtainPairSerializer):
    def validate(self, attrs):
        try:
            obj = z_users.objects.get(uname=attrs.get('uname'))
            if obj:
                uname = obj.uname
                password = f"{attrs.get('password')}@@@{uname}"
                encoded_password = base64.b64encode(password.encode('utf-8'))
                isAutenticated = bcrypt.checkpw(encoded_password, obj.password.encode('utf-8'))

                if isAutenticated:
                    refresh = RefreshToken.for_user(obj)
                    response = {
                        'success':True,
                        'refresh': str(refresh),
                        'access': str(refresh.access_token),
                    }
                    return response
            return {
                "error": True,
                "message": "Invalid username atau password"
            }
        except z_users.DoesNotExist:
            return {
                "error": True,
                "message": "Invalid username atau password"
            }
        
# class GenerateJWTSerializer(TokenObtainPairSerializer):
#     def validate(self, attrs):
#         credentials = {
#             'username': '',
#             'password': attrs.get("password"),
#         }
#         user_obj = z_users.objects.filter(email=attrs.get("username"), upassword=attrs.get("password")).first() or z_users.objects.filter(uname=attrs.get("username"), upassword=attrs.get("password")).first()
#         if user_obj:
#             credentials['username'] = user_obj.uname
#             refresh = RefreshToken.for_user(user_obj)
#             print(user_obj.uname)
#             response = {
#                 'success':True,
#                 # 'status_code': status.HTTP_201_CREATED,
#                 'refresh': str(refresh),
#                 'access': str(refresh.access_token),
#             }
#             return response
#         else:
#             response = {
#                 'success':False,
#                 'message': 'Username or Password not found',
#             }
#             return response