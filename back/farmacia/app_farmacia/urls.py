from django.urls import path, include
from rest_framework import routers
from app_farmacia.views import RolViewSet, EstadoViewSet, UsuariosViewSet, ProveedoresViewSet, IngresoViewSet, OrdenViewSet, CategoriaViewSet, EnvioViewSet, ArticulosViewSet, DetalleVentaViewSet, DetalleIngresoViewSet
from app_farmacia import views

from knox import views as know_views
from .views import LoginAPI
from .views import RegisterAPI


routers=routers.DefaultRouter()
routers.register(r'ROL', views.RolViewSet)
routers.register(r'Estados', views.EstadoViewSet)
routers.register(r'USUARIOS',views.UsuariosViewSet)
routers.register(r'Proveedores', views.ProveedoresViewSet)
routers.register(r'Ingreso', views.IngresoViewSet)
routers.register(r'Orden', views.OrdenViewSet)
routers.register(r'Categoria', views.CategoriaViewSet)
routers.register(r'Envio', views.EnvioViewSet)
routers.register(r'Articulos', views.ArticulosViewSet)
routers.register(r'DetalleVenta', views.DetalleVentaViewSet)
routers.register(r'DetalleIngreso', views.DetalleIngresoViewSet)
#routers.register(r'SuperAdmin', views.SuperAdminRegistrationView)
#routers.register(r'Admin', views.AdminRegistrationView)
#routers.register(r'User', views.UserRegistrationView)


urlpatterns =[
    path('',include(routers.urls)),

    path('registro', RegisterAPI.as_view(), name='register'),
    path('login', LoginAPI.as_view(), name='login'),
    path('logout', know_views.LogoutAllView.as_view(), name='logoutall')
]


