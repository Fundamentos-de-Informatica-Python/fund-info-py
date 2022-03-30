# UNIDAD 03.D17 - D21

# INGRESANDO DATOS AL PROGRAMA
print('\n\n---[Diapo 17]--------------------------')
print('Ingresando Datos \n')

data = input()
print('En la variable data tengo guardado el valor: ', data)

print('\n\n---[Diapo 18.a]--------------------------')
print('Ingresando Datos \n')

nombre = input('Por favor, ingrese su nombre: ')

print('Hola', nombre, '!, bienvendo ')
print('Hola ' + nombre + '!, bienvendo ')
print('Hola {n}!, bienvendo '.format(n=nombre))

print('\n\n---[Diapo 18.b]--------------------------')
print('Calcular \n')

numero1 = input('Ingrese al primer número: ')
numero2 = input('Ingrese al segundo número: ')

print('La suma es: ', numero1 + numero2)

print('\n\n---[Diapo 19]--------------------------')
print('Conversión de los Tipos de Datos: \n')

# Entero
texto = '5'
numero = int(texto)

print('El número es ', numero)

# Float
texto = '5'
numero = float(texto)

print('El número es ', numero)

# String
numero = 5
texto = str(numero)

print('El texto es ', texto)

print('\n\n---[Diapo 20]--------------------------')

numero = 5
numero_dec = 5.0
texto = '5'

print('El tipo de dato de "numero"     es: ', type(numero))
print('El tipo de dato de "numero_dec" es: ', type(numero_dec))
print('El tipo de dato de "texto"      es: ', type(texto))

entero = 5
print('El entero convertido a flotante es: ', float(entero))

flotante = 5.0
print('El flotante convertido a entero es: ', int(flotante))

print('\n\n---[Diapo 21.a]--------------------------')
print('Ingresar Números: \n')

texto = input('Ingrese un número: ')
numero = int(texto)

print('El número es: ', numero)

print('\n\n---[Diapo 21.b]--------------------------')
print('Calcular: \n')

numero1 = int(input('Ingrese al primer número: '))
numero2 = int(input('Ingrese al segundo número: '))

suma = numero1 + numero2
print('La suma es: ', suma)
