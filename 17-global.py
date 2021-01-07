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

app = Flask(__name__)  
app.secret_key = 'qeqweqweqwewq'
csrf = CsrfProtect(app)

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

@app.before_request
def before_request():
    g.test = 'test1'

@app.after_request
def after_request(response):
    print(g.test)
    return response

@app.route('/', methods = ['GET', 'POST'])         
def index():
    print(g.test)
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
        success_message = 'Bienvenido {}'.format(username)
        flash(success_message)

        session['username'] = username

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

if __name__ == '__main__':
    app.run(debug=True, port=8000)    