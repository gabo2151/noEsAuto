"""La tarea consiste en diseñar y construir un programa computacional capaz de
simular cualquier AFD"""
#La entrada al programa consiste en: estado inicial, estados finales
#transiciones del AFD, palabra de entrada

#La salida un mensaje indicando si pertenece o no al lenguaje

#El programa debe poder analizar muchas palabras de entrada
#Debe ser autoexplicativo


class Estado:
	def __init__(self, nombre):
		self.nombre = nombre



print "-----------Teoria de Automatas--------------\nSimulador de Automatas Finitos Deterministas\nAutores: Elliot Ide, Gabriel Galilea, Javier Godoy"
print "*********************************************"

#variables
listaestados = [] #lista de objetos tipo estado


n = input("Ingrese numero de estados (Debe ser mayor a 0): ")
while n<=0:
        n = input("Ingrese numero de estados (Debe ser mayor a 0): ")


x = raw_input("Ingrese simbolo de largo 1 que represente a todos sus estados (Ej: q => q0, q1, ..., qn): ")
while(len(x)!=1):
      x = raw_input("Ingrese simbolo de largo 1 que represente a todos sus estados (Ej: q => q0, q1, ..., qn): ")

for i in range(n):
        listaestados.append(Estado(x+str(i)))

#demostracion
for i in range(n):
        print listaestados[i].nombre


#interfaz grafica
