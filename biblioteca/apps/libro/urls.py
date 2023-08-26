from django.urls import path
from .views import libros

urlpatterns = [
    path('', libros)


]
