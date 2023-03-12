from django.urls import path

from lab6 import views

urlpatterns = [
    path('', views.search),
]
