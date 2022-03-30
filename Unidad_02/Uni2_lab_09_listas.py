# Listas - Funciones Sobre Listas [Diapo 34 - Diapo 35]

print('\n\n---[Diapo 34]--------------')
print('Funciones Sobre listas - Incorporar sublista\n')


lista = [5, 10, 20, 30]
print('La lista inicial es:  ', lista)

lista = lista + [35, 40]
print('Y luego del cambio es: ', lista)

print('\n\n---[Diapo 34]--------------')
print('Funciones Sobre listas - Incorporar elemento\n')

lista = [5, 10, 20, 30]
print('La lista inicial es:  ', lista)

lista.append(35)
print('Y luego del cambio es: ', lista)


print('\n\n---[Diapo 35]--------------')
print('Funciones Sobre listas - Elimino sublista\n')

lista = [5, 10, 20, 30]
print('La lista inicial es:  ', lista)

lista[1:3] = []
print('Y luego del cambio es: ', lista)


print('\n\n---[Diapo 35]--------------')
print('Eliminino  solo un elemento \n')

lista = [5, 10, 20, 30]
print('La lista inicial es:  ', lista)

lista[1:2] = []
print('Y luego del cambio es: ', lista)


print('\n\n---[Diapo 35]--------------')
print('Eliminino  el último elemento \n')
lista = [5, 10, 20, 30]
print('La lista inicial es:  ', lista)

lista.pop()
print('Y luego del cambio es: ', lista)

lista[-1:] = []
print('Y luego del cambio es: ', lista)
