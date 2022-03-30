# UNIDAD 03.D23 - D26

# Tomando parámetros desde la terminal


print('\n\n---[Diapo 24]--------------------------')

import sys

print('Los argumentos son: ', sys.argv)


print('\n\n---[Diapo 25]--------------------------')

import sys

print('Sumar dos números: ')

numero1 = int(sys.argv[1])
numero2 = int(sys.argv[2])

print('La suma es: ', numero1 + numero2)
