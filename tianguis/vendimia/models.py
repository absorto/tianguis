from django.contrib.auth.models import User
from django.db import models
import datetime

class Producto(models.Model):
    nombre      = models.CharField(max_length=200)
    descripcion = models.CharField(max_length=200, null=True, blank=True)
    unidad      = models.CharField('unidad en la que se vende el producto', max_length=20)
    foto        = models.ImageField(null=True, blank=True, upload_to="productos" )

    def __unicode__(self):
        return self.nombre


class Tienda(models.Model):
    nombre    = models.CharField('Local donde se entregan pedidos', max_length=200)
    ubicacion = models.URLField('URL de un mapa de la ubicacion del local', null=True, blank=True)

    def __unicode__(self):
        return self.nombre

    
class Vendimia(models.Model):
    cierre = models.DateTimeField('Fecha de cierre')
    entrega_inicio = models.DateTimeField('Inicia lapso de entregas')
    entrega_fin    = models.DateTimeField('Termina lapso de entregas')

    tienda = models.ForeignKey(Tienda)

    def status(self):
        now = datetime.datetime.now(self.cierre.tzinfo)
        
        if now < self.cierre:
            status = ["recibiendo pedidos"]
        else:
            status = ["cerrada"]

        if now >= self.entrega_inicio and now <= self.entrega_fin:
            status.append( "entregando" )

        if now > self.entrega_fin:
            status.append( "finalizada" )

        return " | ".join(status)

    def __unicode__(self):
        return "%s [%s]" % (self.tienda.nombre, self.status())

class Oferta(models.Model):
    producto = models.ForeignKey(Producto)
    vendimia = models.ForeignKey(Vendimia)
    precio   = models.DecimalField(decimal_places=2, max_digits=5)

    def __unicode__(self):
        return ("%s $%s @%s") % (self.producto.nombre, self.precio, self.vendimia)

class Pedido(models.Model):
    oferta   = models.ForeignKey(Oferta)
    cantidad = models.DecimalField(decimal_places=2,
                                   max_digits=5)
    user = models.ForeignKey(User)
    estado   = models.CharField(max_length=10,
                                choices = ( ('cancelado', 'cancelado'),
                                            ('pendiente', 'pendiente'),
                                            ('entregado', 'entregado'),
                                            ('pagado', 'pagado'), ),
                                default = 'pendiente' )
    # usuario
    fecha_ordenado  = models.DateTimeField(auto_now_add=True)
    fecha_entregado = models.DateTimeField(blank=True, null=True)
    precio_venta    = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    
    def __unicode__(self):
        return "%s [%s]" % (self.oferta.producto.nombre, self.estado)
