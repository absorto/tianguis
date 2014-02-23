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

    def gran_pedido(self):
        pedidos = Pedido.objects.filter(oferta__vendimia=self)
        gp = {}
        for p in pedidos:
            if p.oferta.producto in gp:
                gp[p.oferta.producto] += p.cantidad
            else:
                gp[p.oferta.producto] = p.cantidad
        return gp


    def users(self):
        return list(set([p.user for p in Pedido.objects.filter(oferta__vendimia=self)]))

    def ordenes(self):
        ordenes = {}
        for u in self.users():
            ordenes[u] = Pedido.objects.filter(oferta__vendimia=self, user=u)
        return ordenes


    def liga_a_pedidos(self):
        return "<a href='%s/pedidos/'>pedidos</a>" % self.id
    liga_a_pedidos.short_description = 'Pedidos'
    liga_a_pedidos.allow_tags = True


    def liga_a_gran_pedido(self):
        return "<a href='%s/gran_pedido/'>proveedores</a>" % self.id
    liga_a_gran_pedido.short_description = 'Gran Pedido'
    liga_a_gran_pedido.allow_tags = True


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


