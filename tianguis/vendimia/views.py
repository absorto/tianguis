from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.template import RequestContext
from django.shortcuts import render_to_response
from django.shortcuts import render

from vendimia.models import *



def hola(request):
    return render_to_response('seccion_a.html', {'saludo': "hola como estas"})

def adios(request):
    return render_to_response('seccion_a.html', {'saludo': "ba bai"})


@staff_member_required
def gran_pedido(request, vendimia_id=None):
    v = Vendimia.objects.get( id = vendimia_id )
    import pprint
    pprint.pprint(v.gran_pedido())
    return render_to_response('gran_pedido.html',
                              context_instance=RequestContext(request,
                                                              {'title': 'Gran Pedido: %s' % v,
                                                               'pedido': v.gran_pedido()}))
    


@staff_member_required
def pedidos_vendimia(request, vendimia_id=None):
    v = Vendimia.objects.get( id = vendimia_id )

    return render_to_response('pedidos_vendimia.html',
                              context_instance=RequestContext(request,
                                                              {'title': 'Pedidos: %s' % v,
                                                               'ordenes': v.ordenes()}))



@staff_member_required
def pedido_vendimia_user(request, vendimia_id, user_id):
    u = User.objects.get(id=user_id)
    v = Vendimia.objects.get(id=vendimia_id)
    pedidos = Pedido.objects.filter(oferta__vendimia=v,
                                    user=u)
    return render_to_response('pedidos_vendimia_usuario.html',
                              context_instance=RequestContext(request,
                                                              {'title': 'Orden: %s @ %s' % (u,v),
                                                               'user': u,
                                                               'pedidos': pedidos}))
