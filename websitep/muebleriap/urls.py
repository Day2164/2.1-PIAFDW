from django.urls import path
from .views import *

urlpatterns = [
    path('base/', base, name='base'),
    path('', index, name='index'),
    path('contacto/', contacto, name='contacto'),
    path('nosotros/', nosotros, name='nosotros'),
    path('ofertas/', ofertas, name='ofertas'),
    path('productos/', productos, name='productos'),
] 