
from flask import Flask, jsonify, make_response
import pprint
import sys

app = Flask(__name__)

@app.route('/anuncios/save', methods=['POST'])
def anuncio_save():
    try:
#        pprint.pprint(request)
        return jsonify({ "status": "success"} )
    except:
        return jsonify({ "status": "error",
                         "message": pprint.pformat(sys.exc_info()[0]) })
 


if __name__ == '__main__':
    app.run(debug=True)
