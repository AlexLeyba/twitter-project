from django.shortcuts import render, redirect
from twitter_project.models import Twit


# вывод страницы авторизации
def login(request):
    return render(request, 'account/login.html')


# заносит твит в базу данных

def form_twit(request):
    # if request.method == "POST":
    error = False
    a = request.GET.get('text_message', '')
    if str(a) != '' and len(a) <= 250:
        i = Twit.objects.create(text=a)
        i.save()
    else:
        error = "Error"
    mess = Twit.objects.all()
    return render(request, 'index.html', {"mess": mess, "error": error})


