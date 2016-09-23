from datetime import datetime

from mongoengine import connect, Document, EmbeddedDocument, EmailField, \
    StringField, DecimalField, ReferenceField, DateTimeField, ListField, \
    EmbeddedDocumentField
connect('tianguis')


class User(Document):
    email = EmailField(required=True)
    first_name = StringField(max_length=50)
    last_name = StringField(max_length=50)


class Item(EmbeddedDocument):
    nombre = StringField(required=True)
    descripcion = StringField(required=True)
    unidad = StringField()
    precio = DecimalField(required=True)


class Anuncio(Document):
    """
    Anuncio es el término general para los casos particulares de
    anuncio que son ofertas y demandas. O sea, un anuncio es una
    oferta o una demanda.
    """
    autor = ReferenceField(User)
    descripcion = StringField(required=True)
    titulo = StringField(required=True)
    fecha_expiracion = DateTimeField(required=True)
    fecha_creacion = DateTimeField(required=True)
    items = ListField(EmbeddedDocumentField(Item))

    meta = {'allow_inheritance': True}


class Oferta(Anuncio):
    """
    Un producto o servicio que se ofrece, en términos muy generales,
    como cuando se habla de la ley de la oferta y la demanda.
    """


class Demanda(Anuncio):
    """
    La contraparte de una oferta. En las relaciones de mercado que nos
    imaginamos, también los compradores anuncian "¡se compra, se compra1"
    lo mismo que ahora sólo los vendedores anuncian "¡se vende, se vende".

    No confundir con lo que hacen los abogados.
    """
