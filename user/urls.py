from django.urls import path
from .views import RegisterView, LoginView
from rest_framework_simplejwt import views as jwt_views
from . import serializers

urlpatterns = [
    path('register/', RegisterView.as_view(), name="sign_up"),
    path('login/', LoginView.as_view(), name="sign_in"),
    path('token/get/', jwt_views.TokenObtainPairView.as_view(serializer_class=serializers.CustomJWTSerializer), name="token-obtain")

]