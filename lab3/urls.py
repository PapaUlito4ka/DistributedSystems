from django.urls import path

from lab3 import views

urlpatterns = [
    path('', views.home)
]
