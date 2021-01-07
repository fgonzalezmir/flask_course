from flask import Flask
from flask import render_template
from flask import request
from flask_wtf import CsrfProtect

import forms

app = Flask(__name__)  
app.secret_key = 'my_secret_key'
crsf = CsrfProtect(app)

@app.route('/', methods = ['GET', 'POST'])         
def index():
    comment_form = forms.CommentForm(request.form)
    if request.method == 'POST' and comment_form.validate():
        print(comment_form.username.data)
        print(comment_form.email.data)
        print(comment_form.comment.data)
    else:
        print("Error en el formulario")
    title = "Curso Flask"
    return render_template('index_form.html.j2', title=title, form = comment_form)

@app.route('/login')     
def login():
    login_form = forms.LoginForm(request.form)
    return render_template('login_form.html.j2', form=login_form)

if __name__ == '__main__':
    app.run(debug=True, port=8000)    