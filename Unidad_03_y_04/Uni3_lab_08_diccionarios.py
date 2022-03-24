# UNIDAD 03.D28 - D29

# Diccionarios

print('\n\n---[Diapo 27]---------------------')
print('Diccionarios e Iteraciones:')

diccio = {
    'naranja': 'orange',
    'manzana': 'apple',
    'pera': 'pear'
}

print('Se imprimen las claves: ')
for fruta in diccio:
    print(fruta)

print('Se imprime con clave, valores: ')
for fruta in diccio:
    print(fruta, ' ->', diccio[fruta])

print('Se imprime con clave, valores: ')
for clave, valor in diccio.items():
    print(clave, ' ->', valor)


print('\n\n---[Diapo 28]---------------------')
print('Stock en mi kiosco:')

articulos = []
articulo = {'nombre': 'chicle', 'precio': 10, 'stock': 1500}
articulos.append(articulo)
articulo = {'nombre': 'alfajor', 'precio': 40, 'stock': 300}
articulos.append(articulo)
articulo = {'nombre': 'caramelo', 'precio': 2, 'stock': 10000}
articulos.append(articulo)

for art in articulos:
    print(art['nombre'], '$', art['precio'], 'stock: ', art['stock'])


