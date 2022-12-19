#EXAMEN PARCIAL MODULO TRES#
#NNOTA: Todo el examen esta desarrollado en este único archivo "manuel.py"
# ejercicio1 : creacion de base de datos "Colegio"------------------------
import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="willito",
    )
mycursor=mycon.cursor()
mycursor.execute("CREATE DATABASE colegio")
# ejercicio2: comprbando con código la creación de la base de datos "colegio"
import mysql.connector
from mysql.connector import Error
try:
    mycon=mysql.connector.connect(
         host="localhost",
         port="3306",
         user="root",
         password="willito",
         database="colegio"
    )
    if mycon.is_connected():
        print("ES COORECTO LA CREACION DE LA BASE DE DATOS COLEGIO")
except Error as ex:
    print("No SE PUDO CREAR LA BASE DE DATOS¡¡¡", ex)

#ejercicio 3: Creación de base de datos "tiendas" .......................................
import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="willito",
    )
mycursor=mycon.cursor()
mycursor.execute("CREATE DATABASE tienda")
# agregando las tablas "productos","clientes"
import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="willito",
    database="tienda"
    )
mycursor=mycon.cursor()
mycursor.execute("CREATE TABLE productos(id INT AUTO_INCREMENT PRIMARY KEY, descripción VARCHAR(60), precio INT(50), descuento INT(60))")
mycursor.execute("CREATE TABLE clientes(id INT AUTO_INCREMENT PRIMARY KEY, nombre VARCHAR(60), apellido VARCHAR(50), edad INT(60), dni INT(50))")


# 3.1 operaciones en la tablas "productos"

import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="willito",
    database="tienda"
    )
mycursor=mycon.cursor()

query="INSERT INTO productos(descripción,precio,descuento) VALUES (%s,%s,%s)"
valores=[
    ('leche gloria',4.50,0.70),
    ('agua mineral cielo',2.50,0.50),
    ('galleta casino',1.00,0.20),
    ('gaseosa inka kola',2.70,0.20)
]
mycursor.executemany(query,valores)
mycon.commit()
print(mycursor.rowcount,"Registros de los productos") 
# selecionar todos los registros 
import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="willito",
    database="tienda"
    )
mycursor=mycon.cursor()
mycursor.execute("SELECT * FROM productos")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# selecionar únicammente el segundo registro: este es iguala :"agua mineral cielo"
import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="willito",
    database="tienda"
    )
mycursor=mycon.cursor()
query="SELECT * FROM productos WHERE descripción ='agua mineral cielo'"
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
      print(x)
#eliminar un registro determinado: en este caso el de galleta casino
import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="willito",
    database="tienda"
    )
mycursor=mycon.cursor()
query = "DELETE FROM productos WHERE descripción ='galleta casino'"
mycursor.execute(query)
mycon.commit()
print(mycursor.rowcount )
mycursor.execute("SELECT * FROM productos")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)
# alterar la estructura de la tabla : el modo sera usando order
mycursor = mycon.cursor()
query = "SELECT * FROM productos ORDER BY precio"
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
  print(x)


#3.2 operaciones en la tabla "clientes"-------------------------

# agregando 9 registros
import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="willito",
    database="tienda"
    )
mycursor=mycon.cursor()

query="INSERT INTO clientes(nombre,apellido,edad,dni) VALUES (%s,%s,%s,%s)"
valores=[
    ('Gloria','Porras',27,45678921),
    ('Minerva','Valladolid',50,12955768),
    ('Mariela','Perez',24,48678921),
    ('Manuel','Guerra',30,17355768),
    ('Marta','Piñas',44,42678921),
    ('Juan','Quispe',20,92355768),  
    ('Edward','Ordaya',34,41678921),
    ('Wendy','Berrú',30,14355768),
    ('Hansi','Matos',40,11355768)
]
mycursor.executemany(query,valores)
mycon.commit()
print(mycursor.rowcount,"Registro hechos") 
#selecionar todos los registros
import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="willito",
    database="tienda"
    )
mycursor=mycon.cursor()
mycursor.execute("SELECT * FROM clientes")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# selecionar únicammente un registro mediante WHERE: selecionamos Wendy Berru
import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="willito",
    database="tienda"
    )
mycursor=mycon.cursor()
query="SELECT * FROM clientes WHERE nombre ='Wendy'"
mycursor.execute(query)
myresult = mycursor.fetchall()
for x in myresult:
      print(x)
#eliminar un registro determinado:eliminamos a Gloria Porras con DNI: 45678921
import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="willito",
    database="tienda"
    )
mycursor=mycon.cursor()
query = "DELETE FROM clientes WHERE dni = 45678921"
mycursor.execute(query)
mycon.commit()
print(mycursor.rowcount )
mycursor.execute("SELECT * FROM clientes")
myresult = mycursor.fetchall()
for x in myresult:
  print(x)

# alterar la estructura de la tabla para gregar "tipo de sangre"
import mysql.connector
mycon=mysql.connector.connect(
    host="localhost",
    port="3306",
    user="root",
    password="willito",
    database="tienda"
    )
mycursor=mycon.cursor()
mycursor.execute("ALTER TABLE clientes ADD COLUMN tipo_de_sangre VARCHAR(50)")


# NOTA :  lA PREGUNTA 4 ESTA EN LA HOJA DEL WORD RESUELTO


































