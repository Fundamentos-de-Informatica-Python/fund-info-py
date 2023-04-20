# UNIDAD 10.D17

# Creando un DataFrame


print('\n\n---[Diapo 17]---------------------')
print('Creando un DataFrame')

import pandas as pd

data = {
    'color': ['blue','green','yellow','red','white'],
    'object': ['red', 'yellow', 'green', 'orange', 'blue'],
    'price': [1.2, 1.0, 0.6, 0.9, 1.7]
}

frame_ej1 = pd.DataFrame(data)
print(frame_ej1)

frame_ej2 = pd.DataFrame(data, columns=['object', 'price'])

my_dicc = { 'red':100, 'blue':200, 'yellow':500, 'orange':700, 'green':600 }
print(frame_ej1)
print(frame_ej2)




print('\n\n---[Diapo 18]---------------------')
print('Creando un DataFrame con etiquetas')

data = {
    'color': ['blue','green','yellow','red','white'],
    'object': ['red', 'yellow', 'green', 'orange', 'blue'],
    'price': [1.2, 1.0, 0.6, 0.9, 1.7]
}

frame_ej2 = pd.DataFrame(data, columns=['object', 'price'])
print(frame_ej2)

frame_ej3 = pd.DataFrame(data, columns=['one', 'two', 'three','four', 'five'])
print('Columnas: ', frame_ej3.columns)
print('Index: ',    frame_ej3.index)
print('Values: ',   frame_ej3.values)


# Da Error: TODO: Revisar
print('Seleccionando una columna del DataFrame')
columna_precio = frame_ej3['price']

print(columna_precio)
