from rest_framework import serializers
from .models import USUARIOS
from .models import ROL, estados, Proveedores, Ingreso, Orden, Categoria, Envio, Articulos, DetalleVenta, DetalleIngreso
#from .models import SuperAdmin, Admin, User
from django.contrib.auth.models import User

class RolSerializer(serializers.ModelSerializer):
    class Meta:
        model=ROL
        fields='__all__'

class EstadosSerializer(serializers.ModelSerializer):
    class Meta:
        model=estados
        fields='__all__'

class UsuariosSerializer(serializers.ModelSerializer):
    class Meta:
        model=USUARIOS
        fields= '__all__'

class ProveedoresSerializer(serializers.ModelSerializer):
    class Meta:
        model=Proveedores
        fields='__all__'

class IngresoSerializer(serializers.ModelSerializer):
    class Meta:
        model=Ingreso
        fields='__all__'

class OrdenSerializer(serializers.ModelSerializer):
    class Meta:
        model= Orden
        fields='__all__'

class CategoriaSerializer(serializers.ModelSerializer):
    class Meta:
        model= Categoria
        fields='__all__'

class EnvioSerializer(serializers.ModelSerializer):
    class Meta:
        model=Envio
        fields='__all__'

class ArticulosSerializer(serializers.ModelSerializer):
    class Meta:
        model=Articulos
        fields='__all__'

class DetalleVentaSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetalleVenta
        fields='__all__'

class DetalleIngresosSerializer(serializers.ModelSerializer):
    class Meta:
        model=DetalleIngreso
        fields='__all__'

#-------------------------------
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field = ('id', 'username', 'email')

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        field= ('id', 'username','email', 'password')
        extra_kwarg={'password': {'write_only':True}}

    def create(self, validated_data):
        #user=user.objects.create_user(validated_data['username'], validated_data['email'])

        return User.objects.create_user(**validated_data)

