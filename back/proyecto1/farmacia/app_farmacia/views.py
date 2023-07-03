from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import generics, permissions 
#from rest_framework.permissions import AllowAny
#from rest_framework.views import APIView
from rest_framework.response import Response
from knox.models import AuthToken
from knox.views import LoginView as KnoxLoginView
from .serializer import UserSerializer, RegisterSerializer
from .serializer import UsuariosSerializer, RolSerializer, EstadosSerializer, ProveedoresSerializer, IngresoSerializer, OrdenSerializer, CategoriaSerializer, EnvioSerializer, ArticulosSerializer, DetalleVentaSerializer, DetalleIngresosSerializer
from .models import  ROL, estados, USUARIOS, Proveedores, Ingreso, Orden, Categoria, Envio, Articulos, DetalleVenta, DetalleIngreso
from django.contrib.auth import login



class RolViewSet(viewsets.ModelViewSet):
    queryset=ROL.objects.all()
    serializer_class=RolSerializer

class EstadoViewSet(viewsets.ModelViewSet):
    queryset=estados.objects.all()
    serializer_class=EstadosSerializer

class UsuariosViewSet(viewsets.ModelViewSet):
    queryset=USUARIOS.objects.all()
    serializer_class= UsuariosSerializer

class ProveedoresViewSet(viewsets.ModelViewSet):
    queryset=Proveedores.objects.all()
    serializer_class=ProveedoresSerializer

class IngresoViewSet(viewsets.ModelViewSet):
    queryset=Ingreso.objects.all()
    serializer_class=IngresoSerializer

class OrdenViewSet(viewsets.ModelViewSet):
    queryset=Orden.objects.all()
    serializer_class=OrdenSerializer

class CategoriaViewSet(viewsets.ModelViewSet):
    queryset=Categoria.objects.all()
    serializer_class=CategoriaSerializer

class EnvioViewSet(viewsets.ModelViewSet):
    queryset=Envio.objects.all()
    serializer_class=EnvioSerializer

class ArticulosViewSet(viewsets.ModelViewSet):
    queryset=Articulos.objects.all()
    serializer_class=ArticulosSerializer

class DetalleVentaViewSet(viewsets.ModelViewSet):
    queryset=DetalleVenta.objects.all()
    serializer_class=DetalleVentaSerializer

class DetalleIngresoViewSet(viewsets.ModelViewSet):
    queryset=DetalleIngreso.objects.all()
    serializer_class=DetalleIngresosSerializer




class RegisterAPI(generics.GenericAPIView):
    serializer_class= RegisterSerializer

    def post(self, request, *args, **kwargs):
        serializer= self.get_serializar(data=request.data)
        serializer.is_valid(raise_exception=True)
        user=serializer.save()
        return Response({
            "user": UserSerializer(user, context=self.get_serializer_context()).data,
            "token": AuthToken.objects.create(user)[1]
        })

class LoginAPI(KnoxLoginView):
    permissions_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer= AuthTokenSerializer(data=request.data)
        serializer.is_valid( raise_exception=True)
        user= serializer.validated_data['user']
        login(request, user)
        return super(LoginAPI, self).post(request, format=None)