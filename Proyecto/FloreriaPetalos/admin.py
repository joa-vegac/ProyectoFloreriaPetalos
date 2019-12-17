from django.contrib import admin
from .models import Estado, Producto, Categoria

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "valor", "descripcion", "stock", "estado", "categoria"]
    search_fields = ["nombre"]
    list_filter = ["estado","categoria", "created_date"]
    list_per_page = 12

admin.site.register(Estado)
admin.site.register(Categoria)
admin.site.register(Producto, ProductoAdmin)