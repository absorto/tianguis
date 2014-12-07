from flask import Flask, session, redirect, url_for, escape, request, jsonify

import pprint
import sys

app = Flask(__name__)


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
 


# /ofertas/mias
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
    return 'You are not logged in'


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
