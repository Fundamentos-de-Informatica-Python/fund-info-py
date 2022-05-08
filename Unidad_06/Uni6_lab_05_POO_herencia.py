# UNIDAD 06.D27 - D30

# Programación Orientada a Objetos (POO) 


print('\n\n---[Diapo 27]---------------------')
print('POO - Herencia')


class Vehiculo:
    def __init__(self, velMaxima, nroRuedas, marca, modelo):
        self.velMaxima = velMaxima
        self.nroRuedas = nroRuedas
        self.marca = marca
        self.modelo = modelo
    def __str__(self):
        return '''
            vehiculo {:10} {:10}, de {:1} ruedas y que llega a una
            velocidad máxima de {:>3} km/h 
        '''.format(self.marca, self.modelo, self.nroRuedas, self.velMaxima)

miVehiculo1 = Vehiculo(100, 4, "Chevolet", "Tracker")
miVehiculo2 = Vehiculo(50, 2, "Olmo", "Wish")

print(str(miVehiculo1))
print(str(miVehiculo2))


print('\n\n---[Diapo 28]---------------------')
print('POO - Herencia')

class Auto(Vehiculo):
    def __init__(self, velMaxima, nroRuedas, marca, modelo,
                 cilinrada, motor):
        super().__init__(velMaxima, nroRuedas, marca, modelo)
        self.cilindrada = cilinrada
        self.motor = motor
    def __str__(self):
        agergo = '''
            con una cilindrada de {} y motor de {}.
        '''.format(self.cilindrada, self.motor)
        return super().__str__() + agergo


miAuto = Auto(100, 4, "Chevolet", "Tracker", 1.2, "Naftero")
print(str(miAuto))


print('\n\n---[Diapo 30]---------------------')
print('POO - Herencia')

class Bicicleta(Vehiculo):
    def __init__(self, velMaxima, nroRuedas, marca, modelo,
                 rodado, tipo):
        super().__init__(velMaxima, nroRuedas, marca, modelo)
        self.rodado = rodado
        self.tipo = tipo
    def __str__(self):
        agergo = '''
            es una bici rodado {} y de tipo {}.
        '''.format(self.rodado, self.tipo)
        return super().__str__() + agergo


miBici = Bicicleta(50, 2, "Olmo", "Wish", 26, "Mountain Bike")
print(str(miBici))



