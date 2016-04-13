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


#Nuevas funciones (cuando se incluyo gui estas surgieron por necesidad)

def estadoInicial():
	if entry1.get() != "": #si la entrada es distinta de vacio, ajusto los colores a los por defecto y creo el estado inicial
		entry1.config(highlightbackground="#d9d9d9")
		entry1.config(highlightcolor="black")
		listaestados.append(Estado(entry1.get()))
		listaestados[0].inicial=True
		text1.insert(INSERT,"- El estado inicial es: "+ entry1.get()+".\n")
	else: #si no, el borde se vuelve rojo cuando esta enfocado y cuando no en la entrada
		entry1.config(highlightbackground="red")
		entry1.config(highlightcolor="red")



def creaTransiciones():
	l = entry2.get().split()
	verifica = True
	if len(listaestados)!= 0 and len(l) == 3: #solo si existen estados dentro de listaestados y si el largo de mi lista es 3 creare transiciones
		entry2.config(highlightbackground="#d9d9d9") #con widget.cget('highlightbackground') consegui este valor ty internet
		entry2.config(highlightcolor="black")
		text1.insert(INSERT, "- Verifique que ingreso estado inicial, o si no esta respetando la estructura de ingreso. \n")
		if validaEstado(l[0]): #si el estado existe, solo agrego su transicion al diccionario indices
			c = devuelvePos(l[0])
			if validaTrans(c,l[1]):#si existe una transicion con dicho simbolo para el primer estado
				text1.insert(INSERT, "- Ya existe una transicion asociada a el simbolo ("+ l[1] +") para " + l[0] + ".\n")
				verifica = False #con esto me aseguro de no crear el segundo estado, donde ya existe la transicion con ese simbolo
			else:
				listaestados[c].indices[l[1]]=l[2]
				text1.insert(INSERT, "- La transicion (" + l[0] + " " + l[1] + " " + l[2] + ") ha sido agregada. \n")

		else: #si el estado no existe, lo creo, y luego agrego la transicion
			listaestados.append(Estado(l[0]))
			c = devuelvePos(l[0])
			text1.insert(INSERT, "- El estado " + l[0] + " ha sido creado.\n")
			listaestados[c].indices[l[1]]=l[2]
			text1.insert(INSERT, "- La transicion (" + l[0] + " " + l[1] + " " + l[2] + ") ha sido agregada. \n")

		#segundo estado en la transicion
		if  verifica: #si la transicion se pudo agregar (porque no existia)
			if not validaEstado(l[2]): #si el estado no existe, lo creo, y si existe no hago nada
				listaestados.append(Estado(l[2]))
				text1.insert(INSERT, "- El estado " + l[2] + " ha sido creado.\n")

		cbutton1.deselect()
		button2.configure(state=DISABLED)
		button2.update()
	else:
		entry2.config(highlightbackground="red") #siempre que sea != de 3 el largo de la lista, el borde contenedor sera rojo
		entry2.config(highlightcolor="red")


#ya vali verga man
"""def estadosFinales():
	if entry3.get() != "":
		entry3.config(highlightbackground="#d9d9d9")
		entry3.config(highlightcolor="black")
		l2 = entry3.get().split()
		for i in l2:
			for j in range(len(listaestados)):
				if listaestados[j].nombre == i:
					listaestados[j].final = True
					ttx = "- %s es ahora un estado final.\n" % listaestados[j].nombre
					text1.insert(INSERT,ttx)
					break
	else:
		entry3.config(highlightbackground="red")
		entry3.config(highlightcolor="red")"""


def estadosFinales():# ave fenix
	if entry3.get() != "":
		entry3.config(highlightbackground="#d9d9d9")
		entry3.config(highlightcolor="black")
		l2 = entry3.get().split()
		for i in range(len(l2)):
			if validaEstado(l2[i]):#si el estado se encuentra dentro de la listaestados
				c = devuelvePos(l2[i]) #ubico su posicion y lo vuelvo final
				listaestados[c].final = True
				text1.insert(INSERT,"- " + listaestados[i].nombre + " es ahora un estado final.")
			else:
				text1.insert(INSERT, "El estado (" + l2[i] + ") no existe.\n")
	else:
		entry3.config(highlightbackground="red")
		entry3.config(highlightcolor="red")



def verificaPalabra():
	eA = 0 #Estado actual
	cuenta = 0
	testWord = entry4.get()
	if testWord != "":
		entry4.config(highlightbackground="#d9d9d9")
		entry4.config(highlightcolor="black")
		for key in testWord:
			#text1.insert(INSERT,key)
			if key in listaestados[eA].indices:
				current = listaestados[eA].indices[key]
				for i in range( len( listaestados ) ):
					if current == listaestados[i].nombre:
						eA = i
						break
				cuenta +=1
				#text1.insert(INSERT,eA)
			else:
				text1.insert(INSERT,"- La palabra (" + testWord + ")no pertenece a este lenguaje.\n")
				break
			if cuenta == len(testWord):
				if listaestados[eA].final:
					text1.insert(INSERT, "- La palabra (" + testWord + ") pertenece al lenguaje.\n")
					break
				else:
					text1.insert(INSERT,"- La palabra (" + testWord + ") no pertenece a este lenguaje.\n")
					break
	else:
		entry4.config(highlightbackground="red")
		entry4.config(highlightcolor="red")


#Funciones interfaz grafica

def activar(): #funcion asociada al check button
    if CheckVar1.get() == 1:
    	button2.configure(state=NORMAL)
    	button2.update()
    elif CheckVar1.get() == 0:
    	button2.configure(state=DISABLED)
    	button2.update()

def limpiar():
	text1.delete('1.0', END) #primera fila al final
	text1.insert(INSERT,"\n") #arreglin

def hardReset():#esta funcion se encarga de volver todo a su valor original
	listaestados[:] = [] #elimino de mi lista estados todos los estados
	text1.delete('1.0', END) #borro los datos de la consola
	cbutton1.deselect() #en caso de que el cbutton este seleccionado, lo deselecciono
	button2.configure(state=DISABLED)#y ademas dejo al boton asociado desactivado
	for i in range (len(listaentradas)): #decidi hacer una lista de objetos tipo entry para manipularlos mas facilmente a la hora de reiniciar el programa
		listaentradas[i].delete(0, END) #borro todos los datos de todas las entry, y si estan rojos a sus valores originales
		if listaentradas[i].cget('highlightbackground') == "red" and listaentradas[i].cget('highlightcolor') == "red":
			listaentradas[i].config(highlightbackground="#d9d9d9")
			listaentradas[i].config(highlightcolor="black")


#Variables
listaestados = [] #lista de objetos tipo estado
listaentradas = [] #lista de objetos tipo entry

#Interfaz Grafica  
root= Tk()
root.title("Simulador de AFD")
root.geometry("510x580") #anchoxalto


frame1 = Frame(root,width=510,height=575)
frame1.pack()

CheckVar1 = IntVar()

label1 = Label(frame1, text="Estado inicial")
label1.place(x=25, y=20)

entry1 = Entry(frame1,width=7)
entry1.place(x=125, y=20)
listaentradas.append(entry1)

button1= Button(frame1,text="Definir", command=estadoInicial)
button1.place(x=195, y=15)
	
label2 = Label(frame1, text="Transiciones")
label2.place(x=25, y=55)

label3 = Label(frame1, text="Ej: q0 a q1")
label3.place(x=125, y=77)

entry2 = Entry(frame1,width=20)
entry2.place(x=125, y=55)
listaentradas.append(entry2)

cbutton1= Checkbutton(frame1,text="Confirmar", variable=CheckVar1, onvalue=1, offvalue=0, command=activar)
cbutton1.place(x=300, y=55)

button2 = Button(frame1, state=DISABLED, text="Agregar", command=creaTransiciones)
button2.place(x=400, y=50)

label4 = Label(frame1, text="Estados finales")
label4.place(x=25, y=110)

entry3 = Entry(frame1, width=25)
entry3.place(x=125, y=110)
listaentradas.append(entry3)

label5 = Label(frame1, text="Ej: q0 q1 q2 ...")
label5.place(x=125, y=132)

button3 = Button(frame1, text="Definir",command=estadosFinales)
button3.place(x=340, y=105)

label6 = Label(frame1, text="Palabra")
label6.place(x=25, y=165)

entry4 = Entry(frame1, width=25)
entry4.place(x=125, y=165)
listaentradas.append(entry4)

button4 = Button(frame1, text="Evaluar", command=verificaPalabra)
button4.place(x=340, y=160)

label6 = Label(frame1, text="Consola de Procesos")
label6.place(x=25, y=210)

text1 = Text(frame1,width=65, height=20, wrap=WORD)
text1.place(x=25, y=230)

button5 = Button(frame1, text="Limpiar Consola",command=limpiar)
button5.place(x=280, y=545)

button6 = Button(frame1, text="Reiniciar",command=hardReset)
button6.place(x=410, y=545)

root.mainloop()

