from rest_framework.serializers import ModelSerializer
from .models import  GstInfo


class GstInfoSerializer(ModelSerializer):
    class Meta:
        model = GstInfo
        fields = '__all__'