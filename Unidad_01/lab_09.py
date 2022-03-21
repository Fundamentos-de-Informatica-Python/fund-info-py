# Listas - Funciones Sobre Listas [Diapo 32 - Diapo 33]

print('\n-----------------------------')
print('Funciones Sobre listas [Diapo 32] - Incorporar sublista\n')


lista = [5, 10, 20, 30]
print('La lista inicial es:  ', lista)

lista = lista + [35, 40]
print('Y luego del cambio es: ', lista)

print('\n-----------------------------')
print('Funciones Sobre listas [Diapo 32] - Incorporar elemento\n')

lista = [5, 10, 20, 30]
print('La lista inicial es:  ', lista)

lista.append(35)
print('Y luego del cambio es: ', lista)


print('\n-----------------------------')
print('Funciones Sobre listas [Diapo 33] - Elimino sublista\n')

lista = [5, 10, 20, 30]
print('La lista inicial es:  ', lista)

lista[1:3] = []
print('Y luego del cambio es: ', lista)


print('\n-----------------------------')
print('Eliminino  solo un elemento [Diapo 33]\n')

lista = [5, 10, 20, 30]
print('La lista inicial es:  ', lista)

lista[1:2] = []
print('Y luego del cambio es: ', lista)


print('\n-----------------------------')
print('Eliminino  el último elemento [Diapo 33]\n')
lista = [5, 10, 20, 30]
print('La lista inicial es:  ', lista)

lista.pop()
print('Y luego del cambio es: ', lista)

lista[-1:] = []
print('Y luego del cambio es: ', lista)
