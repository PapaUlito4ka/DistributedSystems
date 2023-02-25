import datetime

from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt

from lab4.tasks import large_task


@csrf_exempt
def home(request: HttpRequest):
    if request.method == 'GET':
        return render(request, 'lab4/form.html')
    if request.method == 'POST':
        print('First', datetime.datetime.now())
        large_task.apply_async(kwargs={'message': request.POST.get('message')},)
        print('Second', datetime.datetime.now())
        return HttpResponse(status=200)
