from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class MensajesRecibidos(models.Model):
    nombre=models.CharField(max_length=50)
    mensaje=models.CharField(max_length=250)

    def __str__(self):
        return self.nombre

class MensajesEnviados(models.Model):
    nombre=models.CharField(max_length=50)
    mensaje=models.CharField(max_length=250)
    
    def __str__(self):
        return self.nombre

