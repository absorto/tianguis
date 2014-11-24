#coding: utf-8
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
            status = ["recibiendo ordenes"]
        else:
            status = ["cerrada"]

        if now >= self.entrega_inicio and now <= self.entrega_fin:
            status.append( "entregando" )

        if now > self.entrega_fin:
            status = [ "finalizada", ]

        return status

    def __unicode__(self):
        if "recibiendo_ordenes" in self.status():
            fecha = cierre.strftime('%d %b %Y %H:%M')
        elif "cerrada" in self.status() and "entregando" in self.status() or "finalizada" in self.status():
            fecha = self.entrega_fin.strftime('%d %b %Y %H:%M')
        else:
            fecha = self.entrega_inicio.strftime('%d %b %Y %H:%M')

        return "%s[%s]->[%s]" % (self.tienda.nombre, " | ".join(self.status()), fecha)

    def gran_pedido(self):
        pedidos = Pedido.objects.filter(orden__vendimia=self)
        gp = {}
        for p in pedidos:
            if p.producto in gp:
                gp[p.producto] += p.cantidad
            else:
                gp[p.producto] = p.cantidad
        return gp


    def users(self):
        return list(set([p.user for p in Pedido.objects.filter(oferta__vendimia=self)]))

    def liga_a_pedidos(self):
        return "<a href='%s/pedidos/'>%s pedidos</a>" % (self.id, len(self.users()))
    liga_a_pedidos.short_description = 'Pedidos'
    liga_a_pedidos.allow_tags = True


    def liga_a_gran_pedido(self):
        return "<a href='%s/gran_pedido/'>proveedores</a>" % self.id
    liga_a_gran_pedido.short_description = 'Gran Pedido'
    liga_a_gran_pedido.allow_tags = True






class Oferta(models.Model):
    producto = models.ForeignKey(Producto)
    vendimia = models.ForeignKey(Vendimia)
    precio   = models.DecimalField(decimal_places=2, max_digits=5)

    def __unicode__(self):
        return ("%s $%s @%s") % (self.producto.nombre, self.precio, self.vendimia)





class Orden(models.Model):
    fecha           = models.DateTimeField(auto_now_add=True)
    user            = models.ForeignKey(User)
    estado          = models.CharField(max_length=10,
                                choices = ( ('cancelado', 'cancelado'),
                                            ('pendiente', 'pendiente'),
                                            ('entregado', 'entregado'),
                                            ('pagado', 'pagado'), ),
                                default = 'pendiente' )
    vendimia        = models.ForeignKey(Vendimia)

    def __unicode__(self):
        return "%s %s %s" % (self.user, self.estado, self.vendimia)

    class Meta:
        verbose_name_plural = "órdenes"


class Pedido(models.Model):
    orden    = models.ForeignKey(Orden)
    producto = models.ForeignKey(Producto)
    cantidad = models.DecimalField(decimal_places=2,
                                   max_digits=5)

    precio_venta    = models.DecimalField(decimal_places=2, max_digits=5, blank=True, null=True)
    
    # def __unicode__(self):
    #     return "%s [%s]" % (self.oferta.producto.nombre, self.estado)
