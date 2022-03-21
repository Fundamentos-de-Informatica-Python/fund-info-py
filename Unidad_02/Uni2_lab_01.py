# UNIDAD 02.D03 - D08

#INGRESANDO DATOS AL PROGRAMA
print('\n-----------------------------')
print('Ingresando Datos \n')

data = input()
print('En la variable data tengo guardado el valor: ', data)



print('\n-----------------------------')
print('Ingresando Datos \n')

nombre = input('Por favor, ingrese su nombre: ')

print('Hola', nombre  ,'!, bienvendo ')
print('Hola ' + nombre + '!, bienvendo ')
print('Hola {n}!, bienvendo '.format(n=nombre))


print('\n-----------------------------')
print('Calcular \n')

numero1 = input('Ingrese al primer número: ')
numero2 = input('Ingrese al segundo número: ')

print('La suma es: ', numero1 + numero2)


print('\n-----------------------------')
print('Conversión de los Tipos de Datos: \n')

# Entero
texto = '5'
numero = int(texto)

print('El número es ' , numero)

# Float
texto = '5'
numero = float(texto)

print('El número es ' , numero)

# String
numero = 5
texto = str(numero)

print('El texto es ' , texto)


print('\n-----------------------------')
print('Identificar al Tipo de Datos: \n')

numero = 5
numero_dec = 5.0
texto = '5'

print('El tipo de dato de "numero"     es: ', type(numero))
print('El tipo de dato de "numero_dec" es: ', type(numero_dec))
print('El tipo de dato de "texto"      es: ', type(texto))

print('\n-----------------------------')
print('Ingresar Números: \n')

numero1 = int(input('Ingrese un número: '))

print('El número es: ', numero1)

print('\n-----------------------------')
print('Calcular: \n')

numero1 = int(input('Ingrese al primer número: '))
numero2 = int(input('Ingrese al segundo número: '))

print('La suma es: ', numero1 + numero2)
