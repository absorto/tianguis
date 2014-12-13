from flask import Flask, session, redirect, url_for, escape, request, jsonify
from flask.ext.pymongo import PyMongo
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
 


@app.route('/ofertas/mias', methods=['POST', 'GET'])
def ofertas_mias():

    # if request.form['cmd'] == 'save-records':
    #     records = {}
    #     for key in request.form:
    #         if key.startswith("changes"):
    #             # parse 'changes' key submited by w2ui
    #             # changes[0][desc]: ffff
    #             (n, pkey) = key.split('][')
    #             pkey = pkey[0:-1]
    #             if pkey != 'recid':
    #                 if n in records:
    #                     records[n][pkey] = request.form[key]
    #                 else:
    #                     records[n] = { pkey: request.form[key] }
                    
    #     app.logger.debug(pformat(records))
    # elif request.form['cmd'] == 'get-records':
    #      pass
    # else:
    #     pass

    app.logger.debug(pformat(parse_w2ui_request_form(request.form)))
    #app.logger.debug(pformat(request.form))

    ofertas = mongo.db.ofertas.find({'autor': session['username']})
    records = [o for o in ofertas]
    return jsonify( { 'status': "success", 'total':len(records), 'records': records} )
       
#        
#            { recid: 1, titulo: 'puesto', desc: 'Tianguis el 100', email: 'jdoe@gmail.com', vigencia: '4/3/2012' },
#        


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
