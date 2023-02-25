from django.urls import path

from lab4 import views

urlpatterns = [
    path('', views.home),
]
