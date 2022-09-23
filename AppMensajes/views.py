from pickle import GET
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template import Template
from AppMensajes.models import *
from AppMensajes.forms import MensajesFormulario
from .models import MensajesEnviados, MensajesRecibidos


def inicio(request):
    return render(request, "AppMensajes/inicio.html")

def mensajesRecibidos(request):
    return render(request, "AppMensajes/mensajesRecibidos.html")

def mensajesEnviados(request):
    return render(request, "AppMensajes/mensajesEnviados.html")

def mensajesFormulario(request):
    if request.method == "POST":
        miFormulario=MensajesFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            print(info)
            usuario=info.get("usuario")
            mensaje=info.get("mensaje")
            mensaje=Mensajes(usuario=usuario, mensaje=mensaje)
            mensaje.save()
            return render(request,"AppMensajes/mensajesEnviados.html",{"mensaje":"Mensaje Enviado"})
        else:
            return render(request, "AppMensajes/mensajesFormulario.html", {"mensaje":"Error"})
            
    else:
        miFormulario=MensajesFormulario()
        return render(request,"AppMensajes/mensajesFormulario.html", {"formulario":"miFormulario"})
    return render(request, "AppMensajes/mensajesFormulario.html")