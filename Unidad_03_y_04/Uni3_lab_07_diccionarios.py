# UNIDAD 03.D25 - D28

# Diccionarios

print('\n\n---[Diapo 25]---------------------')
print('Diccionarios:')

diccio = {
    'naranja': 'orange',
    'manzana': 'apple',
    'pera': 'pear'
}

print('Diccionario', diccio)
print('Manzana en inglés se dice: ', diccio['manzana'])

print('\nCon claves numéricas: ')
diccio = {
    10: 'diez',
    5: 'cinco',
    1: 'uno'
}

print('Diccionario:', diccio)
print('El valor de la clave 1 es:', diccio[1])


print('\n\n---[Diapo 26.a]---------------------')
print('Los diccionarios son mutables:')

diccio = {
    'naranja': 'orange',
    'manzana': 'apple',
    'pera': 'pear'
}

print('Manzana en inglés se dice: ', diccio['manzana'])

diccio['manzana'] = 'banana'
print('Manzana en inglés ... ahora se dice: ', diccio['manzana'])


print('\n\n---[Diapo 26.b]---------------------')
print('Agregar y eliminar elementos a los diccionarios')

diccio = {
    'naranja': 'orange',
    'manzana': 'apple',
    'pera': 'pear'
}

print('Diccionario ', diccio)

# Eliminar
del(diccio['manzana'])
print('Diccionario ', diccio)

# Agregar
diccio['sandia'] = 'watermelon'
print('Diccionario', diccio)

print('\n\n---[Diapo 26.b]---------------------')
print('Agregar y eliminar elementos a los diccionarios')