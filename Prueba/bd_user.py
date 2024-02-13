import mysql.connector
from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/submit_form', methods=['POST'])
def submit_form():
    # Recuperar los datos del formulario
    nombre = request.form['nombre']
    email = request.form['email']
    fecha_nacimiento = request.form['fechaNacimiento']
    password = request.form['password']
    confirm_password = request.form['confirmPassword']
    sus = request.form['btn-opcion']

    # Conectar a la base de datos
    conn = mysql.connector.connect(
        host="3306",
        user="root",
        password="Yugioh34*",
        database="prueba_bd"
    )
    cursor = conn.cursor()

    # Insertar datos en la tabla
    cursor.execute("INSERT INTO usuarios (nom, email, password, suscripcion) VALUES (%s, %s, %s, %s)", (nombre, email, fecha_nacimiento, password, sus))
    conn.commit()

    # Cerrar la conexión
    cursor.close()
    conn.close()

    return 'Formulario enviado correctamente'

if __name__ == '__main__':
    app.run(debug=True)
