from wtforms import Form
from wtforms import StringField, TextField
from wtforms import HiddenField
from wtforms import PasswordField
from wtforms.fields.html5 import EmailField
from wtforms import validators

from models import User

def length_honeypot(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('El campo debe estar vacío')

class CommentForm(Form):
    username = StringField('username',
                            [validators.Required(message = 'El username es requerido'),
                            validators.length(min=4, max=25, message='Introduzca un username válido!')])
    email = EmailField('Correo Electronico',
                        [validators.Required(message="El email es requerido"),
                        validators.email(message="Inserte un email valido")])
    comment = TextField('Comentario')
    honeypot = HiddenField('', [length_honeypot])

class LoginForm(Form):
    username = StringField('Username',
                            [validators.Required(message = 'El username es requerido'),
                            validators.length(min=4, max=25, message='Introduzca un username válido!')])
    password = PasswordField('Password', [validators.Required(message='El password es requerido')])

class CreateForm(Form):
    username = StringField('username',
                            [validators.Required(message = 'El username es requerido'),
                            validators.length(min=4, max=50, message='Introduzca un username válido!')])
    email = EmailField('Correo Electronico',
                        [validators.Required(message="El email es requerido"),
                        validators.email(message="Inserte un email valido"),
                        validators.length(min=4, max=50, message='Introduzca un emailválido!')]])
    password = PasswordField('Password', [validators.Required(message='El password es requerido')])

    #sobreescribimos un metodo de los que se generan automaticamente: validate_username, validate_email, validate_password
    def validate_username(form, field):
        username = field.data
        user = User.query.filter_by(username = username).first()
        if user is not None:
            raise validators.Validationerror('El username ya se encuentra registrado!')
