from django.shortcuts import render, redirect
from miapp.forms import FormularioDatos
from miapp.models import Pais, Cliente, Dni

def index(request):
    return render(request, 'miapp/index.html')

def formulario(request):
    if request.method == 'POST':
        form = FormularioDatos(request.POST)
        if form.is_valid():
            pais_de_origen = form.cleaned_data['pais_de_origen']
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            dni = form.cleaned_data['dni']

            nuevo_pais = Pais(pais_de_origen=pais_de_origen)
            nuevo_pais.save()

            nuevo_cliente = Cliente(nombre=nombre, apellido=apellido)
            nuevo_cliente.save()

            nuevo_dni = Dni(dni=dni)
            nuevo_dni.save()

            return redirect('datos')
    else:
        form = FormularioDatos()

    return render(request, 'miapp/formulario.html', {'form': form})

def datos(request):
    if request.method == 'POST':
        pais_de_origen = request.POST['pais_de_origen']
        nombre = request.POST['nombre']
        apellido = request.POST['apellido']
        dni = request.POST['dni']

        nuevo_pais = Pais(pais_de_origen=pais_de_origen)
        nuevo_pais.save()

        nuevo_cliente = Cliente(nombre=nombre, apellido=apellido)
        nuevo_cliente.save()

        nuevo_dni = Dni(dni=dni)
        nuevo_dni.save()

        datos = {
            'pais_de_origen': pais_de_origen,
            'nombre': nombre,
            'apellido': apellido,
            'dni': dni
        }

        return render(request, 'miapp/datos.html', datos)

    return redirect('index')