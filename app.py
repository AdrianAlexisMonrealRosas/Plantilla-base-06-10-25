from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def inicio():
    return render_template('index.html', active_page='inicio')

@app.route('/animales')
def animales():
    return render_template('animales.html', active_page='animales')

@app.route('/vehiculos')
def vehiculos():
    return render_template('vehiculos.html', active_page='vehiculos')

@app.route('/maravillas')
def maravillas():
    return render_template('maravillas.html', active_page='maravillas')

@app.route('/acerca')
def acerca():
    return render_template('acerca.html', active_page='acerca')

@app.route('/registro')
def inicio():
    return render_template('registro.html', active_page='registro')


if __name__ == '__main__':
    app.run(debug=True)
