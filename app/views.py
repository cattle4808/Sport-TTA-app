from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from django.utils.timezone import now

from . import models
from . import serializers



class SessionsView(ListCreateAPIView):
    queryset = models.SessionAreaModel.objects.filter(day__gte=now().date())
    serializer_class = serializers.SessionsSerializer

class MainMenuView(ListCreateAPIView):
    queryset = models.BookingModel.objects.all()
    serializer_class = serializers.MainMenuSerializer
