from flask import Flask, session, redirect, url_for, escape, request, jsonify
from pprint import pprint
import model as tng
import dom

app = Flask("tianguis")


@app.route('/oferta/', methods=['POST', 'GET'])
def oferta():
    return dom.pag_estandar('Oferta',
                            lambda: tng.oferta_table(),
                            session)


@app.route('/anuncio/editar/<recid>', methods=['POST', 'GET'])
def crear_oferta(recid):
    if recid == 'nueva':
        o = tng.Oferta()
    else:
        o = tng.Oferta.objects.with_id(recid)

    if request.method == 'POST':
        u = tng.marchante_by_login(session['username'])
        o.titulo = request.form['titulo']
        o.descripcion = request.form['descripcion']
        o.marchante = u
        o.save()
        return redirect("/anuncio/%s" % o.pk)

    return dom.pag_estandar('Oferta',
                            lambda: o.edit_form(),
                            session)


@app.route('/demanda/', methods=['POST', 'GET'])
def demanda():
    return dom.pag_estandar('Demanda',
                            lambda: tng.demanda_table(),
                            session)


@app.route('/anuncio/<recid>', methods=['POST', 'GET'])
def anuncio(recid):
    a = tng.Anuncio.objects.with_id(recid)
    return dom.pag_estandar('anuncio %s' % recid,
                            lambda: a.as_div(),
                            session)


@app.route('/anuncio/<recid>/item/agrega', methods=['POST', 'GET'])
def anuncio_agrega_item(recid):
    a = tng.Anuncio.objects.with_id(recid)

    if request.method == 'POST':
        i = tng.Item()
        i.nombre = request.form['nombre']
        i.descripcion = request.form['descripcion']
        i.precio = float(request.form['precio'])
        i.unidad = request.form['unidad']
        a.items.append(i)
        a.save()
        return redirect("/anuncio/%s" % a.pk)
    else:
        i = tng.Item()

    return dom.pag_estandar('anuncio %s' % recid,
                            lambda: a.as_div(item=i),
                            session)


@app.route('/anuncio/<recid>/item/<itemid>/elimina', methods=['POST', 'GET'])
def anuncio_elimina_item(recid, itemid):
    a = tng.Anuncio.objects.with_id(recid)
    del(a.items[int(itemid)])
    a.save()
    return redirect("/anuncio/%s" % a.pk)


# Login on openid Ref:                                                           #
# http://blog.miguelgrinberg.com/post/the-flask-mega-tutorial-part-v-user-logins #

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        session['username'] = request.form['username']
        return redirect(url_for('oferta'))

    u = tng.Marchante()
    return dom.pag_estandar('login',
                            lambda: u.login_form(),
                            session)
    
    # return '''
    #     <form action="" method="post">
    #         <p><input type=text name=username>
    #         <p><input type=submit value=Login>
    #     </form>
    # '''


@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('username', None)
    return redirect(url_for('oferta'))


# set the secret key.  keep this really secret:
app.secret_key = 'A0Zr98j/3yX R~XHH!jmN]LWX/,?RT'


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
