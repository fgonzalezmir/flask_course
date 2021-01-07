from flask import Flask
from flask import render_template
from flask import request
from flask import make_response
from flask_wtf import CsrfProtect

import forms

app = Flask(__name__)  
app.secret_key = 'my_secret_key'
crsf = CsrfProtect(app)

@app.route('/', methods = ['GET', 'POST'])         
def index():
    custom_cookie = request.cookies.get('customer_cookie', 'Undefined')
    print(custom_cookie)
    title = 'Index'
    return render_template('index.html', title=title)

@app.route('/login')     
def login():
    login_form = forms.LoginForm()
    return render_template('login_form.html.j2', form=login_form)

@app.route('/cookie')     
def cookie():
    response = make_response(render_template('cookie.html.j2'))
    response.set_cookie('customer_cookie', 'Fede')
    return response

if __name__ == '__main__':
    app.run(debug=True, port=8000)    