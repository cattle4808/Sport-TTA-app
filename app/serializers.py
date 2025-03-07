from datetime import timedelta

from django.core.serializers import serialize
from django.db.models import Q
from rest_framework import serializers

from . import models


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserModel
        fields = '__all__'


class SessionsSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SessionAreaModel
        fields = '__all__'


class BookingSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(
        queryset=models.UserModel.objects.all(),
        slug_field='user_tg_id'
    )
    session = serializers.SerializerMethodField()

    class Meta:
        model = models.BookingModel
        fields = ['id', 'user', 'session_area', 'start_time', 'end_time', 'session']

    def get_session(self, obj):
        return obj.session_area.id

    def validate(self, data):
        session_area = data['session_area']
        start_time = data['start_time']
        end_time = data['end_time']

        if start_time < session_area.start_time or end_time > session_area.end_time:
            raise serializers.ValidationError("Выберите время в пределах доступной сессии.")

        duration = timedelta(
            hours=end_time.hour, minutes=end_time.minute
        ) - timedelta(
            hours=start_time.hour, minutes=start_time.minute
        )

        if duration > timedelta(hours=2):
            raise serializers.ValidationError("Максимальное время бронирования — 2 часа.")

        overlapping_bookings = models.BookingModel.objects.filter(
            session_area=session_area
        ).filter(
            Q(start_time__lt=end_time) & Q(end_time__gt=start_time)
        )


        if overlapping_bookings.exists():
            raise serializers.ValidationError("Это время уже занято. Выберите другое.")

        return data

class SportAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SportAreaModel
        fields = '__all__'
