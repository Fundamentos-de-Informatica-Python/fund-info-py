# Bifurcaciones - [Diapo 51]


print('\n-----------------------------')
print('Ciclos Iterativos [Diapo 51] - While \n')

valor = 0
while valor == 0:
    print('Ejecutando el ciclo iterativo')
    valor = 1


print('\n-----------------------------')
print('Ciclos Iterativos [Diapo 52] - While \n')

contador = 0
while contador < 5:
    print('Ejecutando el ciclo iterativo')
    contador += 1


print('\n-----------------------------')
print('Ciclos Iterativos [Diapo 52] - While - else \n')

contador = 0
while contador < 5:
    print('Ejecutando el ciclo iterativo')
    contador += 1
else:
    print('Fin de la iteración')



print('\n-----------------------------')
print('Ciclos Iterativos [Diapo 53] - While - else - break \n')

contador = 0
while contador < 5:
    print('Ejecutando el ciclo iterativo')
    contador += 1
    if contador == 2:
        break
else:
    print('Fin de la iteración')
print('El contadpr vale: ', contador)



print('\n-----------------------------')
print('Ciclos Iterativos [Diapo 54] - While - else - continue \n')

contador = 0
while contador < 5:
    print('\nEjecutando el ciclo iterativo', contador)
    contador += 1
    if contador == 2:
        print("El contador vale 2, se continúa al siguiente ciclo")
    print('Fin del ciclo iterativo nro: ', contador)
else:
    print('Fin de la iteración')
print('El contadpr vale: ', contador)

