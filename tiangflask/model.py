# coding: utf-8
from lxml.html.builder import HTML, HEAD, BODY, H1, H2, P, A, TITLE, \
    LINK, SCRIPT, DIV, TH, THEAD, TBODY, TD, TR, TABLE, I, INPUT, FORM, BUTTON, \
    LABEL, TEXTAREA, H3
from mongoengine import connect, Document, EmbeddedDocument, EmailField, \
    StringField, DecimalField, ReferenceField, DateTimeField, ListField, \
    EmbeddedDocumentField
import json
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

    def __repr__(self):
        return u"<item %s>" % self.nombre

    def as_div(self):
        return DIV(H2(self.nombre),
                   P(self.descripcion,
                     "$%02.2d" % self.precio,
                     self.unidad))

    def as_tr(self):
        return TR(TD(self.nombre),
                  TD(self.descripcion),
                  TD("$%02.2f" % self.precio),
                  TD(self.unidad if self.unidad is not None else ""),
                  TD(A('x', href="item/%s/elimina" % self)))

    def edit_form(self):
        rules = {
            'fields': {
                'nombre': {
                    'identifier': 'nombre',
                    'rules': [
                        {'type': 'empty',
                         'prompt': 'Por favor nombre su item'}
                    ]
                },
                'descripcion': {
                    'identifier': 'descripcion',
                    'rules': [
                        {'type': 'empty',
                         'prompt': 'Por favor describa su item'}
                    ]
                },
                'precio': {
                    'identifier': 'precio',
                    'rules': [
                        {'type': 'decimal',
                         'prompt': 'Comercio con moneda'}
                    ]
                }
            }
        }

        script = "$('.ui.form').form(%s)" % json.dumps(rules)
        return DIV(FORM(DIV(LABEL(u"Nombre"),
                            INPUT(TYPE="text",
                                  name="nombre",
                                  placeholder=u"nombre",
                                  value="" if self.nombre is None
                                  else self.titulo),
                            CLASS="field"),
                        DIV(LABEL(u"Descripción"),
                            TEXTAREA("" if self.descripcion is None
                                     else self.descripcion, name="descripcion",
                                     placeholder=u"describe acá el item",
                                     rows="2"),
                            CLASS="field"),
                        DIV(LABEL(u"precio"),
                            INPUT(TYPE="text",
                                  name="precio",
                                  placeholder=u"precio",
                                  value=""),
                            CLASS="field"),
                        DIV(LABEL(u"unidad"),
                            INPUT(TYPE="text",
                                  name="unidad",
                                  placeholder=u"título"),
                            CLASS="field"),
                        DIV('agregar',
                            CLASS="ui primary submit button"),
                        DIV(CLASS="ui error message"),
                        method="POST",
                        CLASS="ui form"),
                   SCRIPT(script))


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

    def as_div(self, item=None):
        return DIV(H3(self.titulo, CLASS="ui top attached header"),
                   DIV(A("editar",
                         href="/anuncio/editar/%s" % str(self.pk)),
                       P(self.descripcion),
                       P('publicado por ', self.marchante.as_a()),
                       P('disponible desde %s' % self.fecha_inicio,
                         " hasta %s" % self.fecha_fin
                         if self.fecha_fin is not None else ""),
                       A("agrega item", href="%s/item/agrega" % self.pk)
                       if item is None
                       else item.edit_form(),
                       self.items_table(),
                       CLASS='ui attached segment'))

    def items_table(self):
        item_rows = []
        for i in self.items:
            item_rows.append(TR(TD(i.nombre),
                                TD(i.descripcion),
                                TD("$%02.2f" % i.precio),
                                TD(i.unidad if i.unidad is not None else ""),
                                TD(A('x',
                                     href="/anuncio/%s/item/%s/elimina"
                                     % (self.pk,self.items.index(i))))))
        return TABLE(
            THEAD(
                TH('nombre'), TH('descripcion'),
                TH('precio'), TH('unidad'), TH()),
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
    return DIV(TABLE(
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
