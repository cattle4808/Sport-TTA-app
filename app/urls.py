from rest_framework.urls import path

from . import views

urlpatterns = [
    path('session/', views.SessionView.as_view()),
    path('sport_area/', views.SportAreasView.as_view()),

    #booking
    path('booking/', views.BookingView.as_view()),

    #user
    path('auth/', views.TelegramAuthView.as_view()),
    path('user/<int:telegram_id>/', views.TelegramView.as_view()),
    path('user/<int:telegram_id>/update/', views.TelegramUpdateView.as_view()),
]