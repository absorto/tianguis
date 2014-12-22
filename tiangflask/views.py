from flask import Flask, session, redirect, url_for, escape, request, jsonify
from flask.ext.pymongo import PyMongo
from bson.objectid import ObjectId
from w2ui import parse_w2ui_request_form


from pprint import pformat
import sys
import re

app = Flask("tianguis")
mongo = PyMongo(app)


############
# anuncios #
############

@app.route('/anuncios/save', methods=['POST'])
def anuncio_save():
    try:
#        pprint.pprint(request)
        app.logger.debug('A value for debugging')
        app.logger.warning('A warning occurred (%d apples)', 42)
        app.logger.error('An error occurred')
        return jsonify({ "status": "success"} )
    except:
        return jsonify({ "status": "error",
                         "message": pformat(sys.exc_info()[0]) })
 

@app.route('/ofertas/save', methods=['POST', 'GET'])
def ofertas_save():
    for record in request.json:
        app.logger.debug(pformat(record))

        if type(record['recid']) == int:
            record.pop('recid')
        elif type(record['recid']) == unicode and len(record['recid']) == 24:
            record['_id'] = ObjectId(record.pop('recid'))
        mongo.db.ofertas.save( record )

    return jsonify( { 'status': "success" } )




@app.route('/ofertas/mias', methods=['POST', 'GET'])
def ofertas_mias():
    
    ofertas = mongo.db.ofertas.find()
    records = []
    for o in ofertas:
        # o['_id'] = str(o['_id'])
        o['recid'] = str(o.pop('_id'))
        records.append(o)

    return jsonify( { 'status': "success", 'total':len(records), 'records': records} )
       





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
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s. <br><a href="/static/index.html">home</a>' % escape(session['username'])
    return 'You are not logged in. <a href="/login">login</a>'


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
