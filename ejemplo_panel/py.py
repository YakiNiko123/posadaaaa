""" from flaskext.mysql import MySQL
from flask import Flask, render_template, request

app = Flask(__name__)

mysql = MySQL()

app.config['MYSQL_DATABASE_HOST'] = 'localhost'
app.config['MYSQL_DATABASE_PORT'] = 3306  
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = ''
app.config['MYSQL_DATABASE_DB'] = 'posada'

mysql.init_app(app)

conexion = mysql.connect()
cursor = conexion.cursor()



@app.route("/")
def index():
    return render_template("panel.html")

@app.route("/panel/buscadorReserva", methods=['POST'])
def reservas():


    reservas = request.form["num_reserva"]
    print('codigo: ', reservas)

    if reservas.isdigit():
        sql = f"SELECT * FROM clientes WHERE cedula = '{reservas}' "
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conexion.commit()
        print(resultado)
        return render_template("panel.html")
    else:
        sql = f"SELECT * FROM reservas WHERE codigo_reserva = '{reservas}'"
        cursor.execute(sql)
        resultado = cursor.fetchall()
        conexion.commit()
        print(resultado)
        return render_template("panel.html",reservas=resultado)
    
@app.route("/panel/buscadorProducto", methods=['POST'])
def productos():
    busqueda = request.form["busqueda_producto"]
    print('Búsqueda:', busqueda)

    
    if busqueda.isdigit():
         
        sql = f"SELECT * FROM productos WHERE codigo_producto ='{busqueda}'"
        
        
    else:
      
      sql = f"SELECT * FROM productos WHERE descripcion ='{busqueda}'"

    print('Consulta SQL:', sql)

    cursor.execute(sql)
    resultado = cursor.fetchall()
    conexion.commit()
    print('Resultado:', resultado)  

    return render_template("panel.html", productos=resultado)

    





if __name__ == '__main__':
    app.run(debug=True)



 """