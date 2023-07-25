from django.urls import path
from django.views.decorators.cache import cache_page

from .views import *

urlpatterns = [
    # path('', home, name='main'),  # http://127.0.0.1:8000/
    path('', ServiceHome.as_view(), name='main'),  # http://127.0.0.1:8000/
    # path('index/<int:indexid>/', index),  # http://127.0.0.1:8000/index/99
    # path('services/<slug:serviceslug>/', services),  # http://127.0.0.1:8000/services/razval
    # path('about/', about, name='about'),  # http://127.0.0.1:8000/about
    path('about/', cache_page(360)(About.as_view()), name='about'),  # http://127.0.0.1:8000/about
    # path('addpage/', addpage, name='add_page'),
    path('addpage/', AddPage.as_view(), name='add_page'),
    # path('contact/', contact, name='contact'),
    path('contact/', cache_page(360)(Contact.as_view()), name='contact'),
    path('login/', LoginUser.as_view(), name='login'),
    path('register/', RegisterUser.as_view(), name='register'),
    path('logout/', logout_user, name='logout'),
    # path('post/<int:post_id>/', show_post, name='post'),
    # path('post/<slug:post_slug>/', show_post, name='post'),
    path('service/<slug:service_slug>/', ShowService.as_view(), name='service'),
    # path('category/<int:cat_id>/', show_category, name='category'),
    path('category/<slug:cat_slug>/', cache_page(360)(ServiceCategory.as_view()), name='category'),
    path('search/', Search.as_view(), name='search'),
    path('accounts/profile/', Profile.as_view(), name='profile'),
]


