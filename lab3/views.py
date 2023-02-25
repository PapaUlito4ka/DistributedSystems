from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
import random


@csrf_exempt
def home(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'lab3/form.html')
    if request.method == 'POST':
        if not (request.POST.get('email') or request.POST.get('password')):
            return redirect('/lab3')
        return render(request, 'lab3/display_form_data.html', context={
            'email': request.POST.get('email'),
            'password': request.POST.get('password'),
            'color':    random.choice(['red', 'yellow', 'green', 'black', 'pink'])
        })
