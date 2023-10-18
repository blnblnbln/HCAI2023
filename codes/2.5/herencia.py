class Animal:
	def __init__(self, nombre):
		self.nombre = nombre
	def hablar(self):
		pass

class Perro(Animal):
	def hablar(self):
		return "Guau!"

class Gato(Animal):
	def hablar(self):
		return "Miau!"

perro=Perro("Cojo")
gato=Gato("Tom")
print(perro.hablar())
print(gato.hablar())

