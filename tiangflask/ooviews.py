from flask import Flask, session, redirect, url_for, escape, request, jsonify
from pprint import pprint
import model as tng
import dom

app = Flask("tianguis")


@app.route('/oferta/', methods=['POST', 'GET'])
def oferta():
    return dom.pag_estandar('Oferta',
                            lambda: tng.oferta_table())


@app.route('/anuncio/editar/<recid>', methods=['POST', 'GET'])
def crear_oferta(recid):
    if recid == 'nueva':
        o = tng.Oferta()
    else:
        o = tng.Oferta.objects.with_id(recid)

    if request.method == 'POST':
        u = tng.Marchante(login='rgh', email='rgh@example.com')
        u.save()
        o.titulo = request.form['titulo']
        o.descripcion = request.form['descripcion']
        o.marchante = u
        o.save()
        return redirect("/anuncio/%s" % o.pk)

    return dom.pag_estandar('Oferta',
                            lambda: o.edit_form())


@app.route('/demanda/', methods=['POST', 'GET'])
def demanda():
    return dom.pag_estandar('Demanda',
                            lambda: tng.demanda_table())


@app.route('/anuncio/<recid>', methods=['POST', 'GET'])
def anuncio(recid):
    a = tng.Anuncio.objects.with_id(recid)
    return dom.pag_estandar('anuncio %s' % recid,
                            lambda: a.as_div())

# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
