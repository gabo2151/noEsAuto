# -*- coding: utf-8 -*-
from Tkinter import *

#Autores: Gabriel Galilea, Javier Godoy, Elliot Ide
class Estado:
	def __init__(self, nombre):
		self.nombre = nombre
		self.inicial = False
		self.final = False
		self.indices = {}

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

def estadoInicial():
	if entry1.get() != "": 
		entry1.config(highlightbackground="#d9d9d9")
		entry1.config(highlightcolor="black")
		listaestados.append(Estado(entry1.get()))
		listaestados[0].inicial=True
		button1.configure(state=DISABLED)
		button1.update()
		text1.insert(INSERT,"- El estado inicial es (%s).\n" %(entry1.get()))
	else:
		entry1.config(highlightbackground="red")
		entry1.config(highlightcolor="red")

def creaTransiciones():
	l = entry2.get().split()
	verifica = True 
	if len(listaestados)!= 0 and len(l) == 3:
		entry2.config(highlightbackground="#d9d9d9")
		entry2.config(highlightcolor="black")
		if validaEstado(l[0]):
			c = devuelvePos(l[0])
			if validaTrans(c,l[1]):
				text1.insert(INSERT, "- Ya existe una transicion asociada a el simbolo <%s> para (%s).\n" %(l[1], l[0]))
				verifica = False
			else:
				listaestados[c].indices[l[1]]=l[2]
				text1.insert(INSERT, "- La transicion [%s %s %s] ha sido agregada. \n" %(l[0], l[1], l[2]))
				listatrans.append(l)
				if l[1] not in alfabeto:
					alfabeto.append(l[1])

		else:
			listaestados.append(Estado(l[0]))
			c = devuelvePos(l[0])
			text1.insert(INSERT, "- El estado (%s) ha sido creado.\n" %(l[0]))
			listaestados[c].indices[l[1]]=l[2]
			text1.insert(INSERT, "- La transicion [%s %s %s] ha sido agregada.\n" %(l[0], l[1], l[2]))
			listatrans.append(l)
			if l[1] not in alfabeto:
					alfabeto.append(l[1])

		if  verifica:
			if not validaEstado(l[2]):
				listaestados.append(Estado(l[2]))
				text1.insert(INSERT, "- El estado (%s) ha sido creado.\n" %(l[2]))

		cbutton1.deselect()
		button2.configure(state=DISABLED)
		button2.update()
	else:
		text1.insert(INSERT, "- Verifique si esta respetando la estructura de ingreso, o si aun no ingresa un estado inicial.\n")
		entry2.config(highlightbackground="red")
		entry2.config(highlightcolor="red")

def estadosFinales():
	if entry3.get() != "":
		entry3.config(highlightbackground="#d9d9d9")
		entry3.config(highlightcolor="black")
		l2 = entry3.get().split()
		for i in range(len(l2)):
			if validaEstado(l2[i]):
				c = devuelvePos(l2[i])
				if not listaestados[c].final:
					listaestados[c].final = True
					text1.insert(INSERT, "- (%s) es ahora un estado final.\n" %(l2[i]))
				else:
					listaestados[c].final = False
					text1.insert(INSERT, "- (%s) ya no es un estado final.\n" %(l2[i]))

			else:
				text1.insert(INSERT, "- El estado (%s) no existe. \n" %(l2[i]))
	else:
		text1.insert(INSERT, "- No ha ingresado nada.") 
		entry3.config(highlightbackground="red")
		entry3.config(highlightcolor="red")

def verificaPalabra():
	eA = 0 
	cuenta = 0
	testWord = entry4.get()
	if testWord != "":
		entry4.config(highlightbackground="#d9d9d9")
		entry4.config(highlightcolor="black")
		for key in testWord: 
			if key in listaestados[eA].indices: 
				current = listaestados[eA].indices[key] 
				eA = devuelvePos(current)
				cuenta +=1
			else:
				if key not in alfabeto:
					text1.insert(INSERT,"- La palabra debe estar compuesta en su totalidad por simbolos del alfabeto.\n")
					break
				else:
					text1.insert(INSERT,"- La palabra (%s) no pertenece al lenguaje.\n" %(testWord))
					break
			if cuenta == len(testWord):
				if listaestados[eA].final:
					text1.insert(INSERT,"- La palabra (%s) pertenece al lenguaje.\n" %(testWord))
					break
				else:
					text1.insert(INSERT,"- La palabra (%s) no pertenece al lenguaje.\n" %(testWord))
					break
	else:
		text1.insert(INSERT, "- El ingreso no puede ser el vacio.\n")
		entry4.config(highlightbackground="red")
		entry4.config(highlightcolor="red")

def activar():
    if CheckVar1.get() == 1:
    	button2.configure(state=NORMAL)
    	button2.update()
    elif CheckVar1.get() == 0:
    	button2.configure(state=DISABLED)
    	button2.update()

def limpiar():
	text1.delete('1.0', END)

def hardReset():
	listaestados[:] = []
	alfabeto[:] = []
	listaentradas = [entry1, entry2, entry3, entry4] 
	text1.delete('1.0', END) 
	button1.configure(state=NORMAL)
	cbutton1.deselect() 
	button2.configure(state=DISABLED)
	for i in range (len(listaentradas)): 
		listaentradas[i].delete(0, END)
		if listaentradas[i].cget('highlightbackground') == "red" and listaentradas[i].cget('highlightcolor') == "red":
			listaentradas[i].config(highlightbackground="#d9d9d9")
			listaentradas[i].config(highlightcolor="black")

def mostrarAlf():
	if len(alfabeto)!= 0:
		text1.insert(INSERT, "- El alfabeto actual es %s.\n" %(alfabeto))
	else:
		text1.insert(INSERT, "- Aun no ha agregado transiciones.\n")

def maximumDisplay():
	if len(listaestados)!=0:
		listanom = []
		listafin = []
		for i in range(len(listaestados)):
			listanom.append(listaestados[i].nombre)
			if listaestados[i].final:
				listafin.append(listaestados[i].nombre)

		text1.insert(INSERT, "- Estados: %s.\n" %(listanom))
		text1.insert(INSERT, "- Estado inicial: (%s).\n" %(listaestados[0].nombre))
		text1.insert(INSERT, "- Estados finales: %s.\n" %(listafin))
		text1.insert(INSERT, "- Transiciones: %s.\n" %(listatrans))
		text1.insert(INSERT, "- Alfabeto: %s.\n" %(alfabeto))

	else:
		text1.insert(INSERT, "- Aun no existen datos en el sistema.\n")

if __name__ == "__main__":
	root= Tk()
	root.title("Simulador de AFD")
	root.geometry("515x590") #anchoxalto

	frame1 = Frame(root,width=515, height=590)
	frame1.pack()

	listaestados = []
	alfabeto = []
	listatrans= []
	CheckVar1 = IntVar()

	label1 = Label(frame1, text="Estado inicial")
	label1.place(x=25, y=20)

	entry1 = Entry(frame1, width=7)
	entry1.place(x=125, y=20)

	button1= Button(frame1, text="Definir", command=estadoInicial)
	button1.place(x=195, y=15)
		
	label2 = Label(frame1, text="Transiciones")
	label2.place(x=25, y=55)

	label3 = Label(frame1, text="Ej: q0 a q1")
	label3.place(x=125, y=77)

	entry2 = Entry(frame1,width=20)
	entry2.place(x=125, y=55)

	cbutton1= Checkbutton(frame1, text="Confirmar", variable=CheckVar1, onvalue=1, offvalue=0, command=activar)
	cbutton1.place(x=300, y=55)

	button2 = Button(frame1, state=DISABLED, text="Agregar", command=creaTransiciones)
	button2.place(x=400, y=50)

	label4 = Label(frame1, text="Estados finales")
	label4.place(x=25, y=110)

	entry3 = Entry(frame1, width=25)
	entry3.place(x=125, y=110)

	label5 = Label(frame1, text="Ej: q0 q1 q2 ...")
	label5.place(x=125, y=132)

	button3 = Button(frame1, text="Definir",command=estadosFinales)
	button3.place(x=340, y=105)

	label6 = Label(frame1, text="Palabra")
	label6.place(x=25, y=165)

	entry4 = Entry(frame1, width=25)
	entry4.place(x=125, y=165)

	button4 = Button(frame1, text="Evaluar", command=verificaPalabra)
	button4.place(x=340, y=160)

	label6 = Label(frame1, text="Consola de Procesos")
	label6.place(x=25, y=210)

	scrollbar1 = Scrollbar(frame1)
	scrollbar1.place(x=490, y=375)

	text1 = Text(frame1, width=65, height=20, wrap=WORD, yscrollcommand=scrollbar1.set)
	text1.place(x=25, y=230)

	scrollbar1.config(command=text1.yview)

	button5 = Button(frame1, text="Limpiar Consola", command=limpiar)
	button5.place(x=280, y=545)

	button6 = Button(frame1, text="Reiniciar", command=hardReset)
	button6.place(x=410, y=545)

	button7 = Button(frame1, text="Alfabeto", command=mostrarAlf)
	button7.place(x=420, y=160)

	button8 = Button(frame1, text= "Display", command=maximumDisplay)
	button8.place(x=203,y=545)
	root.mainloop()