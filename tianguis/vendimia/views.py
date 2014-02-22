from django.contrib.auth.decorators import login_required

from django.shortcuts import render_to_response
from django.shortcuts import render

from vendimia.models import *



def hola(request):
    return render_to_response('seccion_a.html', {'saludo': "hola como estas"})


def adios(request):
    
    return render_to_response('seccion_a.html', {'saludo': "ba bai"})


@login_required
def pedidos(request):
    pedidos = Pedido.objects.all()
    return render_to_response('pedidos.html',
                              {'titulo': "Todos los pedidos",
                               'pedidos': pedidos })
                                           
