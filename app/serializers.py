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
        extra_kwargs = {'user': {'read_only': True}}  # Нельзя менять юзера после создания брони

    def get_session(self, obj):
        return SessionsSerializer(obj.session_area).data

    def validate(self, data):
        session_area = data['session_area']
        start_time = data['start_time']
        end_time = data['end_time']

        if start_time >= end_time:
            raise serializers.ValidationError("Время окончания бронирования должно быть позже времени начала.")

        if not (session_area.start_time <= start_time and end_time <= session_area.end_time):
            raise serializers.ValidationError("Выберите время в пределах доступной сессии.")

        duration_minutes = (end_time.hour * 60 + end_time.minute) - (start_time.hour * 60 + start_time.minute)
        if duration_minutes > 120:
            raise serializers.ValidationError("Максимальное время бронирования — 2 часа.")

        if models.BookingModel.objects.filter(
            session_area=session_area,
            start_time__lt=end_time,
            end_time__gt=start_time
        ).exists():
            raise serializers.ValidationError("Это время уже занято. Выберите другое.")

        return data


class SportAreaSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.SportAreaModel
        fields = '__all__'
