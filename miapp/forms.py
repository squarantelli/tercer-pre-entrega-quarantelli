from django import forms

class FormularioDatos(forms.Form):
    pais_de_origen = forms.CharField(max_length=50)
    nombre = forms.CharField(max_length=50)
    apellido = forms.CharField(max_length=50)
    dni = forms.CharField(max_length=50)