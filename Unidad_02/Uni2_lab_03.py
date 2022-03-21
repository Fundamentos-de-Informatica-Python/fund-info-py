# UNIDAD 02.D09 - D12

#Formateando los datos de salida

print('\n-----------------------------')
# Formateos

nombre = 'Jorge'
apellido = 'Rodriguez'
cadena = 'Mi nombre es {} y mi apellido es {}'.format(nombre, apellido)

print('Cadena: ', cadena)


print('\n-----------------------------')
# Posicional
nombre = 'Jorge'
apellido = 'Rodriguez'
print('Mi nombre es {1} y mi apellido es {0}'.format(nombre, apellido))



print('\n-----------------------------')
# Uso de nombres

nombre = 'Jorge'
apellido = 'Rodriguez'
print('Mi nombre es {n} y mi apellido es {m}'.format(n=nombre, m=apellido))


print('\n-----------------------------')
# Uso de nombres

print('Mi nombre es {nombre} y mi apellido es {apellido}'.format(nombre='Jorge', apellido='Rodriguez'))


print('\n-----------------------------')
print('Alinenando Textos: \n')

# Derecha
c = '{:>30}'.format('Hola a Todos')
print(c)

# Izquierda
c = '{:30}'.format('Hola a Todos') + 'Fin.'
print(c)

# Centro
c = '{:^30}'.format('Hola a Todos') + 'Fin.'
print(c)

# Truncado
c = '{:.3}'.format('Hola a Todos')
print(c)


print('\n-----------------------------')
print('Alinenando Números: \n')

print('{:>4}'.format(10))
print('{:>4}'.format(100))
print('{:>4}'.format(1000))


print('\n Rellenando ceros \n')

print('{:04}'.format(10))
print('{:04}'.format(100))
print('{:04}'.format(1000))

print('\n Truncar Flotantes \n')

print('{:.2f}'.format(3.141592))
print('{:7.2f}'.format(3.141592))
print('{:07.2f}'.format(3.141592))
