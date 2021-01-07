from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask import session
from flask_wtf import CsrfProtect
from flask import url_for
from flask import redirect
from flask import flash
from flask import g
import forms
from config import DevelopmentConfig

from models import db
from models import User, Comment
from helper import date_format

app = Flask(__name__)  
app.config.from_object(DevelopmentConfig)
csrf = CsrfProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    if 'username' not in session and request.endpoint in ['comment']:
        return redirect(url_for('login'))
    elif 'username' in session and request.endpoint in ['login', 'create']:
        return redirect(url_for('index'))

@app.after_request
def after_request(response):
    return response

@app.route('/', methods = ['GET', 'POST'])         
def index():
    if 'username' in session:
        username = session['username']
        print(username)
    else:
        print('nada')
    title = 'Index'
    return render_template('index.html', title=title)

@app.route('/login', methods = ['GET', 'POST'])     
def login():
    login_form = forms.LoginForm(request.form)
    if request.method == 'POST' and login_form.validate():
        username = login_form.username.data
        password =login_form.password.data

        user = User.query.filter_by(username = username).first()
        # select * from users where username= username limit 1
        if user is not None and user.verify_password(password):
            success_message = 'Bienvenido {}'.format(username)
            flash(success_message)
            session['username'] == username
            return redirect(url_for('index'))
        else:
            error_message = 'Contraseña no valida'
            flash(error_message)

    return render_template('login_form.html.j2', form=login_form)

@app.route('/logout')     
def logout():
    if 'username' in session:
        sesion.pop('username')
    return redirect(url_for('login'))

@app.route('/cookie')     
def cookie():
    response = make_response(render_template('cookie.html.j2'))
    response.set_cookie('customer_cookie', 'Fede')
    return response

@app.route('/create', methods = ['GET', 'POST'])
def create():
    create_form = forms.CreateForm(request.form)
    if request.method == 'POST' and create_form.validate():
        user = User(create_form.username.data,
                    create_form.password.data,
                    create_form.email.data)
        db.session.add(user)
        db.session.commit()

        success_message = 'Usuario registrado en la base de datos'
        flash(success_message)
    return render_template('create.html', form= create_form)

@app.route('/comment', methods = ['GET', 'POST'])     
def comment():
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        user_id = session['user_id']
        comment = Comment(user_id=?, 
                        text = comment_form.comment.data)

        db.session.add(comment)
        db.session.commit()
    
    title = "Curso flask"

    return render_template('comment.html', title = title form= comment_form)

@app.route('/reviews', methods = ['GET']) 
@app.route('/reviews/<int:page>', methods = ['GET'])        
def reviews(page=1):
    per_page = 3

    comment_list = Comment.query.join(User).add_columns(
                                            User.username, 
                                            Comment.text,
                                            Comment.created_date).paginate(page,per_page,False)

    return render_template('reviews.html', comments=comment_list)

if __name__ == '__main__':
    csrf.init_app(app)
    db.init_app(app)

    with app.app_context():
        db.create_all()

    app.run(port=8000)    