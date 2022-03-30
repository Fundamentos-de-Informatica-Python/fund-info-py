# Bifurcaciones - [Diapo 53]


print('\n\n---[Diapo 53]--------------')
print('Ciclos Iterativos - While \n')

valor = 0
while valor == 0:
    print('Ejecutando el ciclo iterativo')
    valor = 1


print('\n\n---[Diapo 54]--------------')
print('Ciclos Iterativos - While \n')

contador = 0
while contador < 5:
    print('Ejecutando el ciclo iterativo')
    contador += 1


print('\n\n---[Diapo 54]--------------')
print('Ciclos Iterativos - While - else \n')

contador = 0
while contador < 5:
    print('Ejecutando el ciclo iterativo')
    contador += 1
else:
    print('Fin de la iteración')



print('\n\n---[Diapo 55]--------------')
print('Ciclos Iterativos - While - else - break \n')

contador = 0
while contador < 5:
    print('Ejecutando el ciclo iterativo')
    contador += 1
    if contador == 2:
        break
else:
    print('Fin de la iteración')
print('El contadpr vale: ', contador)



print('\n\n---[Diapo 56]--------------')
print('Ciclos Iterativos - While - else - continue \n')

contador = 0
while contador < 5:
    print('\nEjecutando el ciclo iterativo', contador)
    contador += 1
    if contador == 2:
        print("El contador vale 2, se continúa al siguiente ciclo")
        continue
    print('Fin del ciclo iterativo nro: ', contador)
else:
    print('Fin de la iteración')
print('El contadpr vale: ', contador)

