from django.contrib import admin

from vendimia.models import *


class OfertaInline(admin.TabularInline):
    model = Oferta
    extra = 9

class VendimiaAdmin(admin.ModelAdmin):
    inlines = [OfertaInline]

admin.site.register( Producto )
admin.site.register( Vendimia, VendimiaAdmin )
admin.site.register( Pedido )
admin.site.register( Tienda )

