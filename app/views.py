from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
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


class TelegramAuthView(APIView):
    def post(self, request):
        user_id = request.data.get("id")
        username = request.data.get("username", f"user_{user_id}")
        user, _ = models.UserModel.objects.get_or_create(user_id=user_id, defaults={"username": username})
        return Response(serializers.UserSerializer(user).data, status=status.HTTP_200_OK)
