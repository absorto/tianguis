from lxml.html.builder import HTML, HEAD, BODY, H1, H2, P, A, TITLE, LINK, SCRIPT, DIV, TH, THEAD, TBODY, TD, TR, TABLE, I, INPUT
from lxml.html import tostring

from pprint import pformat


def pag_estandar(title, body):
    return tostring(
        HTML(
            HEAD(
                TITLE(title),
                # aqui semantic
                LINK(type="text/css", rel="stylesheet", href="/static/semantic/dist/semantic.min.css"),
                SCRIPT(src="/static/semantic/dist/semantic.min.js")),
            BODY( main_menu(), body(), style="margin: 2em" )
        ),
        pretty_print=True)



def main_menu():
    return DIV(
        A("Oferta", href="/oferta/", CLASS="item"),
        A("Demanda", href="/demanda/", CLASS="item"),
        DIV(
            DIV(
                DIV(
                    INPUT(placeholder="buscar...", type="text"),
                    I(CLASS="search link icon"),
                    CLASS="ui icon input"),
                CLASS="ui menu"),
            CLASS="item"),
        CLASS="ui three item menu")


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
