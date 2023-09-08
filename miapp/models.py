from django.db import models

class Pais(models.Model):
    pais_de_origen = models.CharField(max_length=50)
    
    def __str__(self):
        return self.pais_de_origen

class Cliente(models.Model):
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

class Dni(models.Model):
    dni = models.CharField(max_length=50)
    
    def __str__(self):
        return self.dni
