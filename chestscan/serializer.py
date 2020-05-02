from . import models
from rest_framework import serializers


class ResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.ResponseModel
        fields = '__all__'