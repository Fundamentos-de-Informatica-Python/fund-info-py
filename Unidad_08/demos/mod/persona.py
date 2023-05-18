class Persona:
    nombre = ''
    edad = 0

    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def __str__(self):
        return 'Persona: ' + self.nombre + ' edad: ' + str(self.edad)