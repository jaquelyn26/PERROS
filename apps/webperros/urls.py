from django.urls import path
from .views import perro


urlpatterns = {
    path('', perro, name='perro'),
}
