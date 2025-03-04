from rest_framework.serializers import ModelSerializer

from . import models


class SessionsSerializer(ModelSerializer):
    class Meta:
        model = models.SessionAreaModel
        fields = '__all__'

class MainMenuSerializer(ModelSerializer):
    class Meta:
        model = models.BookingModel
        fields = '__all__'
