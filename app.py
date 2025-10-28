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

@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        usuario_email = request.form['email']
        contrasenia = request.form['password']
        nacimiento_dia = request.form['dia']
        nacimiento_mes = request.form['mes']
        nacimiento_anio = request.form['anio']
        acepto_terminos = 'verifica' in request.form

        if usuario_email in usuarios:
            flash("Ya existe una cuenta registrada con este correo.")
            return redirect(url_for('registro'))

        usuarios.append(usuario_email)
        print(f"[REGISTRO] Email: {usuario_email} | Clave: {contrasenia} | "
              f"Nacimiento: {nacimiento_dia}/{nacimiento_mes}/{nacimiento_anio} | "
              f"Términos aceptados: {acepto_terminos}")

        flash("Registro completado correctamente. Inicia sesión para continuar.")
        return redirect(url_for('acceso'))

    return render_template('interfaz.html')


@app.route('/acceso', methods=['GET', 'POST'])
def acceso():
    if request.method == 'POST':
        correo_usuario = request.form['usuario']
        clave_usuario = request.form['password']

        if correo_usuario and clave_usuario:
            session['usuario'] = correo_usuario
            flash(f"Bienvenido de nuevo, {correo_usuario}.")
            return redirect(url_for('inicio'))
        else:
            flash("No se pudo iniciar sesión. Verifica tus datos.")
            return redirect(url_for('acceso'))

    return render_template('login.html')


@app.route('/salir')
def salir():
    usuario_activo = session.pop('usuario', None)
    if usuario_activo:
        flash(f"Sesión cerrada. ¡Hasta pronto, {usuario_activo}!")
    else:
        flash("No hay ninguna sesión activa.")
    return redirect(url_for('inicio'))


@app.route('/')
def inicio():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
