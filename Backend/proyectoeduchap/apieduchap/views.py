from django.shortcuts import render
from django.shortcuts import render
from apieduchap.models import *
from rest_framework import generics
from .serializers import *
from rest_framework.decorators import permission_classes
from apieduchap.permissions import IsPostOrIsAuthenticated

#Con def creamos funciones
 #Universidad

class UniversidadList(generics.ListCreateAPIView):
 serializer_class = UniversidadSerializer
 queryset = Universidad.objects.all()
class UniversidadDetail(generics.RetrieveUpdateDestroyAPIView):
 serializer_class = UniversidadSerializer
 queryset = Universidad.objects.all()

 #Carrera

class CarreraList(generics.ListCreateAPIView):
 serializer_class = CarreraSerializer
 queryset = Carrera.objects.all()
class CarreraDetail(generics.RetrieveUpdateDestroyAPIView):
 serializer_class = CarreraSerializer
 queryset = Carrera.objects.all()

@permission_classes((IsPostOrIsAuthenticated, ))
class UsuarioList(generics.ListCreateAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()
class UsuarioDetail(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UsuarioSerializer
    queryset = Usuario.objects.all()