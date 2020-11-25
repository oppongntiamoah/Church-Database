from django.shortcuts import render
from django.http import HttpResponse
from .models import Config


def home(request):
    config = Config.objects.count()

    if config == 0:
        return render(request, 'config/config.html')
    else:
        return HttpResponse("Value is 1")