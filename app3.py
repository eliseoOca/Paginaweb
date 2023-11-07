from flask import Flask, request, render_template, redirect, url_for, session
import psycopg2



app = Flask(__name__)
app.secret_key = '123'  # Clave secreta para la sesión

# Configuración de la base de datos
db_connection = psycopg2.connect(
    dbname="MD",
    user="postgres",
    password="admin",
    host="localhost",  # Puede variar según la configuración de tu servidor PostgreSQL
    port="5432" 
)

@app.route("/")
def index():
   return render_template("login.html")

@app.route("/inicio_sesion", methods=["POST"])
def iniciar_sesion():
   username = request.form["username"]
   password = request.form["password"]

   # Realiza una consulta para verificar el usuario y la contraseña en la base de datos
   cursor = db_connection.cursor()
   cursor.execute("SELECT id, nombre, email, password FROM usuarios WHERE email = %s", (username,))
   user = cursor.fetchone()
   cursor.close()

   if user and user[3] == password:
       # Inicio de sesión exitoso
       session["user_id"] = user[0]  # Almacena el ID del usuario en la sesión
       return render_template('indexFormularioCurso.html')
   else:
       error_message = "Datos incorrectos."
       return render_template("login.html", error_message=error_message)

if __name__ == "__main__":
   app.run(debug=True)
