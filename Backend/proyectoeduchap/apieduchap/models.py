from django.db import models
from django.contrib.auth.models import User

class Usuario(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=50)
    apellido = models.CharField(max_length=50)
    telefono = models.CharField(max_length=50)
    correo = models.EmailField(max_length=50)
    fecha_nacimiento = models.DateField()
    def __str__(self):
        return self.nombre

class Carrera(models.Model):
    nombre = models.CharField(max_length=50)
    creditos = models.CharField(max_length=50)
    snes = models.CharField(max_length=50)
    horario = models.CharField(max_length=50)
    def __str__(self):
        return self.nombre
class Universidad(models.Model):
    nombre = models.CharField(max_length=50)
    sede = models.CharField(max_length=50)
    direccion = models.CharField(max_length=100)
    telefono = models.CharField(max_length=10)
    correo = models.CharField(max_length=100)
    carrera= models.ManyToManyField(Carrera,blank=True, null=True)
    url = models.CharField(max_length=100)
    def __str__(self):
        return self.nombre