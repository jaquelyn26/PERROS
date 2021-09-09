from django.urls import path
from .views import *


urlpatterns = [
    path('', perro, name='perro'),
    path('generic/', generic, name='generic'),
    path('elements/', elements, name='elements'),
]
