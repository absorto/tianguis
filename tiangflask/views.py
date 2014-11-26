
from flask import Flask, jsonify, make_response
import pprint

app = Flask(__name__)
#flask.url_for('static', filename='anuncio_crear.html
#flask.url_for('static', filename='anuncio_crear.js')

@app.route('/crear', methods=['POST'])
def anuncio_crear():
    return jsonify({ "status": "error",
                     "message": "cave canem" })
 

    #    return pprint.pformat(flask.request)
    # pprint.pformat(flask.request)
    # return { "status": "error",
    #          "message": "cave canem",
    #      }

if __name__ == '__main__':
    app.run(debug=True)
