from django.contrib import admin
from .models import Estado, Producto

class ProductoAdmin(admin.ModelAdmin):
    list_display = ["nombre", "valor", "descripcion", "stock", "estado"]
    search_fields = ["nombre"]
    list_filter = ["estado"]
    list_per_page = 12

admin.site.register(Estado)
admin.site.register(Producto, ProductoAdmin)