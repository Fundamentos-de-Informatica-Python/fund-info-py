# UNIDAD 06.D19 - D21

# Programación Orientada a Objetos (POO) 


print('\n\n---[Diapo 19]---------------------')
print('POO - Constructor')


class Galletita:
    sabor = 'Dulce'
    color = 'Negra'
    chips_chocolate = False

    def __init__(self):
        print('Se acaba de crear una galletita')


mi_galletita = Galletita()



print('\n\n---[Diapo 20.a]---------------------')
print('POO - Constructor')


class Galletita:
    chips_chocolate = False

    def __init__(self, sabor, color):
        self.sabor = sabor
        self.color = color
        print('Nueva galletita de {:7} y color {}'.format(self.sabor, self.color))


mi_galletita1 = Galletita('Dulce', 'Blanca')
mi_galletita1 = Galletita('Salada', 'Marrón')
mi_galletita1 = Galletita('Dulce', 'Verde')



print('\n\n---[Diapo 20.a]---------------------')
print('POO - Constructor - valores default')


class Galletita:
    chips_chocolate = False

    def __init__(self, sabor = 'Dulce', color = 'Marrón'):
        self.sabor = sabor
        self.color = color
        print('Nueva galletita de {:7} y color {}'.format(self.sabor, self.color))


mi_galletita1 = Galletita('Dulce', 'Blanca')
mi_galletita1 = Galletita('Salada', 'Marrón')
mi_galletita1 = Galletita()


print('\n\n---[Diapo 21]---------------------')
print('POO - Constructor y Destructor')


class Galletita:
    chips_chocolate = False

    def __init__(self, sabor = 'Dulce', color = 'Marrón'):
        self.sabor = sabor
        self.color = color
        print('Nueva galletita de {:7} y color {}'.format(self.sabor, self.color))

    def __del__(self):
        print('Se está borrando la galletita de sabor', self.sabor)

mi_galletita1 = Galletita('Dulce', 'Blanca')
del(mi_galletita)

