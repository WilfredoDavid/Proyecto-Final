from django.urls import path 
from .views import *


urlpatterns = [

    path('', inicio, name="inicio" ),
    path('mensajesRecibidos/', mensajesRecibidos, name="mensajesRecibidos"),
    path('mensajesEnviados/', mensajesEnviados, name="mensajesEnviados"),


]