from . import models
from rest_framework import serializers


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResponseModel
        fields = '__all__'

class RequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RequestData
        fields = '__all__'