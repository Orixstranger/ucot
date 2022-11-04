from flask import Flask
from flask import render_template,request,redirect,url_for,flash
from flaskext.mysql import MySQL
#para visualizar las imagenes flask
from flask import send_from_directory
#proteccion para autentificaciones no logueadas al servidor
from flask_wtf.csrf import CSRFProtect
#importar para las sesiones, para determinadas rutas no se accedan mientras no usuarios logueados
from flask_login import LoginManager,login_user,logout_user,login_required
#nombrar el nombre de la foto de acuerdo al tiempo
from datetime import datetime
#Acceso a las fotografias
import os
#flash sirve para validación (enviar mensajes)

#config
from configparser import ConfigParser

#importo paquete models
from models.ModelUser import ModelUser

#imporrto las entidades
from models.entries.User import User

#creamos la app
app= Flask(__name__)
app.secret_key="Develoteca"

#proteccion para ingresos al servidor no autorizados
csrf=CSRFProtect()

#usaremos las instrucciones del mysql, con la base de datos
mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='ucot'
mysql.init_app(app)

login_manager_app=LoginManager(app)
@login_manager_app.user_loader
def load_user(id):
    return ModelUser.get_by_id(mysql,id)

#carpeta para manipulacion de fotografias
CARPETA=os.path.join('uploads')
app.config['CARPETA']=CARPETA

#crear un acceso url para visualizar imagenes a través del directorio
@app.route('/uploads/<nombreFoto>')
def uploads(nombreFoto):
    return send_from_directory(app.config['CARPETA'],nombreFoto)

#routeo, recibe la url
@app.route('/inicio')
@login_required
def index():
    #generamos una instruccion mysql
    sql = "SELECT * FROM `empleado`;"
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql)
    
    #selecciona todos los registro y los presenta con las instruccion sql SELECT
    empleados=cursor.fetchall()
    print(empleados)

    conn.commit()


    return render_template("empleados/index.html", empleados=empleados)

#Borrado de datos de la BD
@app.route('/destroy/<int:id>')
@login_required
def destroy(id):
    conn = mysql.connect()
    cursor=conn.cursor()

    cursor.execute("SELECT fotografia FROM empleado WHERE id=%s", id)
    fila=cursor.fetchall()
    os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))

    cursor.execute("DELETE FROM empleado WHERE id=%s",id)
    conn.commit()
    return redirect('/inicio')

#Edición de datos de la BD
@app.route('/edit/<int:id>')
@login_required
def edit(id):
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute("SELECT * FROM empleado WHERE id=%s", (id))
    empleados=cursor.fetchall()
    conn.commit()
    print(empleados)

    return render_template('empleados/edit.html', empleados=empleados)

#Actualizar los datos    
@app.route('/update', methods=['POST'])
@login_required
def update():

    _codigo=request.form['txtCodigo']
    _nombre=request.form['txtNombre']
    _apellido=request.form['txtApellido']
    _cedula=request.form['txtCedula']
    _edad=request.form['txtEdad']
    _telefono=request.form['txtTelefono']
    _correo_electronico=request.form['txtCorreoElectronico']
    _localidad=request.form['txtLocalidad']
    _estado=request.form['txtEstado']
    _reconocimientos=request.form['txtReconocimientos']
    _sanciones=request.form['txtSanciones']
    _c1=request.form['txtC1']
    _c2=request.form['txtC2']
    _fotografia=request.files['txtFotografia']
    id=request.form['txtID']
    #generamos una instruccion mysql
    sql = "UPDATE empleado SET codigo=%s, nombre=%s, apellido=%s, cedula=%s, edad=%s, telefono=%s, correo_electronico=%s, localidad=%s, estado=%s, reconocimientos=%s, sanciones=%s, c1=%s, c2=%s WHERE id=%s;"
    
    datos = (_codigo,_nombre,_apellido,_cedula,_edad, _telefono, _correo_electronico,_localidad,_estado,_reconocimientos, _sanciones, _c1, _c2, id)

    conn = mysql.connect()
    cursor=conn.cursor()
    
    #obtenemos la información de la foto, se remueva y actualice
    now= datetime.now()
    tiempo=now.strftime("%Y%H%M%S")
    
    if _fotografia.filename!='':
        
        nuevoNombreFoto=tiempo+_fotografia.filename
        _fotografia.save("uploads/"+nuevoNombreFoto)

        cursor.execute("SELECT fotografia FROM empleado WHERE id=%s", id)
        fila=cursor.fetchall()

        os.remove(os.path.join(app.config['CARPETA'],fila[0][0]))
        cursor.execute("UPDATE empleado SET fotografia=%s WHERE id=%s",(nuevoNombreFoto,id))
        conn.commit()


    cursor.execute(sql,datos)
    
    conn.commit()
    
    return redirect('/inicio')


#Creación de nuevo empleado
@app.route('/create')
@login_required
def create():
    return render_template('empleados/create.html')

#Insertar un nuevo empleado
@app.route('/store', methods=['POST'])
@login_required
def storage():
    _codigo=request.form['txtCodigo']
    _nombre=request.form['txtNombre']
    _apellido=request.form['txtApellido']
    _cedula=request.form['txtCedula']
    _edad=request.form['txtEdad']
    _telefono=request.form['txtTelefono']
    _correo_electronico=request.form['txtCorreoElectronico']
    _localidad=request.form['txtLocalidad']
    _estado=request.form['txtEstado']
    _reconocimientos=request.form['txtReconocimientos']
    _sanciones=request.form['txtSanciones']
    _c1=request.form['txtC1']
    _c2=request.form['txtC2']
    _fotografia=request.files['txtFotografia']

    if _nombre=='' or _correo_electronico=='' or _fotografia=='':
        flash('Recuerda llenar los datos de los campos')
        return redirect(url_for('create'))
    
    #concatemanos solamente el nombre de la foto
    #obtenemos el tiempo de la foto
    now= datetime.now()
    tiempo=now.strftime("%Y%H%M%S")
    #ya sobreescrito con la fecha se guarda en la carpeta uploads
    if _fotografia.filename!='':
        nuevoNombreFoto=tiempo+_fotografia.filename
        _fotografia.save("uploads/"+nuevoNombreFoto)

    #generamos una instruccion mysql
    sql = "INSERT INTO `empleado` (`codigo`, `nombre`, `apellido`, `cedula`, `edad`, `telefono`, `correo_electronico`, `localidad`, `estado`, `reconocimientos`, `sanciones`, `c1`, `c2`, `fotografia`) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"
    
    datos = (_codigo,_nombre,_apellido,_cedula,_edad, _telefono, _correo_electronico,_localidad,_estado,_reconocimientos, _sanciones, _c1, _c2, nuevoNombreFoto)

    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,datos)
    conn.commit()
    return redirect('/inicio')

@app.route('/buscarEmpleado')
def buscarEmpleado():
    return render_template('empleados/buscar.html')

@app.route('/buscar', methods=['POST'])
def buscar():
    _buscarUsuario=request.form['buscarUsuario']
    #generamos una instruccion mysql
    sql = "SELECT * FROM `empleado` WHERE codigo=%s OR cedula=%s OR apellido=%s;"
    #cursor.execute("UPDATE empleado SET fotografia=%s WHERE id=%s",(nuevoNombreFoto,id))
    print('****************************************')
    conn = mysql.connect()
    cursor=conn.cursor()
    cursor.execute(sql,(_buscarUsuario,_buscarUsuario,_buscarUsuario))
    
    #selecciona todos los registro y los presenta con las instruccion sql SELECT
    empleados=cursor.fetchall()
    print(empleados)

    conn.commit()


    return render_template("empleados/index.html", empleados=empleados)
    return print('entre a buscar')
    
#Creación de login
@app.route('/')
def login2():
    return redirect(url_for('login'))

@app.route('/login', methods=['GET','POST'])
def login():
    
    if request.method == 'POST':
        #print(request.form['username'])
        #print(request.form['password'])
        user = User(0,request.form['username'],request.form['password'])
        logged_user = ModelUser.login(mysql,user)
        if logged_user != None:
            print("///////////////",logged_user.password)
            if logged_user.password:
                login_user(logged_user)
                return redirect('/inicio')
            else:
                print("*******************************")
                flash("Contraseña invalida...")
                return render_template('auth/login.html')
        else:
            print("*******************************")
            flash("Usuario no encontrado...")
            return render_template('auth/login.html')
    else:
        return render_template('auth/login.html')    

@app.route('/logout')
def logout():
    logout_user()
    return redirect('/login')

def status_401(error):
    return redirect(url_for('login'))

def status_404(error):
    return "<h1>Pagina no encontrada<h1/>", 404

if __name__ == '__main__':
    app.config.from_object(ConfigParser['development'])
    csrf.init_app(app)
    app.register_error_handler(401,status_401)
    app.register_error_handler(404,status_404)
    app.run(debug=True)