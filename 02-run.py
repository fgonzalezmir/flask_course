from flask import Flask

app = Flask(__name__)  

@app.route('/')         
def index():
    return 'Podemos realizar cambios en mi archivo y verlos reflejados'

if __name__ == '__main__':
    app.run(debug=True, port=8000)               