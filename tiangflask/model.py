# coding: utf-8
from lxml.html.builder import HTML, HEAD, BODY, H1, H2, P, A, TITLE, \
    LINK, SCRIPT, DIV, TH, THEAD, TBODY, TD, TR, TABLE, I, INPUT, FORM, BUTTON, \
    LABEL, TEXTAREA
from mongoengine import connect, Document, EmbeddedDocument, EmailField, \
    StringField, DecimalField, ReferenceField, DateTimeField, ListField, \
    EmbeddedDocumentField
import datetime
connect('tianguis')


class Marchante(Document):
    email = EmailField(required=True)
    nombre = StringField(max_length=50)
    login = StringField(max_length=50)

    def as_a(self):
        return A(self.login,
                 href="/marchante/%s" % str(self.pk))

    def __repr__(self):
        return str(self.login)


class Item(EmbeddedDocument):
    """
    cosa que se vende o se compra
    """
    nombre = StringField(required=True)
    descripcion = StringField(required=True)
    unidad = StringField()
    precio = DecimalField(required=True)

    def as_div(self):
        return DIV(H2(self.nombre),
                   P(self.descripcion,
                     "$%02.2d" % self.precio,
                     self.unidad))

    def as_tr(self):
        return TR(TD(self.nombre),
                  TD(self.descripcion),
                  TD("$%02.2d" % self.precio),
                  TD(self.unidad if self.unidad is not None else ""))


class Anuncio(Document):
    """
    Anuncio es el término general para los casos particulares de
    anuncio que son ofertas y demandas. O sea, un anuncio es una
    oferta o una demanda.
    """
    marchante = ReferenceField(Marchante)
    descripcion = StringField(required=True)
    titulo = StringField(required=True)
    fecha_inicio = DateTimeField(required=False,
                                 default=datetime.datetime.now())
    fecha_fin = DateTimeField(required=False,
                              default=datetime.datetime.now()
                              + datetime.timedelta(days=5))
    items = ListField(EmbeddedDocumentField(Item))

    meta = {'allow_inheritance': True}

    def edit_form(self):
        return DIV(FORM(DIV(LABEL(u"Título"),
                            INPUT(TYPE="text",
                                  name="titulo",
                                  placeholder=u"título",
                                  value="" if self.titulo is None
                                  else self.titulo),
                            CLASS="field"),
                        DIV(LABEL(u"Descripción"),
                            TEXTAREA("" if self.descripcion is None
                                     else self.descripcion, name="descripcion",
                                     placeholder=u"describe acá la vendimia",
                                     rows="2"),
                            CLASS="field"),
                        DIV(LABEL(u"Desde"),
                            INPUT(TYPE="text",
                                  name="fecha_inicio",
                                  placeholder=u"título",
                                  value=""),
                            CLASS="field"),
                        DIV(LABEL(u"Hasta"),
                            INPUT(TYPE="text",
                                  name="fecha_fin",
                                  placeholder=u"título"),
                            CLASS="field"),
                        BUTTON('guardar',
                               CLASS="ui primary button",
                               TYPE="submit"),
                        method="POST",
                        CLASS="ui form"),
                   CLASS="ui input")

    def as_div(self):
        return DIV(A("editar",
                     href="/oferta/editar/%s" % str(self.pk)),
                   H1(self.titulo),
                   P(self.descripcion),
                   P('publicado por ', self.marchante.as_a()),
                   P('disponible desde %s' % self.fecha_inicio,
                     " hasta %s" % self.fecha_fin
                     if self.fecha_fin is not None else ""),
                   self.items_table())

    def items_table(self):
        item_rows = [i.as_tr() for i in self.items]
        return TABLE(
            THEAD(
                TH('nombre'), TH('descripcion'), TH('precio'), TH('unidad')),
            TBODY(
                *item_rows),
            CLASS="ui table")

    def as_tr(self):
        return TR(TD(A(self.titulo,
                       href="/anuncio/%s" % str(self.pk))),
                  TD(self.descripcion),
                  TD(self.marchante.as_a()),
                  TD(str(self.fecha_inicio)))


class Oferta(Anuncio):
    """
    Un producto o servicio que se ofrece, en términos muy generales,
    como cuando se habla de la ley de la oferta y la demanda.
    """


class Demanda(Anuncio):
    """
    La contraparte de una oferta. En las relaciones de mercado que nos
    imaginamos, también los compradores anuncian "¡se compra, se compra!"
    lo mismo que ahora sólo los vendedores anuncian "¡se vende, se vende!".

    No confundir con lo que hacen los abogados.
    """


def oferta_table():
    trs = [o.as_tr() for o in Oferta.objects()]
    return DIV(A("crear oferta", href="/oferta/editar/nueva"),
               TABLE(
                   THEAD(
                       TH('titulo'),
                       TH('descripcion'),
                       TH('marchante'),
                       TH('fecha_inicio')),
                   TBODY(
                       *trs),
                   CLASS="ui center aligned table"))


def demanda_table():
    trs = [o.as_tr() for o in Demanda.objects()]
    return DIV(A("crear demanda", href="/demanda/crear"),
               TABLE(
                   THEAD(
                       TH('titulo'),
                       TH('descripcion'),
                       TH('marchante'),
                       TH('fecha_inicio')),
                   TBODY(
                       *trs),
                   CLASS="ui center aligned table"))
