from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect


def home(request):
    return HttpResponse("<h1>HOME</h1>")


def index(request, indexid):
    if request.GET:  # Дополнительный GET запрос ?name=VDK&year=45
        print(request.GET)  # http://127.0.0.1:8000/index/99/?name=VDK&year=45
        # return redirect('main')  # Времено
        return redirect('main', permanent=True)  # Постояно
    elif request.POST:
        print(request.POST)  # Дополнительный POST запрос
    return HttpResponse(f"Страница index Автоточка.{indexid}")


def services(request, serviceslug):
    return HttpResponse(f"<h1>Услуги</h1><p>{serviceslug}</p>")


def pageNotFound(request, exception):
    return HttpResponseNotFound(f"<h1>Страница не найдена</h1>")

def pageredirect(request, exception):
    return redirect(f"<h1>Страница перемещена на другой постоянный URL адрес</h1>")