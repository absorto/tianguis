from django.contrib import admin

from vendimia.models import *


class OfertaInline(admin.TabularInline):
    model = Oferta
    extra = 9



class VendimiaAdmin(admin.ModelAdmin):
    inlines = [OfertaInline]
    list_display = ('tienda',
                    'status',
                    'cierre',
                    'entrega_inicio',
                    'entrega_fin',
                    'liga_a_pedidos')

admin.site.register( Producto )
admin.site.register( Vendimia, VendimiaAdmin )
admin.site.register( Tienda )

