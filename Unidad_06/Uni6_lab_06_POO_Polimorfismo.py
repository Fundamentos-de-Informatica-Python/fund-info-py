# UNIDAD 06.D31 - D35

# Programación Orientada a Objetos (POO) 


print('\n\n---[Diapo 31]---------------------')
print('POO - Polimorfismo')

# En la clase Vehiculo, incorporamos el metodo avanzar
# En la clase Auto    , incorporamos el metodo avanzar
# En la clase Bicicleta, incorporamos el metodo avanzar

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
    def avanzar(self):
        print("[Vehiculo      ]: Estoy Avanzando el Vehículo")



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
    def avanzar(self):
        print("[Vehiculo Auto ]: Se debe apretar el acelerador")




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
    def avanzar(self):
        print("[Vehiculo Bici ]: Se debe pedalear")


miAuto = Auto(100, 4, "Chevolet", "Tracker", 1.2, "Naftero")
miBici = Bicicleta(50, 2, "Olmo", "Wish", 26, "Mountain Bike")
miMoto = Vehiculo(250, 2, "Harley davidson", "Low Rider")

print(str(miBici))
print(str(miAuto))
print(str(miMoto))

vehiculos = []
vehiculos.append(miAuto)
vehiculos.append(miBici)
vehiculos.append(miMoto)

for v in vehiculos:
    v.avanzar()



print('\n\n---[Diapo 33]---------------------')
print('POO - Polimorfismo')

vehiculos = []
vehiculos.append(miAuto)
vehiculos.append(miBici)
vehiculos.append(miMoto)

try:
    for v in vehiculos:
        print("Rodado", v.rodado)

except:
    print("Error! ")


    print('\n\n---[Diapo 34]---------------------')


    for v in vehiculos:
        if isinstance(v, Auto):
            print("Motor tipo:", v.motor)
        elif isinstance(v, Bicicleta):
            print("Rodado:", v.rodado)
        else:
            print("Marca:", v.marca)

