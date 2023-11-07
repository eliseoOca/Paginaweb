from flask import Flask, request, render_template, redirect, url_for
import psycopg2

app = Flask(__name__)

# Configuración de la base de datos
db_connection = psycopg2.connect(
    dbname="MD",
    user="postgres",
    password="admin",
    host="localhost",  # Puede variar según la configuración de tu servidor PostgreSQL
    port="5432"   # Cambia según la configuración de tu servidor PostgreSQL
)

# Ruta para la página de registro
@app.route('/', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']

        # Insertar los datos en la base de datos
        cursor = db_connection.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)", (nombre, email, password))
        db_connection.commit()
        cursor.close()

        # Redirigir a una página de inicio de sesión o a donde desees
        return redirect(url_for('inicio_sesion'))

    return render_template('formInc.html')

# Ruta para la página de inicio de sesión
@app.route('/inicio_sesion')
def inicio_sesion():
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
