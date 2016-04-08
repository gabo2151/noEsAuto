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
	print "[3] Verificar palabra"
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
		def muestraNombres(lista):
			for i in range(len(lista)):
				print  lista[i].nombre


		def validaEstado(nombreestado):
			for i in range(len(listaestados)):
				if listaestados[i].nombre == nombreestado:
					return True
					break
				return False

		#variables
		listaestados = [] #lista de objetos tipo estado
		l = []

		#Solicitando nombre estado inicial
		estadoinicial = raw_input("Ingrese estado inicial: ")
		while type(estadoinicial) != str:
			estadoinicial = raw_input("Ingrese estado inicial: ")
		listaestados.append(Estado(estadoinicial))

		listaestados[0].inicial=True

		#Solicitando las transiciones
		trans = raw_input("Ingrese transicion de la forma estado simbolo estado, ej q0 a q1: ")
		while trans != "":
			l = trans.split()
			if validaEstado(l[0]): #valido si existe el estado a partir del nombre
				print "El estado ya existe, no es necesario crear uno"
				listaestados[0].indices[l[1]]=l[2]
			else: #si el estado no existe, lo creo, y agrego el indice
				listaestados.append(Estado(l[0]))
				listaestados[0].indices[l[1]]=l[2]

			if validaEstado(l[2]):#para el estado de llegada a traves de la transicion no es necesario crearle un indice ni nada :captainobvious:
				print validaEstado(l[2])
				print "El estado ya existe, no es necesario crear uno"

			else:
				listaestados.append(Estado(l[2]))

			l =[]
			muestraNombres(listaestados) #muestro los estados
			print listaestados[0].indices #muestro los indices
			trans = raw_input("Ingrese transicion de la forma estado simbolo estado, ej q0 a q1: ")



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
				
				""" Cambiar si es estado final o no
				talvez = raw_input("Desea que el estado "+ listaestados[numE].nombre+" sea estado final (si o no): ")
				while talvez !="si" and talvez != "no":
					talvez = raw_input("Desea que el estado "+ listaestados[numE].nombre+" sea estado final (si o no): ")
				if talvez == "si":
					listaestados[numE].final = True
				else:
					listaestados[numE].final = False"""

				alfa = raw_input("Ingrese simbolo del alfabeto: ")
				dirr = raw_input("Ingrese el numero del estado al cual se conecta\ncon el simbolo: ")
				listaestados[numE].data()[alfa] = dirr

				pause()

			elif opc == 3: # Probar palabra
				eA = 0 #Estado actual
				cuenta = 0
				testWord = raw_input("Ingrese la palabra a analizar\n=> :")
				for key in testWord:
					if key in listaestados[eA].indices:
						eA = int( listaestados[eA].indices[key][1] )
						cuenta +=1
					else:
						print "La palabra no pertenece a este lenguaje"
						break

					if cuenta == len(listaestados)-1:
						if listaestados[eA].final:
							print "La palabra pertenece al lenguaje"
							break
						else:
							print "La palabra no pertenece a este lenguaje"
							break


				pause()

	# Inicio del modo GUI
	elif selGUI == 1:
		print "Iniciando GUI..."
		pause()

#interfaz grafica
