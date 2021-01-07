from flask import Flask

app = Flask(__name__)   # nuevo objeto

@app.route('/')         # wrap o decorador
def index():
    return 'Hola Mundo'

app.run()               #ejecuta en el servidor en el puerto 5000

