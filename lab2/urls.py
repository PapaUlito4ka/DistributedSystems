from django.urls import path

from lab2 import views

urlpatterns = [
    path('', views.home),
]
