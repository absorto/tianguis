from lxml.html.builder import HTML, HEAD, BODY, H1, H2, P, A, TITLE, LINK, SCRIPT, DIV, TH, THEAD, TBODY, TD, TR, TABLE, I, INPUT, SPAN
from lxml.html import tostring

from pprint import pformat


def pag_estandar(title, body):
    return tostring(
        HTML(
            HEAD(
                TITLE(title),
                # aqui semantic
                SCRIPT(src="/static/bower_components/jquery/dist/jquery.min.js"),
                LINK(type="text/css", rel="stylesheet", href="/static/semantic/dist/semantic.min.css"),
                LINK(type="text/css", rel="stylesheet", href="static/semantic/dist/components/dropdown.min.css"),
                SCRIPT(src="/static/semantic/dist/semantic.min.js"),
                SCRIPT(src="/static/semantic/dist/components/dropdown.min.js")
            ),
            BODY( main_menu(), body(), style="margin: 2em" )
        ),
        pretty_print=True)



def main_menu():
    return DIV(DIV(SPAN("Oferta", CLASS="text"), I(CLASS="dropdown icon"),
                   DIV(A("ver ofertas", href="/oferta/", CLASS="item"),
                       A("crear oferta", href="/anuncio/editar/nueva", CLASS="item"),
                       A("buscar", href="/oferta/buscar", CLASS="item"),
                       CLASS="menu"),
                   CLASS="ui pointing dropdown link item"),
               SCRIPT("$('.ui.dropdown').dropdown({on: 'hover'});"),
               CLASS="ui menu")

def anuncios_table(anuncios):
    a_tr = [anuncio2tr(a) for a in anuncios]
    return TABLE(
        THEAD(
            TH('titulo'), TH('descripcion'), TH('autor'), TH('fecha_creacion')),
        TBODY(
            *a_tr),
        CLASS="ui center aligned table")


def anuncio2tr(a):
    return TR( TD( A( a['titulo'],
                      href=str(a['_id']))),
               TD( a['descripcion'] ),
               TD( a['autor'] ),
               TD( str(a['fecha_creacion'] )))


def anuncio2div(a):
    header = [H1(a['titulo']),
              P(a['descripcion']),
              P('publicado por %s' % a['autor']),
              P('disponible desde %s' % a['fecha_creacion'],
                "hasta %s" % a['fecha_expiracion'] if a['fecha_expiracion'] != None else "")
              ]

    items = [item2div(i) for i in a['items']]

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
