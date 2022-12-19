# PARADIGMA DE PROGRAMACIÓN ORIENTADA A OBJETOS

# Vamos a trabajar con clases, metodos, objetos (creacion de objetos)
# Vamos a definir objetos e instanciar objetos.

# Objeto, atributos, metodo, clase 

# OBJETO: Es todo aquello que se puede abstraer de la vida real, el cual tiene sus propias
# caracteristicas (sus datos, información, programación, tiene acciones propias a realizar)

#     ATRIBUTOS: Son caracteristicas basicas de un objeto, sean fisicas o no fisicas.
#     METODO: Son las acciones que puede realizar un objeto.

# CLASE: Nos ayuda a definir un objeto en concreto.
#     INSTANCIA (Instancia de una clase o instancia de la Abstracción Objeto): Aquella que me ayuda a replicar los atributos y metodos
#                                                 de un objeto.
""" 
# CD
class Galleta:
    #Atributos
    sabor = "Vainilla"
    forma = "Circular"
    color = "Amarillo"
    olor = "Vainilla y Canela"
    peso = "15 gramos"
    marca = "Sayon"
    caducidad = "25/12/2023"
    #Metodos (acciones que realizar el objeto o relacionadas al objeto --> funciones)
    def cantidad_de_galletas(self):
        print("La cantidad de galletas es 20.")  
    def caducidad_de_galletas(self):
        print("Vencimiento el 25/12/2023")
# PP
galleta_1 = Galleta()
galleta_1.cantidad_de_galletas()
galleta_1.caducidad_de_galletas()

galleta_2 = Galleta()
galleta_2.caducidad_de_galletas()
galleta_2.cantidad_de_galletas()

 """

# PROBLEMA 01
# Elaborar una LI, con una clase Persona, la cual tiene como atributos
# nombre y como metodo imprimir nombre.
""" 
# DC
class Persona:

    def recibir_nombre(self, nombre):
        self.nom = nombre

    def imprimir_nombre(self):
        print("El nombre ingresado es:", self.nom)
# PP

persona_1 = Persona()
persona_1.recibir_nombre("Luis Angel")
persona_1.imprimir_nombre()

persona_2 = Persona()
persona_2.recibir_nombre("Victor Andre")
persona_2.imprimir_nombre()
"""

# # PROBLEMA 02
# Elaborar una LI, en la cua se tenga una clase Persona, con atributos
# nombre, apellido, dni y que cuente con con dos metodos, guardar datos y otro metodo, mostrar datos.
""" 
class Persona:

    def guardar_datos(self, nombre, apellido, dni):
        self.nom = nombre
        self.ape = apellido
        self.dni = dni 

    def mostrar_datos(self):
        print("El nombre ingresado es: ", self.nom)
        print("EL apellido ingresado es: ", self.ape)
        print("El dni ingresado es: ", self.dni)
#Programa principal
persona_1 = Persona()
persona_1.guardar_datos("Luis", "Gamarra", "412545875")
persona_1.mostrar_datos()
print("*************************")
persona_2 = Persona()
persona_2.guardar_datos("Jorge", "Alina", "124574894")
persona_2.mostrar_datos()
print("*************************")
persona_3 = Persona()
persona_3.guardar_datos("Fiorela", "Arroyo", "1245789563")
persona_3.mostrar_datos()

"""

# PROBLEMA 03
# Elaborar una LI, que contanga una clase estudiante, la cual incluya los atributos de
# codigo, nombre, calificacion.
# Crear metodos, para los atributos, para imprimir en pantalla los datos y mostrar
# si se endcuenta aprobado el estudiante.
# NOTA: calificacion recibida es el promedio final de ciclo (Minimo aprobatorio 11)
 
# CD
class Estudiante:
    def guardar_atributos(self, codigo, nombre, calificacion):
        self.cod = codigo
        self.nom = nombre
        self.calif = calificacion

    def imprimir_pantalla(self):
        print("El codigo de estudiante es: ", self.cod)
        print("El nombre del estudiante es: ", self.nom)
        print("La calificación promedio es: ", self.calif)

    def mostrar_estado(self):
        if self.calif >= 11:
            print("Estado: Se encuentra aprobado.")
        else:
            print("Estado: Se encuentra reprobado.")
# PP

estudiante_1 = Estudiante()
estudiante_1.guardar_atributos(14526387, "Lisset Elescano", 18)
estudiante_1.imprimir_pantalla()
estudiante_1.mostrar_estado()
print("****************")
estudiante_2 = Estudiante()
estudiante_2.guardar_atributos(74856213, "Luis Andres", 17)
estudiante_2.imprimir_pantalla()
estudiante_2.mostrar_estado()












