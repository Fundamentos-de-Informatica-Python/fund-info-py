# UNIDAD 03.D06

# Tuplas

print('\n\n---[Diapo 06]---------------------')

frutas = ('manzana', 'mandarina', 'naranja')

print('Las mandarina están en la posición:', frutas.index('mandarina'))

# print('Las peras están en la posición:', frutas.index('peras'))      # Error!!


frutas = ('manzana', 'mandarina', 'naranja', 'mandarina')

print('Las mandarinas están', frutas.count('mandarina'), 'veces')
print('Las mandarinas están', frutas.count('peras'), 'veces')


print('Las mandarina están en la posición:', frutas.index('mandarina'))

print('\n\n---[Diapo 06 - consulta]---------------------')

frutas = ('manzana', 'no_es_mandarina', 'naranja', 'mandarina')

print('Las mandarinas están', frutas.count('mandarina'), 'veces')
print('Las mandarinas están', frutas.count('peras'), 'veces')


print('Las mandarina están en la posición:', frutas.index('mandarina'))

