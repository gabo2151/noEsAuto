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

	if selGUI == 0:
		while True:
			menuConsola()
			opc = input("Elija una opcion: ")

			if opc == 0:
				break

			#variables
			listaestados = [] #lista de objetos tipo estado


			n = input("Ingrese numero de estados (Debe ser mayor a 0): ")
			while n<=0:
				n=input("Ingrese numero de estados (Debe ser mayor a 0): ")


			x = raw_input("Ingrese simbolo de largo 1 que represente a todos sus estados (Ej: q => q0, q1, ..., qn): ")
			while(len(x)!=1):
				x = raw_input("Ingrese simbolo de largo 1 que represente a todos sus estados (Ej: q => q0, q1, ..., qn): ")

			for i in range(n):
				listaestados.append(Estado(x+str(i)))

			#demostracion
			for i in range(n):
				print listaestados[i].nombre

	elif selGUI == 1:
		print "Iniciando GUI..."

#interfaz grafica