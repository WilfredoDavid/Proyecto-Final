from pickle import GET
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template import Template
from AppMensajes.models import *
from AppMensajes.forms import *
from .models import MensajesEnviados, MensajesRecibidos


def inicio(request):
    return render(request, "AppMensajes/inicio.html")

def mensajesRecibidos(request):
    return render(request, "AppMensajes/mensajesRecibidos.html")

def mensajesEnviados(request):
    return render(request, "AppMensajes/mensajesEnviados.html")