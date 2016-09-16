from lxml.html.builder import HTML, HEAD, BODY, H1, H2, P, A, TITLE, DIV, TH, THEAD, TBODY, TD, TR, TABLE
from lxml.html import tostring

from pprint import pformat


def pag_estandar(title, body):
    return tostring(
        HTML(
            HEAD(
                TITLE(title),
                # aqui semantic
                ),
            BODY( body() )
        ),
        pretty_print=True)



import api as tngs

def anuncio2div(a):
    header = [H1(a['titulo']),
              P(a['descripcion']),
              P('publicado por %s' % a['autor']),
              P('disponible desde %s' % a['fecha_creacion'],
                "hasta %s" % a['fecha_expiracion'] if a['fecha_expiracion'] != None else "")
              ]

    items = [item2html(i) for i in a['items']]

    return DIV(
        *header + \
        items)



def item2div(i):
    return DIV(H2(i['nombre']),
               P(i['descripcion'],
                 "$%02.2d" % i['precio'],
                 i['unidad']))
        


def item2tr(i):
    return TR(TD( i['nombre'] ),
              TD( i['descripcion'] ),
              TD( "$%02.2d" % i['precio'] ),
              TD( i['unidad'] ))



def items_table(a):
    item_rows = [item2tr(i) for i in a['items']]
    return TABLE(
        THEAD(
            TH('nombre'), TH('descripcion'), TH('precio'), TH('unidad')),
        TBODY(
            *item_rows))
