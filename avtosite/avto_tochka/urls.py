from django.urls import path


from .views import *

urlpatterns = [
    path('', home, name='main'),  # http://127.0.0.1:8000/
    path('index/<int:indexid>/', index),  # http://127.0.0.1:8000/index/99
    path('services/<slug:serviceslug>/', services),  # http://127.0.0.1:8000/services/razval
    path('about/', about, name='about'),  # http://127.0.0.1:8000/about

]


