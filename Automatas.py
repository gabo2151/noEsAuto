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

		#Funciones
		def muestraAtributos():
			for i in range(len(listaestados)):
				print listaestados[i].nombre
				print listaestados[i].indices


		def validaEstado(nombreestado):
			for i in range(len(listaestados)):
				if listaestados[i].nombre == nombreestado:
					return True
					break
			return False

		def validaTrans(pos,clave):
			if clave in listaestados[pos].indices:
				return True
			else:
				return False

		def devuelvePos(nombreestado):
			for i in range(len(listaestados)):
				if listaestados[i].nombre == nombreestado:
					return i
					break

		#Variables
		listaestados = [] #lista de objetos tipo estado
		l = []
		c = 0

		#Estado inicial
		estadoinicial = raw_input("Ingrese estado inicial (q0): ")
		while type(estadoinicial) != str:
			estadoinicial = raw_input("Ingrese estado inicial (q0): ")
		listaestados.append(Estado(estadoinicial))

		listaestados[0].inicial=True

		#Transiciones
		trans = raw_input("Ingrese transicion de la forma estado simbolo estado, Ej: q0 a q1: ")
		while trans != "":
			l = trans.split()
			#primer estado en la transicion
			if validaEstado(l[0]): #si el estado existe, solo agrego su transicion al diccionario indices
				print "El estado ya existe"
				c = devuelvePos(l[0])
				if validaTrans(c,l[1]):
					print "Ya existe una transicion asociada a este simbolo"
				else:
					listaestados[c].indices[l[1]]=l[2]

			else: #si el estado no existe, lo creo, y luego agrego la transicion
				listaestados.append(Estado(l[0]))
				c = devuelvePos(l[0])
				listaestados[c].indices[l[1]]=l[2]

			#segundo estado en la transicion
			if validaEstado(l[2]):
				print "El estado ya existe"

			else:
				listaestados.append(Estado(l[2]))

			l =[]
			muestraAtributos()
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
					print

				pause()

			elif opc == 2: # Edita estados
				est = ""
				for i in range(len(listaestados)):
					est += listaestados[i].nombre + " "
				print est
				print "Seleccione el estado que desee editar (por su numero)"
				numE = int(raw_input("Num: "))
				print "Estado actual del estado:"
				print listaestados[numE].data()
				print "Edicion\n"
				
				maybe1 = raw_input("Desea cambiar tipo de estado? (si o no)\n")
				while maybe1 !="si" and maybe1 != "no":
					maybe1 = raw_input("Desea cambiar tipo de estado? (si o no)\n")
				if maybe1 == "si":
					#Cambiar si es estado final o no
					talvez = raw_input("Desea que el estado "+ listaestados[numE].nombre+" sea estado final (si o no): ")
					while talvez !="si" and talvez != "no":
						talvez = raw_input("Desea que el estado "+ listaestados[numE].nombre+" sea estado final (si o no): ")
					if talvez == "si":
						listaestados[numE].final = True
					else:
						listaestados[numE].final = False

				maybe2 = raw_input("Desea cambiar alguna transicion? (si o no)\n")
				while maybe2 !="si" and maybe2 != "no":
					maybe2 = raw_input("Desea cambiar alguna transicion? (si o no)\n")
				if maybe2 == "si":
					alfa = raw_input("Ingrese simbolo del alfabeto: ")
					dirr = raw_input("Ingrese el numero del estado al cual se conecta\ncon el simbolo: ")
					listaestados[numE].data()[alfa] = dirr

				pause()

			elif opc == 3: # Probar palabra
				eA = 0 #Estado actual
				cuenta = 0
				testWord = raw_input("Ingrese la palabra a analizar\n=> ")
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
