from rest_framework.urls import path

from . import views

urlpatterns = [
    path('session/', views.SessionView.as_view()),
    path('booking/', views.BookingView.as_view()),
    path('user/', views.UserViews.as_view())
]