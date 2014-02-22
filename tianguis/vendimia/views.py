from django.shortcuts import render_to_response
from django.shortcuts import render

from vendimia.models import *



def hola(request):
    return render_to_response('seccion_a.html', {'saludo': "hola como estas"})


def adios(request):
    
    return render_to_response('seccion_a.html', {'saludo': "ba bai"})



def pedidos(request):
    pedidos = Pedido.objects.all()
    return render_to_response('pedidos.html',
                              {'titulo': "Todos los pedidos",
                               'pedidos': pedidos })
                                           
