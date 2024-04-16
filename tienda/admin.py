from django.contrib import admin

# Register your models here.
from .models import Categoria
from .models import Producto
from .models import Cliente
from .models import Direccion

@admin.register(Categoria)
class CategoriaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'pub_date']

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'stock', 'precio', 'Categoria', 'pub_date']

@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'apellidos', 'dni', 'telefono', 'direccion', 'email', 'f_nacimiento', 'f_publicacion']

@admin.register(Direccion)
class DireccionAdmin(admin.ModelAdmin):
    list_display = ['nombre_calle', 'manzana', 'barrio', 'numero_lote']