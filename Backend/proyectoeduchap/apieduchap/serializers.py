from rest_framework import serializers
from apieduchap.models import *
from django.contrib.auth.models import User


class CarreraSerializer(serializers.ModelSerializer):
 class Meta:
    model = Carrera
    fields = ('nombre','creditos','snes','horario')

class UniversidadSerializer(serializers.ModelSerializer):
 class Meta:
    model = Universidad
    fields = ('nombre','sede','direccion','telefono','correo','url',)

class UsuarioSerializer(serializers.ModelSerializer):
    username = serializers.CharField(write_only=True, source="user.username")
    password = serializers.CharField(write_only=True, source="user.password")
    nombre = serializers.CharField(required=False)
    apellido = serializers.CharField(required=False)
    correo = serializers.CharField(required=False)
    fecha_nacimiento = serializers.DateField(required=False)
    telefono = serializers.CharField(required=False)
    #category_name = serializers.RelatedField(source='category',read_only=True)
    class Meta:
        model = User
        fields = ('id', 'username', 'password', 'nombre', 'apellido','correo', 'fecha_nacimiento', 'telefono')
    def create(self, validated_data, instance=None):
        user_data = validated_data.pop('user')
        user = User.objects.create(**user_data)
        user.set_password(user_data['password'])
        user.save()
        Usuario.objects.update_or_create(user=user,**validated_data)
        usuario = Usuario.objects.get(user=user)
        return usuario



