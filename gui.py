from Tkinter import *
##interfaz grafica

class Estado:
	def __init__(self, nombre):
		self.nombre = nombre
		self.initGui(nombre)
	def initGui(self, nombre):
		gui = Tk()
		gui.title(nombre)
		gui.geometry("150x200")

if __name__ == "__main__":
	listStates = []
	##interfaz grafica   
	ventana = Tk()
	ventana.title("Simulador de AFD")
	ventana.geometry("400x200") #anchoxalto

	frame1 = Frame(ventana,width=400,height=200) #estaba pensando en tener multiples frames para las etapas del programa
	frame1.pack()

	#var = IntVar()

	label1 = Label(frame1, text="Ingrese simbolo que represente a sus estados")
	label1.place(x=15,y=15)

	entrada = Entry(frame1,width=4)
	entrada.place(x=300,y=15)

	spinbox1 = Spinbox(frame1, from_=1, to=10)
	spinbox1.place(x=150,y=45)

	botonevalua = Button(ventana, text="Crear Estados", command=lambda:createState())
	botonevalua.place(x=150,y=75)
	def createState():
		print "holi"
		name = "q%s" % len(listStates)
		print name
		listStates.append( Estado(name) )
		print "holu"

	ventana.mainloop()