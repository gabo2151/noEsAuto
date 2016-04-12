from Tkinter import *

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


#funciones basicas
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


#nuevas funciones

def estadoInicial(): #siempre la entrada sera considerada como un string, no puedo restringuir esto
	listaestados.append(Estado(entry1.get()))
	listaestados[0].inicial=True
	text1.insert(INSERT,"Su estado inicial es: "+ entry1.get()+"\n")

	#entry1.configure(bg="red") #poner el marco rojo
	#entry1.update()	

def creaTransiciones():
	l = entry2.get().split()
	if validaEstado(l[0]): #si el estado existe, solo agrego su transicion al diccionario indices
		text1.insert(INSERT, "El estado " + l[0]+ " ya existe \n")
		c = devuelvePos(l[0])
		if validaTrans(c,l[1]):
			text1.insert(INSERT, "Ya existe una transicion asociada a este simbolo\n")
		else:
			listaestados[c].indices[l[1]]=l[2]

	else: #si el estado no existe, lo creo, y luego agrego la transicion
		listaestados.append(Estado(l[0]))
		c = devuelvePos(l[0])
		listaestados[c].indices[l[1]]=l[2]

		#segundo estado en la transicion
		if validaEstado(l[2]):
			text1.insert(INSERT, "El estado " + l[2] + " ya existe \n")

		else:
			listaestados.append(Estado(l[2]))
	cbutton1.deselect()
	button2.configure(state=DISABLED)
	button2.update()


def estadosFinales():
	print "aun valgo verga man"
	"""l2 = entry3.get().split() #como verifico a cada estado ahorrando codigo xd HELP
	largol2 = len(l2)
	count = 0"""

def verificaPalabra():
	eA = 0 #Estado actual
	cuenta = 0
	testWord = entry4.get()
	for key in testWord:
		text1.insert(INSERT,key)
		if key in listaestados[eA].indices:
			eA = int( listaestados[eA].indices[key][1] )
			cuenta +=1
			text1.insert(INSERT,eA)
		else:
			text1.insert(INSERT,"La palabra no pertenece a este lenguaje \n")
			break

		if cuenta == len(testWord):
			if listaestados[eA].final:
				text1.insert(INSERT, "La palabra pertenece al lenguaje \n")
				break
			else:
				text1.insert(INSERT,"La palabra no pertenece a este lenguaje \n")
				break




#funciones interfaz grafica

def activar(): #funcion asociada a los check button
    if CheckVar1.get() == 1:
    	button2.configure(state=NORMAL)
    	button2.update()
    elif CheckVar1.get() == 0:
    	button2.configure(state=DISABLED)
    	button2.update()

def limpiar():
	text1.delete('2.0', END) #2.0 desde la segunda fila en adelante
	text1.insert(INSERT,"\n") #arreglin


#variables
listaestados = [] #lista de objetos tipo estado
#l = []
#c = 0

#interfaz grafica   
root= Tk()
root.title("Simulador de AFD")
root.geometry("500x600") #anchoxalto

frame1 = Frame(root,width=500,height=600) #estaba pensando en tener multiples frames para las etapas del programa
frame1.pack()

CheckVar1 = IntVar()

label1 = Label(frame1, text="Estado inicial")
label1.place(x=15, y=15)

entry1 = Entry(frame1,width=6)
entry1.place(x=125, y=15)

button1= Button(frame1,text="Definir", command=estadoInicial)
button1.place(x=190, y=10)


label2 = Label(frame1, text="Transiciones")
label2.place(x=15, y=45)

label3 = Label(frame1, text="Ej: q0 a q1")
label3.place(x=125, y=70)

entry2 = Entry(frame1,width=20)
entry2.place(x=125, y=45)

cbutton1= Checkbutton(frame1,text="Confirmar", variable=CheckVar1, onvalue=1, offvalue=0, command=activar)
cbutton1.place(x=300, y=40)

button2 = Button(frame1, state=DISABLED, text="Agregar", command=creaTransiciones)
button2.place(x=400, y=40)

label3 = Label(frame1, text="Estados finales")
label3.place(x=15, y=115)

label4 = Label(frame1, text="Ej: q0 q1 q2 ...")
label4.place(x=125, y=140)

entry3 = Entry(frame1, width=20)
entry3.place(x=125, y=115)

button3 = Button(frame1, text="Definir",command=estadosFinales)
button3.place(x=300, y=110)

label5 = Label(frame1, text="Palabra")
label5.place(x=15, y=175)

entry4 = Entry(frame1, width=20)
entry4.place(x=125, y=175)

button4 = Button(frame1, text="Evaluar")
button4.place(x=300, y=170)


text1 = Text(frame1,width=65, height=20, wrap=WORD)
text1.place(x=15, y=225)
text1.insert(INSERT, "Consola de Procesos" +"\n")

button5 = Button(frame1, text="Limpiar Consola",command=limpiar)
button5.place(x=325, y=545)

root.mainloop()

