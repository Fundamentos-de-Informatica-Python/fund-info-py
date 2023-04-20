# UNIDAD 10.D01

# Ciencia de datos en Python. NumPy


print('\n\n---[Diapo 06]---------------------')
print('Pandas Demo')

import pandas as pd

# Filtrando valores en la serie
print('\n\n---[Diapo 10 y 11]---------------------')
print('Filtrando valores en la serie')

s = pd.Series([12,-4,-7,-9], index=['a','b','c','d'])

sMayore = s[s > 8]
print('sMayore: ', sMayore)


print('Aplicando operaciones matemáticas a las series')
suma = s + 3
print('suma: \n ', suma)

suma = s /  2
print('sMayore: \n ', suma)



print('\n\n---[Diapo 12 y 13]---------------------')
print('Obteniendo la media de la serie')

s = pd.Series([12,-4,-7,-9], index=['a','b','c','d'])
promedio_serie = s.mean()
desvio_serie = s.std()
print('Promedio: ', promedio_serie)
print('Desvio estanadr', desvio_serie)

print('\nDescribe la serie: ')
print(s.describe())
