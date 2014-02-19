from django.db import models


class Producto(models.Model):
    nombre      = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    unidad      = models.CharField('unidad en la que se vende el producto', max_length=20)
    foto        = models.ImageField(null=True, blank=True, upload_to="productos" )

    def __unicode__(self):
        return self.nombre

class Vendimia(models.Model):
    cierre = models.DateTimeField('Fecha de cierre')
    entrega_inicio = models.DateTimeField('Inicia lapso de entregas')
    entrega_fin    = models.DateTimeField('Termina lapso de entregas')
    local          = models.CharField('Local donde se entregan pedidos', max_length=200)
    ubicacion      = models.URLField('URL de un mapa de la ubicacion del local', null=True, blank=True)

    def __unicode__(self):
        return self.local

class Oferta(models.Model):
    producto = models.ForeignKey(Producto)
    vendimia = models.ForeignKey(Vendimia)
    precio   = models.DecimalField(decimal_places=2, max_digits=5)

    def __unicode__(self):
        return self.producto.nombre

class Pedido(models.Model):
    oferta   = models.ForeignKey(Oferta)
    cantidad = models.DecimalField(decimal_places=2,
                                   max_digits=5)
    estado   = models.CharField(max_length=10,
                                choices = ( ('cancelado', 'cancelado'),
                                            ('pendiente', 'pendiente'),
                                            ('entregado', 'entregado'),
                                            ('pagado', 'pagado'), ),
                                default = 'pendiente' )
    # usuario
    fecha_ordenado  = models.DateTimeField(auto_now_add=True)
    fecha_entregado = models.DateTimeField()
    precio_venta    = models.DecimalField(decimal_places=2, max_digits=5)
    
    def __unicode__(self):
        return "%s [%s]" % (self.oferta.producto.nombre, self.estado)
