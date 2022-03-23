# UNIDAD 03.D09 - D12

# Tomando parámetros desde la terminal


print('\n\n---[Diapo 10]--------------------------')

import sys

print('Los argumentos son: ', sys.argv)


print('\n\n---[Diapo 11]--------------------------')

import sys

print('Sumar dos números: ')

numero1 = int(sys.argv[1])
numero2 = int(sys.argv[2])

print('La suma es: ', numero1 + numero2)
