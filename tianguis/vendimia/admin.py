from django.contrib import admin

from vendimia.models import *

def duplica_vendimia(modeladmin, request, queryset):
    for v in queryset:
        vendimia = Vendimia.objects.create( cierre = v.cierre,
                                            entrega_inicio = v.entrega_inicio,
                                            entrega_fin    = v.entrega_fin,
                                            tienda = v.tienda )
        for o in Oferta.objects.filter( vendimia = v):
            oferta = Oferta.objects.create( producto = o.producto,
                                            precio   = o.precio,
                                            vendimia = vendimia )

duplica_vendimia.short_description = "Crea una nueva vendimia con las mismas ofertas y fechas"


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
                    'liga_a_pedidos',
                    'liga_a_gran_pedido')
    actions = [duplica_vendimia]

admin.site.register( Producto )
admin.site.register( Vendimia, VendimiaAdmin )
admin.site.register( Tienda )

