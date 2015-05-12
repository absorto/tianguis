from flask import Flask, session, redirect, url_for, escape, request, jsonify, render_template
from flask.ext.pymongo import PyMongo
from bson.objectid import ObjectId

from sh import find, cd
from pprint import pformat

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

    items = []
    for i in req['itemgrid']:
        if 'changes' in i:
            changes = i.pop('changes')
            i.pop('recid')
            i.update(changes)
        items.append(i)
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


    if request.form['cmd']==u'delete-records':
        
        # grab IDs from the request
        for f,v in request.form.viewitems():
            if f == 'selected[]':
                recids = v

        # remove them
        for recid in recids:
            mongo.db.ofertas.remove({"_id":ObjectId(recid)})
        

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

    # add recid to item list, that w2ui grid may edit it
    for n in range(0, len(ad['items'])):
        ad['items'][n]['recid'] = n
        
    return jsonify( ad )





@app.route('/contactos', methods=['POST', 'GET'])
def contactos():
    # if request.form['cmd']==u'delete-records':
        
    #     # grab IDs from the request
    #     for f,v in request.form.viewitems():
    #         if f == 'selected[]':
    #             recids = v

    #     # remove them
    #     #for recid in recids:
    #     #    mongo.db.ofertas.remove({"_id":ObjectId(recid)})
        
    contactos = mongo.db.contactos.find({'usuario': session['username']})
    records = []
    for c in contactos:
        c['recid'] = str(c.pop('_id'))
        records.append(c)

    records = []
    
    return jsonify( { 'status': "success", 'total':len(records), 'records': records} )



@app.route('/contactos/save', methods=['POST', 'GET'])
def contactos_save():
    app.logger.debug(pformat(request.form))

    if request.form['cmd']==u'save-records':
        app.logger.debug(pformat(request.form))
    
    items = []
    for i in req['itemgrid']:
        if 'changes' in i:
            changes = i.pop('changes')
            i.pop('recid')
            i.update(changes)
        items.append(i)
    ad.update( {'recid': recid,
                'items': items} )


# 'tis contains w2ui commands to web server
#    app.logger.debug(pformat(request.form))

#    app.logger.debug(pformat(request.get_json()))
#    app.logger.debug(pformat(ad))

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
