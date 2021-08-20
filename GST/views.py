from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from . import models 
from . import serializers

class GSTList(APIView):

    def get(self,request,format = None):
        gsts = models.GstInfo.objects.all()
        serializer = serializers.GstInfoSerializer(gsts, many=True)
        return Response(serializer.data)

    def post(self,request,format=None):
        serializer = serializers.GstInfoSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class GSTDetail(APIView):
    def get_object(self, pk):
        try:
            return models.GstInfo.objects.get(pk=pk)
        except models.GstInfo.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        gst = self.get_object(pk)
        serializer = serializers.GstInfoSerializer(gst)
        return Response(serializer.data)