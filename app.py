import psycopg2
from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)
#app.config['STATIC_FOLDER'] = 'css'

# Configura la conexión a la base de datos 

db = psycopg2.connect(
    dbname="MD",
    user="postgres",
    password="admin",
    host="localhost",  
    port="5432"         
)


@app.route('/', methods=['GET', 'POST'])
def index():
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


    return render_template('indexFormularioCurso.html')
@app.route('/gracias')
def gracias():
    return "Gracias por enviar el formulario."

if __name__ == '__main__':
    app.run(debug=True)