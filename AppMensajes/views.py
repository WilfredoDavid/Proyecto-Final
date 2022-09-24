from distutils.log import info
from multiprocessing import context
from pickle import GET
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.template import Template
from AppMensajes.models import *
from AppMensajes.forms import MensajesFormulario
from .models import MensajesEnviados, MensajesRecibidos, Mensajes


def inicio(request):
    return render(request, "AppMensajes/inicio.html")

def mensajesRecibidos(request):
    return render(request, "AppMensajes/mensajesRecibidos.html")

def mensajesEnviados(request):
    return render(request, "AppMensajes/mensajesEnviados.html")

def inbox(request):
    
    if request.method == "POST":
        miFormulario=MensajesFormulario(request.POST)
        print(miFormulario)
        if miFormulario.is_valid():
            info=miFormulario.cleaned_data
            usuario=info.get("usuario")
            texto=info.get("texto")
            mensaje=Mensajes(usuario=usuario, texto=texto)
            mensaje.save()
            return render(request, "AppMensajes/inbox.html", {"comentario":"Mensaje enviado"})

        else:
            return render(request, "AppMensajes/inbox.html", {"comentario":"Ingrese nuevamente, pero bien"})

    else:
        miFormulario=MensajesFormulario()
        return render(request,"AppMensajes/inbox.html", {"formulario":miFormulario})


def busquedaUsuario(request):
    return render(request, "AppMensajes/busquedaUsuario.html")  

def buscar(request):
    if request.GET["usuario"]:
        usua=request.GET["usuario"]
        mensajes=Mensajes.objects.filter(usuario=usua)
        if len(mensajes)!=0:
            return render(request, "AppMensajes/resultadoBusqueda.html", {"mensaje":mensajes})
        else:
            return render(request, "AppMensajes/resultadoBusqueda.html", {"comentario":"No existe mensajes de este guachin"})
    
    else:
         return render(request, "AppMensajes/resultadoBusqueda.html", {"comentario":"No enviaste datos, intentalo de nuevo"})


        
   