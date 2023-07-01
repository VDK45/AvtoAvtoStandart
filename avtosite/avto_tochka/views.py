from django.http import HttpResponse, HttpResponseNotFound
from django.shortcuts import render, redirect
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить услугу", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


def home(request):
    posts = Service.objects.all()
    context = {
        'title': 'Главная страница',
        'menu': menu,
        'posts': posts
    }
    return render(request, 'avto_tochka/home.html', context=context)


def about(request):
    return render(request, 'avto_tochka/about.html', {'title': 'О сайте', 'menu': menu})


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


def addpage(request):
    return HttpResponse("Добавление статьи")


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


def show_post(request, post_id):
    return HttpResponse(f"Отображение статьи с id = {post_id}")


def pageredirect(request, exception):
    return redirect(f"<h1>Страница перемещена на другой постоянный URL адрес</h1>")




