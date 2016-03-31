class Estado:
	def __init__(self, transicion, puntero, final):
		self.final = final #True or False
		self.vinculo = []
		
	def addPuntero(self, transicion, puntero):
		self.vinculo.append([tansicion, puntero])
		
class Estado_Inicial(Estado):
	def __init__(self, transicion, puntero, final):
		self.inicial = True
		self.final = final #True or False
		self.vinculo = []
