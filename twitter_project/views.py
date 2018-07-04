from django.shortcuts import render

# Create your views here.
from django.shortcuts import render


# вывод главной страницы
def index(request):
    return render(request, 'index.html')


# вывод страницы авторизации
def login(request):
    return render(request, 'account/login.html')
