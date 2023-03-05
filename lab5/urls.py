from django.urls import path

from lab5 import views

urlpatterns = [
    path('', views.search),
]
