from unittest.util import _MAX_LENGTH
from django.db import models

# Create your models here.
class MensajesRecibidos(models.Model):
    nombre=models.CharField(max_length=50)
    mensaje=models.CharField(max_length=250)

class MensajesEnviados(models.Model):
    nombre=models.CharField(max_length=50)
    mensaje=models.CharField(max_length=250)
    

