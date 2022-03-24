# UNIDAD 03.D18 - D19

# Tuplas

print('\n\n---[Diapo 18 y 19.a]---------------------')

mis_frutas = ('manzana', 'mandarina', 'naranja')

print('Contenido de la tupla:', mis_frutas)
print('Y el tipo de dato es:', type(mis_frutas))

print()

print('El segundo elemento es:', mis_frutas[1])
print('Los ùltimos dos elementos son:', mis_frutas[-2:])

print()
print('La longitud de la tupla es:', len(mis_frutas))

print('\n\n---[Diapo 19.b]--------------------------')

# Errores por Inmutabilidad:

mis_frutas = ('manzana', 'mandarina', 'naranja')

mis_frutas['0'] = 'Pera'        # Error!

mis_frutas.append('pera')       # Error! ... la tupla es inmutable!






print('\n\n---[Diapo 18]--------------------------')