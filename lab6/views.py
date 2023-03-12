from django.http import HttpRequest
from django.shortcuts import render


def search(request: HttpRequest):
    return render(request, 'lab6/search_posts.html')
