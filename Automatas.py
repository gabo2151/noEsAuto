"""La tarea consiste en diseniar y construir un programa computacional capaz de
simular cualquier AFD"""
# La entrada al programa consiste en: estado inicial, estados finales
# transiciones del AFD, palabra de entrada
#
# La salida un mensaje indicando si pertenece o no al lenguaje
#
# El programa debe poder analizar muchas palabras de entrada
# Debe ser autoexplicativo

import os
import string

# Definir una funcion de pausa... por comodidad
def pause():
	raw_input("Presione ENTER para continuar...")

# Una funcion de interfaz de consola para liberar de espacio en medio del codigo
def menuConsola():
	print "==MENU==================================="
	print "[1] Imprime nodos y conecciones actuales"
	print "[2] Editar un estado"
	print "[0] Salir"

class Estado:
	def __init__(self, nombre):
		self.nombre = nombre
		self.inicial = False
		self.final = False
		self.indices = {}

	# Sirve para editar tambien***
	def addIndice(self, caracter, direccion):
		# La direccion debiese de ser el numero del indice
		self.indices[caracter] = direccion

	def data(self):
		return self.indices

if __name__ == "__main__":
	os.system('cls' if os.name == 'nt' else 'clear')
	print "--------------Teoria de Automatas-----------------\nSimulador de Automatas Finitos Deterministas\nAutores: Elliot Ide, Gabriel Galilea, Javier Godoy"
	print "**************************************************\n"

	#Seleccion consola o GUI
	while True:
		selGUI = raw_input("Iniciar en consola [0] o iniciar GUI [1]: ")
		if selGUI == "0" or selGUI == "1":
			selGUI = int(selGUI)
			break

	# Inicio de modo consola
	if selGUI == 0:
		# Metodo para buscar en una lista, el elemento x sabiendo que esta en la
		# lista y devolver el indice
		def encuentraPos(lista,x):
			c = 0
			for i in range(len(lista)):
				if lista[i] == x:
					return c
				else: c = c + 1

		#variables
		listaestados = [] #lista de objetos tipo estado
		listanombres = []

		# Numero de estados/nodos
		n = input("Ingrese numero de estados (Debe ser mayor a 0): ")
		while n<=0:
			n=input("Ingrese numero de estados (Debe ser mayor a 0): ")

		# Elegir la letra de los estados, puede ser q, o, p, etc...
		x = raw_input("Ingrese simbolo de largo 1 que represente a todos sus estados (Ej: q => q0, q1, ..., qn): ")
		while(len(x)!=1):
			x = raw_input("Ingrese simbolo de largo 1 que represente a todos sus estados (Ej: q => q0, q1, ..., qn): ")

		# Crea los estados y los almacena en la lista
		for i in range(n):
			listaestados.append(Estado(x+str(i)))

		#demostracion
		for i in range(n):
			print listaestados[i].nombre
			
		listaestados[0].inicial = True

		pause()

		# INICIO DE LA INTERFAZ EN CONSOLA
		while True: #Loop infinito para ejecutar el programa sin terminarlo
			os.system('cls' if os.name == 'nt' else 'clear')
			menuConsola()
			opc = input("Elija una opcion: ")
			print "=========================================\n"

			if opc == 0: # Termina el programa
				break #Termina el while

			elif opc == 1:
				for i in listaestados:
					print "Nombre: %s\nIndices: " % i.nombre
					print i.indices

				pause()

			elif opc == 2: # Edita estados
				est = ""
				for i in range(n):
					est += listaestados[i].nombre + " "
				print est
				print "Seleccione el estado que desee editar (por su numero)"
				numE = int(raw_input("Num: "))
				print "Estado actual del estado:"
				print listaestados[numE].data()
				print "Edicion\n"
				
				# Cambiar si es estado final o no
				talvez = raw_input("Desea que el estado "+ listaestados[numE].nombre+" sea estado final (si o no): ")
				while talvez !="si" and talvez != "no":
					talvez = raw_input("Desea que el estado "+ listaestados[numE].nombre+" sea estado final (si o no): ")
				if talvez == "si":
					listaestados[numE].final = True
				else:
					listaestados[numE].final = False

				alfa = raw_input("Ingrese simbolo del alfabeto: ")
				dirr = raw_input("Ingrese el numero del estado al cual se conecta\ncon el simbolo: ")
				listaestados[numE].data()[alfa] = dirr

				pause()

	# Inicio del modo GUI
	elif selGUI == 1:
		print "Iniciando GUI..."
		pause()

#interfaz grafica
