"""La tarea consiste en diseniar y construir un programa computacional capaz de
simular cualquier AFD"""
#La entrada al programa consiste en: estado inicial, estados finales
#transiciones del AFD, palabra de entrada

#La salida un mensaje indicando si pertenece o no al lenguaje

#El programa debe poder analizar muchas palabras de entrada
#Debe ser autoexplicativo
def menuConsola():
	print "==MENU========================"
	print "[1] Continuar con el programa"
	print "[0] Salir"

class Estado:
	def __init__(self, nombre):
		self.nombre = nombre
		self.tipo = "regular"
		self.indices = {}

	def addIndice(self, caracter, direccion):
		# La direccion debiese de ser el numero del indice
		self.indices(caracter) = direccion


if __name__ == "__main__":
	print "-----------Teoria de Automatas--------------\nSimulador de Automatas Finitos Deterministas\nAutores: Elliot Ide, Gabriel Galilea, Javier Godoy"
	print "*********************************************"

	#Seleccion consola o GUI
	selGUI = 2
	while True:
		selGUI = raw_input("Iniciar en consola [0] o iniciar GUI [1]: ")
		if selGUI == "0" or selGUI == "1":
			selGUI = int(selGUI)
			break

	# Inicio de modo consola
	if selGUI == 0:
		while True: #Loop infinito para ejecutar el programa sin terminarlo
			menuConsola()
			opc = input("Elija una opcion: ")

			if opc == 0:
				break #Termina el while

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

			talvez = raw_input("Desea que el estado "+ listaestados[0].nombre+" sea el estado inicial (si o no): ")
			while talvez !="si" and talvez != "no":
				talvez = raw_input("Desea que el estado "+ listaestados[0].nombre+" sea el estado inicial (si o no): ")
			
			if talvez == "si":
				listaestados[0].tipo = "inicial"
				print listaestados[0].tipo

			else:
				for i in range(n):
					listanombres.append(listaestados[i].nombre)
				ini = raw_input("Ingrese nombre estado inicial: ")
				while ini not in listanombres:
					ini = raw_input("Ingrese nombre estado inicial: ")

				pos = encuentraPos(listanombres,ini)
				print pos

				listaestados[pos].tipo ="inicial"
				print listaestados[pos].tipo




	# Inicio del modo GUI
	elif selGUI == 1:
		print "Iniciando GUI..."

#interfaz grafica
