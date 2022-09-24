from django import forms

class MensajesFormulario(forms.Form):
    usuario=forms.CharField(max_length=50)
    mensajes=forms.CharField(max_length=1000)