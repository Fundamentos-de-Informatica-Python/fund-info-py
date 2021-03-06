# UNIDAD 06.D23 - D24

# Programación Orientada a Objetos (POO) 


print('\n\n---[Diapo 23.a]---------------------')
print('POO - Imprimir En String')


class Galletita:
    tamanio = 'Dulce'

mi_galletita = Galletita()
print(str(mi_galletita))



print('\n\n---[Diapo 23.b]---------------------')
print('POO - Imprimir En String')


class Galletita:
    sabor = 'Dulce'
    def __str__(self):
        return 'Galletita de colo {}'.format(self.sabor)

print(str(mi_galletita))





print('\n\n---[Diapo 24]---------------------')
print('POO - Métodos Especiales - Len')


class Galletita:
    tamanio = 26
    def __len__(self):
        return self.tamanio

mi_galletita = Galletita()
print('Tamaño de la gelletita: ', len(mi_galletita))
