from django.urls import path
from .views import *
from . import views

urlpatterns = [
    path('base/', base, name='base'),
    path('', index, name='index'),
    path('contacto/', views.sucursales_view, name='contacto'),
    path('nosotros/', nosotros, name='nosotros'),
    path('ofertas/', ofertas, name='ofertas'),
    path('productos/', productos, name='productos'),
] 