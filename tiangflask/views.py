
import flask
import pprint

app = flask.Flask(__name__)
#flask.url_for('static', filename='anuncio_crear.html
#flask.url_for('static', filename='anuncio_crear.js')

@app.route('/crear', methods=['GET', 'POST'])
def anuncio_crear():
#    return pprint.pformat(flask.request)
    pprint.pformat(flask.request)
    return "hola"

if __name__ == '__main__':
    app.run(debug=True)
