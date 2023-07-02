from django.contrib import admin
from django.contrib import admin
from .models import USUARIOS
from .models import ROL
from .models import Articulos
from .models import Categoria
from .models import estados
from .models import Proveedores
from .models import Ingreso
from .models import Orden
from .models import Envio
from .models import DetalleVenta
from .models import DetalleIngreso
#from .models import *




class ROLADMIN(admin.ModelAdmin):
    list_display=["idrol","detalle"]

class USUARIOADMIN(admin.ModelAdmin):
    list_display=('nombre','idrol')

class CategoriaADMIN(admin.ModelAdmin):
    list_display=('idcategoria','nombre','descripcion')

class ArticulosADMIN(admin.ModelAdmin):
    list_display=('idarticulo', 'nombre', 'descripcion', 'precio', 'stock', 'imagen','precio','idcategoria')

class EstadosADMIN(admin.ModelAdmin):
    list_display=('idestados', 'detalle')

class ProveedoresADMIN(admin.ModelAdmin):
    list_display=('idproveedor', 'nombre')

class IngresosADMIN(admin.ModelAdmin):
    list_display=('idingreso', 'idproveedor', 'tipoComprobante', 'serieComprobante','numeroComprobante', 'fecha', 'total', 'estado')

class OrdenADMIN(admin.ModelAdmin):
    list_display=('idorden', 'usuario')

class EnvioADMIN(admin.ModelAdmin):
    list_display=('idenvio','descripcion','direccion_envio', 'fecha', 'cod_seguimiento', 'orden','estado')

class DetalleVentaADMIN(admin.ModelAdmin):
    list_display=('iddetalle','cantidad','precio', 'descuento', 'articulo', 'orden')    

class DetalleIngresoADMIN(admin.ModelAdmin):
    list_display=('iddetalle','cantidad', 'descripcion')    

"""class DetalleSuperAdmin(admin.ModelAdmin):
    list_display=('username', 'email','password')

class DetalleAdminUser(admin.ModelAdmin):
    list_display=('username', 'email','password')

class DetalleUser(admin.ModelAdmin):
    list_display=('username', 'email','password')

"""
admin.site.register(ROL, ROLADMIN)
admin.site.register(USUARIOS, USUARIOADMIN)
admin.site.register(Categoria,CategoriaADMIN)
admin.site.register(Articulos, ArticulosADMIN)
admin.site.register(estados, EstadosADMIN)
admin.site.register(Proveedores, ProveedoresADMIN)
admin.site.register(Ingreso, IngresosADMIN)
admin.site.register(Orden, OrdenADMIN)
admin.site.register(Envio, EnvioADMIN)
admin.site.register(DetalleIngreso, DetalleIngresoADMIN)
admin.site.register(DetalleVenta, DetalleVentaADMIN)
#admin.site.register(SuperAdmin, DetalleSuperAdmin)
#admin.site.register(Admin, DetalleAdminUser)
#admin.site.register(User, DetalleUser)