from flask import Flask, session, redirect, url_for, escape, request, jsonify, render_template
from flask.ext.pymongo import PyMongo
from bson.objectid import ObjectId

from sh import find, cd

from pprint import pformat
import sys


app = Flask("tianguis")
mongo = PyMongo(app)


@app.route('/')
def index():

    if 'username' in session:
        username = session['username']
    else:
        username = False

    scripts = [n.strip() for n in find("static/js", "-iname", "*.js", _iter=True)]
    
    return render_template('base.html',
                           scripts=scripts,
                           username=username)




@app.route('/ofertas/save', methods=['POST', 'GET'])
def ofertas_save():

    # crea diccionario 'ad' a partir de dos widgets
    req   = request.get_json()

    recid = req['recid']
    ad    = req['top_form']
    items = [i['changes'] if 'changes' in i else i for i in req['itemgrid']]
    ad.update( {'recid': recid,
                'items': items} )

    bulk = mongo.db.ofertas.initialize_ordered_bulk_op()    
    if ad['recid'] == 'nueva':
        # oferta nueva
        ad.pop('recid')
        ad['usuario'] = session['username']
        bulk.insert( ad )
    else:
        # ah, actualizando
        recid = ObjectId(ad.pop('recid'))
        bulk.find( {'_id'    : recid,
                    'usuario': session['username'] } ).update({'$set': ad}) 
    result = bulk.execute()

    return jsonify( { 'status': "success", 'result': result } )




@app.route('/ofertas/mias', methods=['POST', 'GET'])
def ofertas_mias():
    
    ofertas = mongo.db.ofertas.find({'usuario': session['username']})
    records = []
    for o in ofertas:
        o['recid'] = str(o.pop('_id'))
        records.append(o)

    return jsonify( { 'status': "success", 'total':len(records), 'records': records} )
       


@app.route('/ofertas/<recid>', methods=['POST', 'GET'])
def oferta(recid):

    ad = mongo.db.ofertas.find_one({'_id': ObjectId(recid),
                                    'usuario': session['username']})
    ad['recid'] = str(ad.pop('_id'))
    return jsonify( ad )


#    bulk = mongo.db.ofertas.initialize_ordered_bulk_op()
    #for record in request.get_json():
#    app.logger.debug(request.get_json())
    #     if type(record['recid']) == int:
    #         # sin llave? has de ser nuevo
    #         record.pop('recid')
    #         record['usuario'] = session['username']
    #         bulk.insert( record )
    #     elif type(record['recid']) == unicode and len(record['recid']) == 24:
    #         # ah, actualizando
    #         recid = ObjectId(record.pop('recid'))
    #         bulk.find( {'_id': recid,
    #                     'usuario': session['username']}).update({'$set': record})
    # result = bulk.execute()




# /overtas/inbox
# /ofertas/mercado


# /pedidos/mios
# /pedidos/inbox
# /pedidos/mercado
    





##################################################################################
# Login on openid Ref:                                                           #
# http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins #
# Falso login                                                                    #
##################################################################################


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('index'))
    return '''
        <form action="" method="post">
            <p><input type=text name=username>
            <p><input type=submit value=Login>
        </form>
    '''

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('index'))

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'



if __name__ == '__main__':
    app.run(debug=True)
