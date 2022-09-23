from unittest.util import _MAX_LENGTH
from django.db import models


# Create your models here.
class MensajesRecibidos(models.Model):
    usuario=models.CharField(max_length=50)
    mensaje=models.TextField()

    def __str__(self):
        return self.usuario 

class MensajesEnviados(models.Model):
    usuario=models.CharField(max_length=50)
    mensaje=models.TextField()
    def __str__(self):
        return self.usuario

class Mensajes(models.Model):
    usuario=models.CharField(max_length=50)
    mensaje=models.TextField()
    def __str__(self):
        return self.usuario

