class Persona:
	def __init__(self, nombre, edad):
		self.nombre = nombre
		self.edad = edad

class Estudiante(Persona):
	def __init__(self, nombre, edad, nivel):
		super().__init__(nombre, edad)
		self.nivel = nivel

e = Estudiante("blncita", 23, 2)
print(e.nombre, e.edad, e.nivel)
