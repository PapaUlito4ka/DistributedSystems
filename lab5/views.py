from typing import List, Dict

import requests
from django.http import HttpRequest
from django.shortcuts import render

from lab5.services import SearchService


def search(request: HttpRequest):
    search_param: str = request.GET.get('search', '')
    posts: List[Dict] = requests.get('https://jsonplaceholder.typicode.com/posts').json()

    posts = SearchService.search(posts, search_param)
    return render(request, 'lab5/search_posts.html', context={
        'posts': posts
    })
