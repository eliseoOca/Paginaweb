from flask import Flask, render_template, request, redirect, url_for, session, flash
import psycopg2

app = Flask(__name__)
app.secret_key = '123'  # Clave secreta para la sesión

# Configuración de la base de datos
db = psycopg2.connect(
    dbname="MD",
    user="postgres",
    password="admin",
    host="localhost",
    port="5432"
)

# Rutas para las páginas estáticas
@app.route('/')
def index():
    return render_template('index.html')

@app.route('/carrusel')
def carrusel():
    return render_template('carrusel.html')

@app.route('/cartas')
def cartas():
    return render_template('cartasAgradecimiento.html')

@app.route('/indexBancoAlimento')
def index_banco_alimento():
    return render_template('indexBancoAlimento.html')

@app.route('/indexDonation')
def index_donation():
    return render_template('indexDonation.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/formInc')
def form_inc():
    return render_template('formInc.html')

@app.route('/formulario_opcion')
def formulario_opcion():
    return render_template('indexFormularioOp.html')

@app.route('/formulario_curso')
def formulario_curso():
    return render_template('indexFormularioCurso.html')

# Rutas para el registro y el inicio de sesión
@app.route('/registro', methods=['GET', 'POST'])
def registro():
    if request.method == 'POST':
        nombre = request.form['nombre']
        email = request.form['email']
        password = request.form['password']

        cursor = db.cursor()
        cursor.execute("INSERT INTO usuarios (nombre, email, password) VALUES (%s, %s, %s)", (nombre, email, password))
        db.commit()
        cursor.close()
        return redirect(url_for('inicio_sesion'))

    return render_template("login.html")  


@app.route('/inicio_sesion', methods=["GET", "POST"])
def inicio_sesion():
    if request.method == 'POST':
        username = request.form["username"]
        password = request.form["password"]

        cursor = db.cursor()
        cursor.execute("SELECT id, nombre, email, password FROM usuarios WHERE email = %s", (username,))
        user = cursor.fetchone()
        cursor.close()
        
        if user and user[3] == password:
            session["user_id"] = user[0]
            return redirect(url_for('formulario_inscripcion'))
        else:
            error_message = "Datos incorrectos."
            return render_template("login.html", error_message=error_message)

    return render_template("login.html")

# Rutas para el formulario de inscripción y la página de agradecimiento
@app.route('/formulario_inscripcion', methods=['GET', 'POST'])
def formulario_inscripcion():
    if request.method == 'POST':
        idioma = request.form['idioma']
        sucursal = request.form['sucursal']
        fecha = request.form['fecha']
        clases = request.form['clases']
        nombre = request.form['nombre']
        apellido = request.form['apellido']
        cp = request.form['cp']
        salario = request.form['salario']
        comentario = request.form['comentario']

        cursor = db.cursor()
        sql = "INSERT INTO inscripciones (idioma, sucursal, fecha, clases, nombre, apellido, cp, salario, comentario) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
        values = (idioma, sucursal, fecha, clases, nombre, apellido, cp, salario, comentario)
        cursor.execute(sql, values)
        db.commit()
        cursor.close()

        return redirect(url_for('gracias'))

    return render_template('indexFormularioOp.html')

@app.route('/gracias')
def gracias():
    return "Gracias por enviar el formulario."

if __name__ == '__main__':
    app.run(debug=True)
