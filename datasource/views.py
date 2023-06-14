from rest_framework import generics, status, permissions
from datasource.models import zpraba_conn
from datasource.serializers import zpraba_conn_serializer
from rest_framework.response import Response

class ConnectionList(generics.ListAPIView):
    queryset = zpraba_conn.objects.all()
    serializer_class = zpraba_conn_serializer
    permission_classes = [permissions.IsAuthenticated]
    def get(self, request):
        queryset = self.get_queryset()
        serializer = zpraba_conn_serializer(queryset, many=True)
        return Response(serializer.data)
    def post(self, request):
        print(request.user.__dict__)
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"status": "success", "data": serializer.data}, status=status.HTTP_201_CREATED)
        else:
            return Response({"status": "fail", "message": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

class DetailConnection(generics.RetrieveUpdateDestroyAPIView):
    queryset = zpraba_conn.objects.all()
    serializer_class = zpraba_conn_serializer
