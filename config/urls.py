from django.urls import path
from django.contrib import admin
from miapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('formulario/', views.formulario, name='formulario'),
    path('datos/', views.datos, name='datos'),
    path('admin/', admin.site.urls),
]