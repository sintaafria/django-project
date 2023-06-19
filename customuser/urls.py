from django.urls import path
from .views import auth


urlpatterns = [
    path('cutom-login/', auth, name="sign_in"),
]