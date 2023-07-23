from django.contrib import messages
from django.contrib.auth import logout, login
from django.contrib.auth.views import LoginView
from django.db.models import Q
from django.http import HttpResponse, HttpResponseNotFound, Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse_lazy
from django.views import View
from django.views.generic.edit import FormMixin
from django.views.generic import ListView, DetailView, CreateView, TemplateView
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import *
from .models import *
from .utils import *


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


class ServiceHome(DataMixin, ListView):
    """  Главная страница  """
    model = Service
    template_name = 'avto_tochka/home.html'
    context_object_name = 'posts'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Главная страница")
        return dict(list(context.items()) + list(c_def.items()))

    def get_queryset(self):
        return Service.objects.filter(is_published=True).select_related('cat')


class Search(DataMixin, ListView):
    """  Страница поиска """
    model = Service
    template_name = 'avto_tochka/home.html'
    context_object_name = 'posts'

    def get_queryset(self):
        return Service.objects.filter(Q(content__icontains=self.request.GET.get('q'))
                                      | Q(title__icontains=self.request.GET.get('q'))).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['q'] = self.request.GET.get('q')
        c_def = self.get_user_context(title="Результат поиска", cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))


# def index(request, indexid):
#     if request.GET:  # Дополнительный GET запрос ?name=VDK&year=45
#         print(request.GET)  # http://127.0.0.1:8000/index/99/?name=VDK&year=45
#         # return redirect('main')  # Времено
#         return redirect('main', permanent=True)  # Постояно
#     elif request.POST:
#         print(request.POST)  # Дополнительный POST запрос
#     return HttpResponse(f"Страница index Автоточка.{indexid}")


# def services(request, serviceslug):
#     return HttpResponse(f"<h1>Услуги</h1><p>{serviceslug}</p>")


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


class AddPage(LoginRequiredMixin, DataMixin, CreateView):
    """  Страница добавления услуги  """
    model = Service
    fields = ["title", "slug", "price", "content", "photo", "is_published", "cat"]
    template_name = 'avto_tochka/addpage.html'
    success_url = reverse_lazy('main')
    login_url = reverse_lazy('login')

    # success_url = reverse_lazy('main')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Добавление статьи'
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title="Добавление Услуги", cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))


class About(DataMixin, TemplateView):
    """  Страница о нас  """
    template_name = 'avto_tochka/about.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'О нас'
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title="О нас", cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))


class Contact(DataMixin, TemplateView):
    """  Страница обратная связь  """
    template_name = 'avto_tochka/contact.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Добавление статьи'
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title="Обратная связь", cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))


def pageNotFound(request, exception):
    """  Страница не найдена  """
    return HttpResponseNotFound('<h1>Страница не найдена</h1>')


class ShowService(FormMixin, DataMixin, DetailView):
    """  Страница одной услуги  """
    model = Service
    template_name = 'avto_tochka/service.html'
    slug_url_kwarg = 'service_slug'
    # pk_url_kwarg = 'service_pk'
    context_object_name = 'service'
    form_class = CommentForm
    # success_msg = 'Комментарий успешно создан, ожидайте модерации'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = context['service']
        # context['menu'] = menu
        # return context
        c_def = self.get_user_context(title=context['service'], cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self, **kwargs):
        return reverse_lazy('service', kwargs={'service_slug': self.get_object().slug})

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        self.object = form.save(commit=False)
        self.object.post = self.get_object()
        self.object.user = self.request.user
        self.object.save()
        return super().form_valid(form)


def pageredirect(request, exception):
    """  Страница перемещена  """
    return redirect(f"<h1>Страница перемещена на другой постоянный URL адрес</h1>")


# def show_category(request, cat_id):
#    """  Страница одной категории  """
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


class ServiceCategory(DataMixin, ListView):
    """  Страница одной категории  """
    model = Service
    template_name = 'avto_tochka/home.html'
    context_object_name = 'posts'
    allow_empty = False

    def get_queryset(self):
        return Service.objects.filter(cat__slug=self.kwargs['cat_slug'], is_published=True).select_related('cat')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        # context['title'] = 'Категория - ' + str(context['posts'][0].cat)
        # context['menu'] = menu
        # context['cat_selected'] = context['posts'][0].cat_id
        # return context
        c = Category.objects.get(slug=self.kwargs['cat_slug'])
        c_def = self.get_user_context(title='Категория - ' + str(c.name),
                                      cat_selected=c.pk)
        return dict(list(context.items()) + list(c_def.items()))


class RegisterUser(DataMixin, CreateView):
    """  Страница регистрации  """
    form_class = RegisterUserForm
    template_name = 'avto_tochka/register.html'
    success_url = reverse_lazy('login')

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Регистрация", cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))

    def form_valid(self, form):
        user = form.save()
        login(self.request, user)
        return redirect('main')


class LoginUser(DataMixin, LoginView):
    """  Страница входа  """
    form_class = LoginUserForm
    template_name = 'avto_tochka/login.html'

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        c_def = self.get_user_context(title="Авторизация", cat_selected=None)
        return dict(list(context.items()) + list(c_def.items()))

    def get_success_url(self):
        return reverse_lazy('main')


def logout_user(request):
    """  Страница выхода  """
    logout(request)
    return redirect('main')

