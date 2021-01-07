from flask import Flask
from flask import request

app = Flask(__name__)  

@app.route('/')         
def index():
    return 'Hola Mundo'

#params/libros/1
@app.route('/params')
@app.route('/params/<name>')  
@app.route('/params/<name>/<int:num>')         
def params(name='este es un valor por defecto', num=0):
    return 'El parametro es {} {}'.format(name, num)

if __name__ == '__main__':
    app.run(debug=True, port=8000)      