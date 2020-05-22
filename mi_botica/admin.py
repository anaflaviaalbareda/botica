from django.contrib import admin
from .models import *

# Register your models here.

#class AlmuerzosAdmin(admin.ModelAdmin):
#	list_display = ('almuerzos_id','fecha','nombre','telefono','direccion','opcion')

#admin.site.register(Almuerzos,AlmuerzosAdmin)

class CarritoHasAdmin(admin.ModelAdmin):
	list_display=('carrito_idcarrito','cantidad','subtotal','presentacion','producto')

admin.site.register(CarritoHasProducto,CarritoHasAdmin)

class CarritoAdmin(admin.ModelAdmin):
	list_display=('idcarrito','cantidad_productos','total')

admin.site.register(Carrito,CarritoAdmin)

class ProductosAdmin(admin.ModelAdmin):
	list_display=('idproductos','descripcion')

admin.site.register(Producto,ProductosAdmin)

class PresentacionAdmin(admin.ModelAdmin):
	list_display=('idpresentacion','nombre')

admin.site.register(Presentacion,PresentacionAdmin)