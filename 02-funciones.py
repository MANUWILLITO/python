# FUNCIONES RETORNO DE VALOR (RETORNO DE DATOS)
# Son aquellas que permiten recibir argumentos, operarlos y devolver un resultado (datos o en informacion)

# PROBLEMA 01:
# Trababajar con el area del trapecio mediante una funcion que permita devolver el resultado.
""" 
# FD
def halla_area_trapecio(base_mayor, base_menor, altura):
    area_trapecio = ((base_mayor + base_menor) * altura) / 2
    return area_trapecio
# PP
base_mayor = int(input("Ingerse la base mayor del trapecio: "))
base_menor = int(input("Ingrese la base menor del trapecio: "))
altura = int(input("Ingrese la altura del trapecio: "))

area_trapecio = halla_area_trapecio(base_mayor, base_menor, altura)
print("El area del trapecio es: ", area_trapecio)
 """
# print(halla_area_trapecio(base_mayor, base_menor, altura))

# PROBLEMA 02
# Elaboara una LI, en la cual se envie por teclado dos numeros enteros,
# luego los compare y retorne el mayor de dichos numeros.
# NOTA: utilizar funciones con retorno de valor.
""" 
# FD
def retornar_mayor(num1, num2):
    if num1 > num2:
        num_mayor = num1
    else:
        num_mayor = num2
    
    return num_mayor

# PP
numero_1 = int(input("Ingrese un 1er número: "))
numero_2 = int(input("Ingrese un 2do número: "))
mayor = retornar_mayor(numero_1, numero_2)
print("El número mayor es: ", mayor)

# print("El numero mayores es: ", retornar_mayor(numero_1, numero_2))
"""

# PROBLEMA 03
# Elaborar una LI, en la cual se ingrese por teclado una primera cordenada (x1, y1) y
# luego una segunda cordenada (x2. y2), con dicha informacion obtener la distancia entre 
# dichos puntos, utilizando paramentros y retorno de valor.
""" 
# FD
def distanciaDepuntos(x1, y1, x2, y2):
    distancia =  ((x1 - x2) ** 2 + (y1 - y2) ** 2) ** 0.5
    return distancia
# PP
print("Hallar la distancia entre dos puntos")
print("Ingrese el Primer punto (x1, y1)")
x1 = int(input("Ingrese x1: "))
y1 = int(input("Ingrese y1: "))
print("Ingrese el Segundo punto (x2, y2)")
x2 = int(input("Ingerse x2: "))
y2 = int(input("Ingerse y2: "))

resultado = distanciaDepuntos(x1, y1, x2, y2)
print("La distancia entre los puntos es: ", resultado)

# print("La distancia entre los puntos es: ", distanciaDepuntos(x1, y1, x2, y2))

"""
# FUNCIONES DECLARADAS

# Ejemplo 01
""" 
# FD
def suma(numero_1=10, numero_2=20):
    suma = numero_1 + numero_2
    print("la suma total es:", suma)
# PP
suma(50,50)

"""

# Ejemplo 02
""" 
# FD
def longitud_cadena(cad_apellido, saludo = ", Gracias que tengas un buen día"):
    print("Tu apellido es:", cad_apellido)
    print("Tu apellido tiene", len(cad_apellido), "caracteres", saludo)
# PP
Apellido = input("Ingrese su apellido: ")
Saludo = input("Ingrese un Saludo: ")
longitud_cadena(Apellido, Saludo)
"""

# PROBLEMA PROPUESTO
# Elaborar una LI, en la cual se realicen las operaciones de:
# *, / , // y % a traves de funciones con paremetros,
# los cuales soliciten ingresar un par de datos enteros y luego de operarlos
# devuelvan un valor como resultado a donde estas fueron invocadas, para luego
# mostrarlo en pantalla.








