# coding: utf-8
import datetime

from flask import Flask, url_for, redirect, render_template, request


from flask_admin.base import MenuLink, Admin, BaseView, expose


import flask_admin as admin
from flask_mongoengine import MongoEngine
from flask_admin.form import rules
from flask_admin.contrib.mongoengine import ModelView
from wtforms import form, fields, validators
import flask_login as login
from flask_login import current_user, UserMixin

# Create application
app = Flask(__name__)

# Create dummy secrey key so we can use sessions
app.config['SECRET_KEY'] = '123456790'
app.config['MONGODB_SETTINGS'] = {'DB': 'testing'}

# Create models
db = MongoEngine()
db.init_app(app)


class Marchante(db.Document):
    email = db.EmailField(required=True)
    nombre = db.StringField(max_length=50)
    login = db.StringField(max_length=50)
    password = db.StringField(max_length=40)

    # Flask-Login integration
    def is_authenticated(self):
        return True

    def is_active(self):
        return True

    def is_anonymous(self):
        return False

    def get_id(self):
        return str(self.id)

    # Required for administrative interface
    def __unicode__(self):
        return self.login

    def __repr__(self):
        return "<marchante %s>" % self.login


class Item(db.EmbeddedDocument):
    """
    cosa que se vende o se compra
    """
    nombre = db.StringField(required=True)
    descripcion = db.StringField(required=True)
    unidad = db.StringField()
    precio = db.DecimalField(required=True)

    def __repr__(self):
        return u"<item %s>" % self.nombre


class Anuncio(db.Document):
    """
    Anuncio es el término general para los casos particulares de
    anuncio que son ofertas y demandas. O sea, un anuncio es una
    oferta o una demanda.
    """
    marchante = db.ReferenceField(Marchante)
    descripcion = db.StringField(required=True)
    titulo = db.StringField(required=True)
    fecha_inicio = db.DateTimeField(required=False,
                                    default=datetime.datetime.now())
    fecha_fin = db.DateTimeField(required=False,
                                 default=datetime.datetime.now()
                                 + datetime.timedelta(days=5))
    items = db.ListField(db.EmbeddedDocumentField(Item))

    def __unicode__(self):
        return self.titulo


# Define login and registration forms (for flask-login)
class LoginForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        user = self.get_user()

        if user is None:
            raise validators.ValidationError('Invalid user')

        if user.password != self.password.data:
            raise validators.ValidationError('Invalid password')

    def get_user(self):
        return Marchante.objects(login=self.login.data).first()


class RegistrationForm(form.Form):
    login = fields.StringField(validators=[validators.required()])
    email = fields.StringField()
    password = fields.PasswordField(validators=[validators.required()])

    def validate_login(self, field):
        if Marchante.objects(login=self.login.data):
            raise validators.ValidationError('Duplicate username')


# Initialize flask-login
def init_login():
    login_manager = login.LoginManager()
    login_manager.setup_app(app)

    # Create user loader function
    @login_manager.user_loader
    def load_user(user_id):
        return Marchante.objects(id=user_id).first()



# Create customized model view class
class MyModelView(ModelView):
    def is_accessible(self):
        return current_user.is_authenticated


# Create customized index view class
class MyAdminIndexView(admin.AdminIndexView):
    def is_accessible(self):
        return current_user.is_authenticated




# Create menu links classes with reloaded accessible
class AuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return current_user.is_authenticated


class NotAuthenticatedMenuLink(MenuLink):
    def is_accessible(self):
        return not current_user.is_authenticated




# Flask views
@app.route('/')
def index():
    return render_template('index.html', user=current_user)


@app.route('/login/', methods=('GET', 'POST'))
def login_view():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        user = form.get_user()
        login.login_user(user)
        return redirect(url_for('index'))

    return render_template('form.html', form=form)


@app.route('/register/', methods=('GET', 'POST'))
def register_view():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        user = Marchante()

        form.populate_obj(user)
        user.save()

        login.login_user(user)
        return redirect(url_for('index'))

    return render_template('form.html', form=form)


@app.route('/logout/')
def logout_view():
    login.logout_user()
    return redirect(url_for('index'))



if __name__ == '__main__':
    init_login()

    # Create admin
    admin = admin.Admin(app, 'Tianguis', index_view=MyAdminIndexView())

    # Add views

    admin.add_view(MyModelView(Marchante))

#    admin.add_view(ModelView(Marchante))
    admin.add_view(ModelView(Anuncio))


    # Add home link by url
    admin.add_link(MenuLink(name='Back Home', url='/'))

    # Add login link by endpoint
    admin.add_link(NotAuthenticatedMenuLink(name='Login',
                                            endpoint='login_view'))

    # Add links with categories
    admin.add_link(MenuLink(name='Google', category='Links', url='http://www.google.com/'))
    admin.add_link(MenuLink(name='Mozilla', category='Links', url='http://mozilla.org/'))

    # Add logout link by endpoint
    admin.add_link(AuthenticatedMenuLink(name='Logout',
                                         endpoint='logout_view'))


    # Start app
    app.run(debug=True)
