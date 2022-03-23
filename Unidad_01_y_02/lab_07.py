# UNIDAD 01.D25 - D27

print('\n-----------------------------')
print('Funciones sobre cadenas \n')

saludo = 'Hola'
nombre = 'Juan'

saludar = saludo +  ' ' + nombre + "!"
print(saludar)

'''
Funcion longitud
'''
print('\n-----------------------------')
print('Longitud sobre cadenas \n')

nombre = 'Juan Carlos Rodriguez'
longitud = len(nombre)

print('Mi nombre tiene', longitud, 'caracteres')



'''
Indices en un string
'''
print('\n-----------------------------')
print('Indices sobre cadenas \n')

var = 'Hola a tod@s!'
print('La primera letra es ', var[0])
print('La segunda letra es ', var[1])
print('La tercera letra es ', var[2])


print('La última letra es    ', var[-1])
print('La penúltima letra es ', var[-2])
print('Y la antepenúltima es ', var[-3])




'''
Slicing
'''
print('\n-----------------------------')
print('Slicing sobre cadenas \n')

var = 'Hola a tod@s!'
print('Las primera  dos letra es ', var[0:2])
print('Las siguientes cuatro     ', var[2:6])
print('Desde la tercera hasta la anteúltima      ', var[2:-1])
print('Desde la antepnultima hasta la anteúltima ', var[-3:-1])

print('Los dos primeeros     ', var[:2])
print('Y las últimas cuatro  ', var[-4:])

