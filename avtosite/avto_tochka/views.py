from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    return HttpResponse("<h1>HOME</h1>")


def index(request):
    return HttpResponse("Страница index Автоточка.")


def services(request):
    return HttpResponse("<h1>Услуги</h1>")

