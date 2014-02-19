from django.contrib import admin

from vendimia.models import *

admin.site.register( Producto )
admin.site.register( Vendimia )
admin.site.register( Oferta )
admin.site.register( Pedido )

