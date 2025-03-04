from django.contrib import admin

from . import filters
from .models import UserModel, SportAreaModel, SessionAreaModel, BookingModel


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'username', 'status')
    list_filter = ('status',)
    search_fields = ('username',)

@admin.register(SportAreaModel)
class SportAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'address')
    search_fields = ('name', 'address')

@admin.register(SessionAreaModel)
class SessionAreaAdmin(admin.ModelAdmin):
    list_display = ('id', 'sport_area__name','day', 'start_time', 'end_time', 'status')
    list_display_links = ('sport_area__name', 'status')
    list_filter = ('sport_area__name', 'status', filters.DayFilterAdmin)
    search_fields = ('sport_area__name',)


@admin.register(BookingModel)
class BookingAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'session_area', 'start_time', 'end_time')
    list_filter = ('session_area', 'user')
    search_fields = ('user__username', 'session_area__sport_area__name')
