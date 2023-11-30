import re
from flaskext.mysql import MySQL
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


@app.route("/reservas",methods=['POST'])
def reservas():
    codigo = request.form ['num_reserva']
    estructura = re.compile(r'^\d[A-Z][A-Z]\d{3}[A-F]$')
    #que no se me olvide : /d = numero az son letras si al /d se le ponen corchetes es cuantos numeros va a poder usar 
    if (codigo) and (len(codigo)>6):
        if estructura.match(codigo):
            consulta=f"SELECT * FROM reservas WHERE codigo ='{codigo}'"
            cursor.execute(consulta)
            resultado_reserva= cursor.fetchall()
            conexion.commit()
            if resultado_reserva:   

                return render_template('panel.html',resultado_reserva = resultado_reserva)
            else: 
                mensaje = 'No Existe papi'
                return render_template('panel.html',mensaje=mensaje)
                
            
        elif all(c.isdigit() for c in codigo):
            consulta=f"SELECT * FROM reservas WHERE cedula ='{codigo}'"
            cursor.execute(consulta)
            resultado_reserva= cursor.fetchall()
            conexion.commit()
            if resultado_reserva:   

                return render_template('panel.html',resultado_reserva = resultado_reserva)
            else: 
                mensaje = 'No Existe papi'
                return render_template('panel.html',mensaje=mensaje)
            
        
        else:
            mensaje = 'No Existe papi'
            return render_template('panel.html',mensaje = mensaje)
    else:
        mensaje = 'No Existe papi'
        return render_template('panel.html',mensaje = mensaje)

        
#busca prioducto si es un codifgo o nombre 
@app.route("/productos",methods=['POST'])
def productos():
    producto = request.form['busqueda_producto']
    if (producto) and (len(producto)>2):
        #all todos son numeros 
        if all(c.isdigit() for c in producto):
            consulta=f"SELECT * FROM productos WHERE codigo_barra ='{producto}'"
            cursor.execute(consulta)
            resultado_producto= cursor.fetchall()
            conexion.commit()
            if resultado_producto:   

                return render_template('panel.html',resultado_producto = resultado_producto)
            else: 
                mensaje = 'No Existe papi'
                return render_template('panel.html',mensaje=mensaje)
            
            
        
        #el any es que contiene no importa si todos son iguales o diferentes simplemente lo contiene // contiene letras mayusculas o minusculas 
        elif any(c.isalpha() and c.islower() for c in producto):
            consulta=f"SELECT * FROM productos WHERE nombre ='{producto}'"
            cursor.execute(consulta)
            resultado_producto= cursor.fetchall()
            conexion.commit()
            if resultado_producto:   

                return render_template('panel.html',resultado_producto = resultado_producto)
            else: 
                mensaje = 'No Existe papi'
                return render_template('panel.html',mensaje=mensaje)
            
        else: 
            mensaje="No Existe papi"
            return render_template('panel.html',mensaje=mensaje)
    else: 
            mensaje="No Existe papi"
            return render_template('panel.html',mensaje=mensaje)
    

          





    


        
            

    



if __name__ == '__main__':
    app.run(debug=True)


