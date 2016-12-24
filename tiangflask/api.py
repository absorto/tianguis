from datetime import datetime
import pymongo
from bson.objectid import ObjectId
client = pymongo.MongoClient("localhost", 27017)
db = client.tianguis




def anuncio_guardar(anuncio):
    return db.anuncios.save(anuncio)





def anuncio_publicar( anuncio ):
    anuncio['status'] = 'publicado'
    db.anuncios.save(anuncio)



def anuncio_por_id( aid ):
    """
    devuelve un anuncio si le das un ID
    """
    return db.anuncios.find_one( ObjectId(aid) )



def anuncios_publicados():
    """ 
    lista de todos los anuncios publicados 
    """
    publicados = []
    for a in db.anuncios.find({"status": "publicado"}):
        publicados.append(a)
    return publicados



def anuncio_crear( autor, titulo, fecha_expiracion=None ,items=[], descripcion=''):
    return { 'autor': autor,
             'descripcion': descripcion,
             'titulo': titulo,
             'fecha_expiracion': fecha_expiracion,
             'fecha_creacion': datetime.now(),
             'items': items
        }


def anuncio_agrega_item( anuncio, item ):
    anuncio['items'].append(item)
    return anuncio



def item_crear( nombre, unidad, precio, descripcion=''):
    return {'nombre': nombre,
            'descripcion': descripcion,
            'unidad': unidad,
            'precio': precio,
        }



def pedido_crear( cliente, anuncio, items=[]):
    return {'cliente': cliente,
            'aid': anuncio["_id"],
            'items': items
        }



def pedido_agrega_item( pedido, item ):
    pedido['items'].append(item)
    return pedido



def pedido_guardar( pedido):
    return db.pedidos.save(pedido)



def pedido_enviar(pedido):
    pedido['status'] = 'enviado'
    pid = pedido_guardar(pedido)
    # agrega pid a su anuncio
    a = anuncio_por_id( pedido['aid'], db )
    if 'pedidos' in a:
        a['pedidos'].append( pid )
    else:
        a['pedidos'] = [ pid, ]
    anuncio_guardar(a, db)
    
    return pid
    


def pedido_cancelar(pedido):
    pedido['status'] = 'cancelado'
    return pedido_guardar(pedido,db)



def pedido_por_id(pid):
    return db.pedidos.find_one( ObjectId(pid) )



def nota_crear(cliente, pedido, items=[]):
    return {'cliente': cliente,
            'pid': pedido["_id"],
            'items': items
        }
