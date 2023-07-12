from django.urls import path


from .views import *

urlpatterns = [
    # path('', home, name='main'),  # http://127.0.0.1:8000/
    path('', ServiceHome.as_view(), name='main'),  # http://127.0.0.1:8000/
    # path('index/<int:indexid>/', index),  # http://127.0.0.1:8000/index/99
    path('services/<slug:serviceslug>/', services),  # http://127.0.0.1:8000/services/razval
    path('about/', about, name='about'),  # http://127.0.0.1:8000/about
    # path('addpage/', addpage, name='add_page'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    path('contact/', contact, name='contact'),
    path('login/', login, name='login'),
    # path('post/<int:post_id>/', show_post, name='post'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    path('post/<slug:service_slug>/', ShowService.as_view(), name='post'),
    # path('category/<int:cat_id>/', show_category, name='category'),
    path('category/<slug:cat_slug>/', ServiceCategory.as_view(), name='category'),

]


