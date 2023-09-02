# para renderizar os templates que estão dentro do app
from django.shortcuts import render


def home(request):
    return render(request, 'recipes/home.html')
