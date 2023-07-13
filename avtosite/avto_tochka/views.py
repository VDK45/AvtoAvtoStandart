from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, CreateView
from .forms import *
from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить услугу", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
        {'title': "Войти", 'url_name': 'login'}
]


# класс ServiceHome взамен
# def home(request):
#     # posts = Service.objects.all()
#     # cats = Category.objects.all()
#
#     context = {
#         'title': 'Главная страница',
#         'menu': menu,
#         # 'posts': posts,
#         # 'cats': cats,
#         'cat_selected': 0,
#     }
#     return render(request, 'avto_tochka/home.html', context=context)


class ServiceHome(ListView):
    model = Service
    template_name = 'avto_tochka/home.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['menu'] = menu
        context['title'] = 'Главная страница'
        context['cat_selected'] = 0
        return context

    def get_queryset(self):
        return Service.objects.filter(is_published=True)


def about(request):
    return render(request, 'avto_tochka/about.html', {'title': 'О сайте', 'menu': menu})

#
# def index(request, indexid):
#     if request.GET:  # Дополнительный GET запрос ?name=VDK&year=45
#         print(request.GET)  # http://127.0.0.1:8000/index/99/?name=VDK&year=45
#         # return redirect('main')  # Времено
#         return redirect('main', permanent=True)  # Постояно
#     elif request.POST:
#         print(request.POST)  # Дополнительный POST запрос
#     return HttpResponse(f"Страница index Автоточка.{indexid}")


def services(request, serviceslug):
    return HttpResponse(f"<h1>Услуги</h1><p>{serviceslug}</p>")


# def addpage(request):
#     if request.method == 'POST':
#         form = AddServiceForm(request.POST, request.FILES)
#         if form.is_valid():
#             # add to database:
#             try:
#                 # Service.objects.create(**form.cleaned_data)  # Форма не связана с БД
#                 form.save()  # Форма связана с БД
#                 return redirect('main')
#             except:
#                 form.add_error(None, 'Ошибка добавления поста')
#     else:
#         form = AddServiceForm()
#
#     return render(request, 'avto_tochka/addpage.html', {'form': form, 'menu': menu, 'title': 'Добавление услуги'})


class AddPage(CreateView):
    model = Service
    fields = ["title", "slug", "price", "content", "photo", "is_published", "cat"]
    template_name = 'avto_tochka/addpage.html'
    # success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Добавление статьи'
        context['menu'] = menu
        return context


def contact(request):
    return HttpResponse("Обратная связь")


def login(request):
    return HttpResponse("Авторизация")


def pageNotFound(request, exception):
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


# def show_post(request, post_id):
#     return HttpResponse(f"Отображение статьи с id = {post_id}")
# def show_post(request, post_slug):
#     post = get_object_or_404(Service, slug=post_slug)
#
#     context = {
#         'post': post,
#         'menu': menu,
#         'title': post.title,
#         'cat_selected': post.cat_id,
#     }
#     return render(request, 'avto_tochka/service.html', context=context)


class ShowService(DetailView):
    model = Service
    template_name = 'avto_tochka/service.html'
    slug_url_kwarg = 'service_slug'
    # pk_url_kwarg = 'service_pk'
    context_object_name = 'service'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = context['service']
        context['menu'] = menu
        return context


def pageredirect(request, exception):
    return redirect(f"<h1>Страница перемещена на другой постоянный URL адрес</h1>")


# def show_category(request, cat_id):
#     # posts = Service.objects.filter(cat_id=cat_id)
#     # cats = Category.objects.all()
#
#     # if len(posts) == 0:
#     #     raise Http404()
#
#     context = {
#         'title': 'Отображение по сервисам',
#         'menu': menu,
#         # 'posts': posts,
#         # 'cats': cats,
#         'cat_selected': cat_id,
#     }
#     return render(request, 'avto_tochka/home.html', context=context)


class ServiceCategory(ListView):
    model = Service
    template_name = 'avto_tochka/home.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Service.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        context['menu'] = menu
        context['cat_selected'] = context['posts'][0].cat_id
        return context
