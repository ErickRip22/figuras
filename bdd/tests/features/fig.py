import math

class Figuras():

	def __init__(self):
		self.area = 0

	def get_area(self):
		return self.area

	def calcular_area_circulo(self, radio):
		self.area = math.pow(math.pi,2) * radio

	def calcular_area_cuadrado(self, lado):
		self.area = math.pow(lado, 2)

	def calcular_area_rectangulo(self,ancho, largo):
		self.area = ancho*largo

	def calcular_area_trapecio(self, altura, baseA, baseB):
		self.area = float(altura) * (baseA + baseB) / 2.0