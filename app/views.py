from django.template.context_processors import request
from rest_framework.views import APIView
from rest_framework.generics import ListCreateAPIView
from django.utils import timezone

from . import models
from . import serializers

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


class UserViews(ListCreateAPIView):
    queryset = models.UserModel.objects.all()
    serializer_class = serializers.UserSerializer

# class BookingView(ListCreateAPIView):
#     serializer_class = serializers.BookingSerializer
#
#     def get_queryset(self):
#         return models.BookingModel.objects.filter()


#
# class BookingView(ListCreateAPIView):
#     serializer_class = serializers.BookingSerializer
#     def get_queryset(self):
#         today = timezone.now().date()
#         three_days_later = today + timezone.timedelta(days=3)
#         return models.BookingModel.objects.filter(session_area__day__range=[today, three_days_later])
#
#     def perform_create(self, serializer):
#         user = self.request.user
#         session = serializer.validated_data['session_area']
#         start_time = serializer.validated_data['start_time']
#         end_time = serializer.validated_data['end_time']
#
#         if not (session.start_time <= start_time and end_time <= session.end_time):
#             raise serializers.ValidationError("Выбранное время выходит за границы сессии!")
#
#         overlapping_bookings = models.BookingModel.objects.filter(
#             session_area=session,
#             start_time__lt=end_time,
#             end_time__gt=start_time
#         )
#
#         if overlapping_bookings.exists():
#             raise serializers.ValidationError("Выбранное время уже занято!")
#
#         serializer.save(user=user)