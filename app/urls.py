from rest_framework.urls import path

from . import views

urlpatterns = [
    path('main', views.MainMenuView.as_view()),
    path('sessions', views.SessionsView.as_view()),
]