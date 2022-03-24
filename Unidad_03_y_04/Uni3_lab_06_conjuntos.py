# UNIDAD 03.D22 - D23

# Set - Conjuntos

print('\n\n---[Diapo 21]---------------------')
print('Conjunto vacío:')

frutas = set()

print('El contenido del conjunto es:', frutas)
print('Y el tipo de dato es:', type(frutas))


print('\nConjunto con elementos:')

frutas = {'manzana', 'naranja', 'pera'}

print('El conjunto contiene:', frutas)

frutas.add('mandarina')
print('Y ahora:', frutas)


print('\n\n---[Diapo 22.a]---------------------')
print('Agregamos elementos repetidos:')

frutas = {'manzana', 'naranja', 'pera', 'pera', 'pera'}

print('Contenido de frutas:', frutas)

frutas.add('manzana')
frutas.add('pera')

print('Y ahora:', frutas)


print('\n\n---[Diapo 22.b]---------------------')
print('Un Truco! Cómo eliminar elmentos duplicados en listas? ...')

frutas = ['manzana', 'pera', 'naranja', 'pera', 'pera']

print('Frutas: ', frutas)

conjunto = set(frutas)
frutas = list(conjunto)

print('Y ahora: ', frutas)


print('\n\n---[Diapo 23.a]---------------------')
print('Eliminar elementos de un conjunto:')

frutas = {'manzana', 'naranja', 'pera'}
print('Contenido de frutas:', frutas)

frutas.remove('naranja')
print('Y ahora:', frutas)


print('\n\n---[Diapo 23.b]---------------------')
print('Pertenece a un conjunto')

frutas = {'manzana', 'naranja', 'pera'}
print('Contenido de frutas:', frutas)

print('\n in ')

print('Está la naranja?:', 'naranja' in frutas)
print('Está la mandarina?:', 'mandarina' in frutas)

print('\n not in ')

print('No está la naranja?:', 'naranja' not in frutas)
print('No está la mandarina?:', 'mandarina' not in frutas)
