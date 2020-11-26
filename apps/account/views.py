from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Config
from .forms import ConfigForm, AdminCreation

def home(request):
    
    config = Config.objects.count()
    
    if config == 0:
        return redirect('install')
    
    else:
        return HttpResponse("Dashboard")

def config(request):
    
    if request.method == 'POST':
        form = ConfigForm(request.POST, request.FILES)
        a_form = AdminCreation(request.POST)
        
        if form.is_valid() and a_form.is_valid():
            form.save()
            a_form.save()
            return redirect('login')
                
    else:
        form = ConfigForm()
        a_form = AdminCreation()
    
    return render(request, 'config/config.html', {'form': form, 'a_form': a_form})
