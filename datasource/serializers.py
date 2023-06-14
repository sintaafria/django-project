from rest_framework import serializers
from datasource.models import zpraba_conn

class zpraba_conn_serializer(serializers.ModelSerializer):
    
    class Meta:
        model = zpraba_conn
        exclude = ["conn_name", "conn_params", "desc"]
