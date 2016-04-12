from Tkinter import *
##interfaz grafica

class Estado:
	def __init__(self, nombre):
		self.nombre = nombre


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


    
##interfaz grafica   
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

button1= Button(frame1,text="Definir")
button1.place(x=190, y=10)


label2 = Label(frame1, text="Transiciones")
label2.place(x=15, y=45)

label3 = Label(frame1, text="Ej: q0 a q1")
label3.place(x=125, y=70)

entry2 = Entry(frame1,width=20)
entry2.place(x=125, y=45)

cbutton1= Checkbutton(frame1,text="Confirmar", variable=CheckVar1, onvalue=1, offvalue=0, command=activar)
cbutton1.place(x=300, y=40)

button2 = Button(frame1, state=DISABLED, text="Definir")
button2.place(x=400, y=40)

label3 = Label(frame1, text="Estados finales")
label3.place(x=15, y=115)

label4 = Label(frame1, text="Ej: q0 q1 q2 ...")
label4.place(x=125, y=140)

entry3 = Entry(frame1, width=20)
entry3.place(x=125, y=115)

button3 = Button(frame1, text="Definir")
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

