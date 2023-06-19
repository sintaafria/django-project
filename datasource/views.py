from rest_framework import generics, status, permissions
from datasource.models import zpraba_conn
from datasource.serializers import zpraba_conn_serializer
from rest_framework.response import Response

from django.utils.decorators import method_decorator
from coba.middleware import jwtRequired


class ConnectionList(generics.ListAPIView):
    queryset = zpraba_conn.objects.all()
    serializer_class = zpraba_conn_serializer
    # permission_classes = [permissions.IsAuthenticated]
    @method_decorator(decorator=jwtRequired, name="get")
    def get(self, request):
        queryset = self.get_queryset()
        serializer = zpraba_conn_serializer(queryset, many=True)
        return Response(serializer.data)
    @method_decorator(decorator=jwtRequired, name="post")
    def post(self, request):
        print(request.user)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DetailConnection(generics.RetrieveUpdateDestroyAPIView):
    queryset = zpraba_conn.objects.all()
    serializer_class = zpraba_conn_serializer
