from django.urls import path
from datasource.views import ConnectionList, DetailConnection

urlpatterns = [
    path('connection/', ConnectionList.as_view(), name='connection'),
    path('connection/<int:pk>/', DetailConnection.as_view(), name='connection-detail'),
]