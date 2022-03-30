# UNIDAD 06.D15 - D18

# Programación Orientada a Objetos (POO) 


print('\n\n---[Diapo 15]---------------------')
print('POO - Clases y Objetios en Python')

class Galletita:
    pass

mi_galletita = Galletita()

print('mi_galletita es de typo: ', type(mi_galletita))



print('\n\n---[Diapo 16]---------------------')
print('POO - Atributos de clase')

class Galletita:
    sabor = 'Dulce'
    color = 'Negra'
    chips_chocolate = False

mi_galletita = Galletita()

print('mi_galletita es de sabor: ', mi_galletita.sabor)




print('\n\n---[Diapo 17.a]---------------------')
print('POO - Atributos de clase')

class Galletita:
    sabor = 'Dulce'
    color = 'Negra'
    chips_chocolate = False

mi_galletita = Galletita()
mi_galletita.sabor = 'Salada'

print('mi_galletita es de sabor: ', mi_galletita.sabor)


print('\n\n---[Diapo 17.b]---------------------')
print('POO - Atributos de clase')

class Galletita:
    sabor = 'Dulce'
    color = 'Negra'
    chips_chocolate = False

mi_galletita = Galletita()
mi_galletita.tamanio = 'Mediano'

print('mi_galletita es de sabor: ', mi_galletita.tamanio)



print('\n\n---[Diapo 18]---------------------')
print('POO - Métodos de clase')

class Galletita:
    sabor = 'Dulce'
    color = 'Negra'
    chips_chocolate = False

    def cambiarSabor(self):
        if self.sabor == 'Dulce':
           self.sabor = 'Salado'
        else:
           self.sabor = 'Dulce'

mi_galletita = Galletita()
mi_galletita.cambiarSabor()
print('mi_galletita es de sabor: ', mi_galletita.sabor)

mi_galletita.cambiarSabor()
print('mi_galletita es de sabor: ', mi_galletita.sabor)

mi_galletita.cambiarSabor()
print('mi_galletita es de sabor: ', mi_galletita.sabor)



