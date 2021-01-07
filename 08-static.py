from flask import Flask
from flask import render_template

app = Flask(__name__)  

@app.route('/')         
def index():
    return render_template('static.html.j2', title="Hola Mundo")

if __name__ == '__main__':
    app.run(debug=True, port=8000)    