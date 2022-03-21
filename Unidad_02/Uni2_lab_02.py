# UNIDAD 02.D09 - D12

#Tomando parámetros desde la terminal

import sys

print('\n-----------------------------')
print('Los argumentos son: ', sys.argv)

print('\n-----------------------------')
print('Sumar dos números: ')

numero1 = int(sys.argv[1])
numero2 = int(sys.argv[2])

print('La suma es: ', numero1 + numero2)