from flask import Flask, render_template, redirect, request, url_for, flash, session, g
from flask_mysqldb import MySQL

events =[
    {
        'id': '',
        'title': 'prueba',
        'start': '2022-06-04',
        'end':   '',
        'color': 'red'
    }
]

app = Flask(__name__)
app.config['MYSQL_HOST'] = 'LOCALHOST'
app.config['MYSQL_USER'] = 'root'
app.config['MYSQL_PASSWORD'] = ''
app.config['MYSQL_DB'] = 'v1'
mysql = MySQL(app)

app.secret_key = 'Esto_Debe_Ser_Secreto'

@app.route("/")
def index():
    cur = mysql.connection.cursor()
    cur.execute('SELECT c.id, c.motivo, c.fecha, c.color, c.asistencia, u.nombre, u.paterno, u.materno, p.nombre, p.paterno, p.materno FROM tbl_citas AS c INNER JOIN tbl_usuarios AS u ON c.id_dentista = u.id INNER JOIN tbl_pacientes AS p on c.id_paciente = p.id;')
    citas = cur.fetchall()
    return render_template('index.html', citas=citas)

@app.route("/pacientes", methods=('GET', 'POST'))
def pacientes():
    # Mostrar pacientes
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tbl_pacientes')
    pacientes = cur.fetchall()
    if request.method == 'POST':
        nombre      = request.form['nombre']
        paterno     = request.form['paterno']
        materno     = request.form['materno']
        nacimiento  = request.form['nacimiento']
        sexo        = request.form['sexo']
        telefono    = request.form['telefono']
        email       = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tbl_pacientes(nombre, paterno, materno, nacimiento, sexo, telefono, email) VALUES(%s, %s, %s, %s, %s, %s,%s)', (nombre, paterno, materno, nacimiento, sexo, telefono, email))
        mysql.connection.commit()
        return redirect(url_for('pacientes'))
    return render_template('pacientes/pacientes.html', pacientes=pacientes) 

@app.route("/pacientes/eliminar/<string:id>")
def pacienteEliminar(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tbl_pacientes WHERE id LIKE %s", [id])
    mysql.connection.commit()
    return redirect(url_for('pacientes'))

@app.route("/pacientes/editar/<string:id>", methods=('GET', 'POST'))
def pacienteEditar(id):
    data = get_paciente(id)
    if request.method == 'POST':
        nombre      = request.form['nombre']
        paterno     = request.form['paterno']
        materno     = request.form['materno']
        nacimiento  = request.form['nacimiento']
        sexo        = request.form['sexo']
        telefono    = request.form['telefono']
        email       = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE tbl_pacientes SET nombre = %s, paterno = %s, materno = %s, nacimiento = %s, sexo = %s, telefono = %s, email = %s WHERE id = %s", (nombre, paterno, materno, nacimiento, sexo, telefono, email, id))
        mysql.connection.commit()
        return redirect(url_for('pacientes'))
    return render_template('/pacientes/pacientes-editar.html', user=data)

def get_paciente(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tbl_pacientes WHERE id LIKE %s", [id])
    data = cur.fetchone()
    return data

@app.route('/dentistas', methods=('GET', 'POST'))
def dentistas():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tbl_usuarios')
    dentistas = cur.fetchall()
    if request.method == 'POST':
        nombre      = request.form['nombre']
        paterno     = request.form['paterno']
        materno     = request.form['materno']
        nacimiento  = request.form['nacimiento']
        sexo        = request.form['sexo']
        telefono    = request.form['telefono']
        email       = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute('INSERT INTO tbl_usuarios(nombre, paterno, materno, nacimiento, sexo, telefono, email, id_rol) VALUES(%s,%s,%s,%s,%s,%s,%s,2)', (nombre, paterno, materno, nacimiento, sexo, telefono, email))
        mysql.connection.commit()
        return redirect(url_for('dentistas'))
    return render_template('dentistas/dentistas.html', dentistas=dentistas)

@app.route('/dentistas/eliminar/<string:id>')
def dentistaEliminar(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tbl_usuarios WHERE id LIKE %s", [id])
    mysql.connection.commit()
    return redirect(url_for('dentistas'))

@app.route('/dentistas/editar/<string:id>', methods=('GET', 'POST'))
def dentistaEditar(id):
    data = get_user(id)
    if request.method == 'POST':
        nombre      = request.form['nombre']
        paterno     = request.form['paterno']
        materno     = request.form['materno']
        nacimiento  = request.form['nacimiento']
        sexo        = request.form['sexo']
        telefono    = request.form['telefono']
        email       = request.form['email']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE tbl_usuarios SET nombre = %s, paterno = %s, materno = %s, nacimiento = %s, sexo = %s, telefono = %s, email = %s WHERE id = %s", (nombre, paterno, materno, nacimiento, sexo, telefono, email, id))
        mysql.connection.commit()
        return redirect(url_for('dentistas'))
    return render_template('/dentistas/dentistas-editar.html', user=data)

def get_user(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tbl_usuarios WHERE id LIKE %s", [id])
    data = cur.fetchone()
    return data

@app.route("/calendario", methods=('GET', 'POST'))
def calendar():
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tbl_usuarios')
    dentistas = cur.fetchall()
    cur.execute('SELECT * FROM tbl_pacientes')
    pacientes = cur.fetchall()
    cur.execute('SELECT c.id, c.motivo, c.fecha, c.color, c.asistencia, u.nombre, u.paterno, u.materno, p.nombre, p.paterno, p.materno FROM tbl_citas AS c INNER JOIN tbl_usuarios AS u ON c.id_dentista = u.id INNER JOIN tbl_pacientes AS p on c.id_paciente = p.id;')
    citas = cur.fetchall()
    if request.method == 'POST':
        evento      = request.form['evento']
        fecha       = request.form['fecha_inicio']
        color       = request.form['color_evento']
        dentista    = request.form['dentista']
        paciente    = request.form['paciente']
        cur.execute('INSERT INTO tbl_citas(motivo, fecha, color, asistencia, id_dentista, id_paciente) VALUES(%s,%s,%s,%s,%s,%s)', (evento, fecha, color, 2, dentista, paciente))
        mysql.connection.commit()
        return redirect(url_for('index'))
    return render_template('calendar/calendar.html', dentistas=dentistas, pacientes=pacientes, citas=citas)

@app.route('/cita/eliminar/<string:id>')
def citaEliminar(id):
    cur = mysql.connection.cursor()
    cur.execute("DELETE FROM tbl_citas WHERE id LIKE %s", [id])
    mysql.connection.commit()
    return redirect(url_for('index'))

@app.route('/cita/editar/<string:id>', methods=('GET', 'POST'))
def citaEditar(id):
    cita = get_date(id)
    cur = mysql.connection.cursor()
    cur.execute('SELECT * FROM tbl_usuarios')
    dentistas = cur.fetchall()
    cur.execute('SELECT * FROM tbl_pacientes')
    pacientes = cur.fetchall()
    if request.method == 'POST':
        evento      = request.form['evento']
        fecha       = request.form['fecha_inicio']
        color       = request.form['color_evento']
        dentista    = request.form['dentista']
        paciente    = request.form['paciente']
        cur = mysql.connection.cursor()
        cur.execute("UPDATE tbl_citas SET motivo = %s, fecha = %s, color = %s, id_dentista = %s, id_paciente = %s WHERE id = %s", (evento, fecha, color, dentista, paciente, id))
        mysql.connection.commit()
        return redirect(url_for('index'))
    return render_template('/calendar/calendar-edit.html',dentistas=dentistas, pacientes=pacientes, cita=cita)

def get_date(id):
    cur = mysql.connection.cursor()
    cur.execute("SELECT * FROM tbl_citas WHERE id LIKE %s", [id])
    data = cur.fetchone()
    return data

if __name__ == '__main__':
    app.run(port=1000, debug=True)