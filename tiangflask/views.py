from flask import Flask, session, redirect, url_for, escape, request, jsonify
from flask.ext.pymongo import PyMongo


import pprint
import sys

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
                         "message": pprint.pformat(sys.exc_info()[0]) })
 


@app.route('/ofertas/mias', methods=['POST', 'GET'])
def ofertas_mias():

    if request.form['cmd'] == 'get-records':
        ofertas = mongo.db.anuncios.find({'autor': session['username']})
        for o in ofertas:
            app.logger.debug(pprint.pformat(o))                    
        # records = [ { 'recid': '32af', 'titulo': 'puesto', 'desc': 'Tianguis el 100', 'email': 'jdoe@gmail.com', 'vigencia': '4/3/2012' },
        #             { 'recid': 'uio2', 'titulo': 'puesto', 'desc': 'Tianguis el 100', 'email': 'jdoe@gmail.com', 'vigencia': '4/3/2012' },
        #         ]
    
    return jsonify( { 'status': "success", 'total':2, 'records': records} )
        
#        
#            { recid: 1, titulo: 'puesto', desc: 'Tianguis el 100', email: 'jdoe@gmail.com', vigencia: '4/3/2012' },
#        app.logger.debug(pprint.pformat(ofertas))


    # /overtas/inbox
# /ofertas/mercado


# /pedidos/mios
# /pedidos/inbox
# /pedidos/mercado
    



###################
# Falso login     #
###################
@app.route('/')
def index():
    if 'username' in session:
        return 'Logged in as %s' % escape(session['username'])
    return 'You are not logged in. <a href="/login">login</a><br><a href="/static/index.html">home</a>'


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
