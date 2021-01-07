from flask import Flask
from flask import render_template

app = Flask(__name__)  

@app.route('/')         
def index():
    name= 'Fede'
    return render_template('index_extend.html.j2', name=name)

@app.route('/client')         
def client():
    list_name= ['Fede', 'Sandra', 'Lourdes', 'Victoria']
    return render_template('client.html.j2', list=list_name)

if __name__ == '__main__':
    app.run(debug=True, port=8000)    