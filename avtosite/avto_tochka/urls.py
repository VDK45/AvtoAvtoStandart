from django.urls import path


from .views import *

urlpatterns = [
    path('', home),  # http://127.0.0.1:8000/avtoservice/
    path('index/', index),  # http://127.0.0.1:8000/avtoservice/index/
    path('services/', services),  # http://127.0.0.1:8000/avtoservice/services/
]
