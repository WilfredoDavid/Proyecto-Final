from django.urls import path, include
from .views import *


urlpatterns = [

    path('', inicio, name="inicio" ),
    path('mensajesRecibidos/', mensajesRecibidos, name='mensajesRecibidos'),
    path('mensajesEnviados/', mensajesEnviados, name='mensajesEnviados'),
    path('inbox/', inbox, name='inbox'),
    path('busquedaUsuario/', busquedaUsuario, name='busquedaUsuario'),
    path('buscar/', buscar ,name='buscar' ),


]