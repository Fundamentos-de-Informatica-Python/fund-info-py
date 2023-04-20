# UNIDAD 10.D22

# Incorporando una nueva columna al DataFrame


print('\n\n---[Diapo 22]---------------------')
print('Incorporando una nueva columna al DataFrame')

import pandas as pd

data = {
    'color': ['blue','green','yellow','red','white'],
    'object': ['red', 'yellow', 'green', 'orange', 'blue'],
    'price': [1.2, 1.0, 0.6, 0.9, 1.7]
}

frame = pd.DataFrame(data)
fila = frame.loc[2]
print(fila)

filas = frame.loc[[2,4]]

frame['new'] = 12
print('Filas: \n ', frame)


print('--[Diapo 21]----------------')

frame.index.name = 'id'
frame.columns.name = 'item'
print(frame)


frame['new'] = [3.0, 1.2, 2.6, 3.1, 6.4]
print('Filas: \n ', frame)


print('--[Diapo 22]----------------')

menores = frame[frame['price'] < 1]
print(menores)



print('Creando un DataFrame a partir de un diccionario anidado')

mesDict = {
    'red': {2012:800, 2013:600},
    'white': {20122:1500, 2012:800, 2013:400},
    'Blue': {2011:300, 2012:800, 2013:600}
}

frame = pd.DataFrame(mesDict)
print('Frame from Dicc: \n', frame)


print('Transponiendo un DataFrame')

frame_transpuesto = frame.transpose()
print('Frame transpuesto: \n', frame_transpuesto)