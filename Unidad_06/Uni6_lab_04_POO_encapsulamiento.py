# UNIDAD 06.D25 - D26

# Programación Orientada a Objetos (POO) 


print('\n\n---[Diapo 25.a]---------------------')
print('POO - Encapsilamiento')


class Galletita:
    __metodoProductivo = 'Por Lotes'

mi_galletita = Galletita()
print(mi_galletita.__metodoProductivo)     ## Error: Cancela por ser privado



print('\n\n---[Diapo 25.b]---------------------')
print('POO - Encapsilamiento')


class Galletita:
    __metodoProductivo = 'Por Lotes'
    def __obtenerMetodoProductiovo(self):
        return self.__metodoProductivo

mi_galletita = Galletita()
print(mi_galletita.__obtenerMetodoProductiovo())     ## Error: Cancela por ser privado





print('\n\n---[Diapo 26]---------------------')
print('POO - Encapsilamiento Ok')


class Galletita:
    __metodoProductivo = 'Por Lotes'
    def obtenerMetodoProductiovo(self):
        return self.__metodoProductivo

mi_galletita = Galletita()
print(mi_galletita.obtenerMetodoProductiovo())     ## Ok el encapsulamiento