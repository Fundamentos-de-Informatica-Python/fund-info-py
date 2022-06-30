# UNIDAD 10.D29

# Creando un DataFrame


print('\n\n---[Diapo 20]---------------------')
print('Creando un DataFrame')

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
print('Filas: \n ', filas)


print('------------------')

frame.index.name = 'id'
frame.columns.name = 'item'
print(frame)
