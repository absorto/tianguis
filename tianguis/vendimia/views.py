from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render
from django.shortcuts import redirect

from decimal import Decimal

from vendimia.models import *

import pprint

@staff_member_required
def gran_pedido(request, vendimia_id=None):
    v = Vendimia.objects.get( id = vendimia_id )
    return render_to_response('gran_pedido.html',
                              context_instance=RequestContext(request,
                                                              {'title': 'Gran Pedido: %s' % v,
                                                               'vendimia': v,
                                                               'pedido': v.gran_pedido()}))
    


@staff_member_required
def pedidos_vendimia(request, vendimia_id=None):
    v = Vendimia.objects.get( id = vendimia_id )

    return render_to_response('pedidos_vendimia.html',
                              context_instance=RequestContext(request,
                                                              {'title': 'Pedidos: %s' % v,
                                                               'vendimia': v,}))




@staff_member_required
def pedido_vendimia_user(request, vendimia_id, user_id):
    u = User.objects.get(id=user_id)
    v = Vendimia.objects.get(id=vendimia_id)
    pedidos = Pedido.objects.filter(oferta__vendimia=v,
                                    user=u)

    if request.method == "POST":
        pprint.pprint(request.POST)

    return render_to_response('pedidos_vendimia_usuario.html',
                              context_instance=RequestContext(request,
                                                              {'title': 'Orden: %s @ %s' % (u,v),
                                                               'vendimia': v,
                                                               'user': u,
                                                               'pedidos': pedidos}))








# url(r'^(?P<vendimia_id>\d)/ordenes/', orden_index),
@login_required
def orden_index(request,vendimia_id):
    v = Vendimia.objects.get(id=vendimia_id)
    ordenes = Orden.objects.filter(vendimia = v,
                                   user     = request.user)

    return render_to_response('orden_index.html',
                              context_instance=RequestContext(request,
                                                              {'title': 'Mis ordenes para %s' % v,
                                                               'vendimia': v,
                                                               'ordenes': ordenes,}))


# url(r'^(?P<vendimia_id>\d)/ordenes/nueva', orden_nueva),
@login_required
def orden_nueva (request, vendimia_id):
    v = Vendimia.objects.get (id = vendimia_id)
    mis_ordenes = v.orden_set.filter(user=request.user)

    if request.method == 'GET':
        return render_to_response('orden_nueva.html',
                                  context_instance=RequestContext(request,
                                                                  {'title': 'Orden nueva',
                                                                   'mis_ordenes': mis_ordenes,
                                                                   'vendimia': v,}))
    elif request.method == 'POST':
        o = Orden.objects.create(user     = request.user,
                                 vendimia = v )

        for p_id in request.POST:
            if p_id != 'csrfmiddlewaretoken':
                try:
                    producto = Producto.objects.get(id=int(p_id.split('_')[1]))
                    cantidad = Decimal(request.POST[p_id])
                    Pedido.objects.create(orden=o,
                                          producto=producto,
                                          cantidad=cantidad)
                except:
                    pass

        # redirigir a la orden recien creada
        return redirect("/vendimia/%s/" % vendimia_id)


# url(r'^(?P<vendimia_id>\d)/ordenes/(?P<orden_id>\d)', get_orden),
@login_required
def get_orden(request,vendimia_id, orden_id):
    v = Vendimia.objects.get (id = orden_id)
    o = Orden.objects.get (id = orden_id)
    return render_to_response('orden.html',
                              context_instance=RequestContext(request,
                                                              {'title': 'Mis ordenes para %s' % v,
                                                               'vendimia': v,
                                                               'orden': o,}))

