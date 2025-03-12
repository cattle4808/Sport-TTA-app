from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateAPIView, RetrieveAPIView
from django.utils import timezone
from rest_framework.response import Response
from rest_framework import status

from . import models
from . import serializers

class SportAreasView(ListCreateAPIView):
    serializer_class = serializers.SportAreaSerializer
    queryset = models.SportAreaModel.objects.all()
    http_method_names = ['get']

class SessionView(ListCreateAPIView):
    serializer_class = serializers.SessionsSerializer
    queryset = models.SessionAreaModel.objects.all()
    http_method_names = ['get']

    def get_queryset(self):
        today = timezone.now().date()
        three_days_later = today + timezone.timedelta(days=3)
        return self.queryset.filter(day__gte=today, day__lte=three_days_later, status=True).order_by('day')




class BookingView(ListCreateAPIView):
    serializer_class = serializers.BookingSerializer
    def get_queryset(self):
        today = timezone.now().date()
        three_days_later = today + timezone.timedelta(days=3)
        return models.BookingModel.objects.filter(session_area__day__range=[today, three_days_later], session_area__status=True)

class TelegramAuthView(ListCreateAPIView):
    serializer_class = serializers.UserAuthSerializer
    queryset = models.UserModel.objects.all()

class TelegramView(RetrieveAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.UserModel.objects.all()
    lookup_field = 'telegram_id'

class TelegramUpdateView(RetrieveUpdateAPIView):
    serializer_class = serializers.UserSerializer
    queryset = models.UserModel.objects.all()
    lookup_field = 'telegram_id'
    http_method_names = ['put', 'patch']
