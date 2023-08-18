from django.http import HttpResponse
from django.shortcuts import render, reverse
import os
import datetime

def home_view(request):
    template_name = 'app/home.html'
    pages = {
        'Главная страница': reverse('home'),
        'Показать текущее время': reverse('time'),
        'Показать содержимое рабочей директории': reverse('workdir')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def time_view(request):
    current_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    msg = f'Текущее время: {current_time}'
    return HttpResponse(msg)

def workdir_view(request):
    current_directory = os.getcwd()
    files = os.listdir(current_directory)
    files_str = ', '.join(files)
    return HttpResponse(f'Содержимое рабочей директории: {files_str}')
