# UNIDAD 10.D01

# Ciencia de datos en Python. NumPy


print('\n\n---[Diapo 06]---------------------')
print('Pandas Demo')

import pandas as pd

s = pd.Series([12,-4,-7,-9])
print(s)
print('values: ', s.values)
print('index: ', s.index)


print('\n\n---[Diapo 07]---------------------')
s = pd.Series([12,-4,-7,-9], index=['a','b','c','d'])
print(s)
print('values: ', s.values)
print('index: ', s.index)


print('\n\n---[Diapo 08]---------------------')
print('Seleccionando elementos individuales o múltiples')

s = pd.Series([12,-4,-7,-9], index=['a','b','c','d'])
print(s)
print('Por indices: ', s[2])
print('Por clave: ', s['b'])

# Rangos
print('Por indices: ', s[0:2])
print('Por clave: ', s[['b','c']])

# Asignando valores individuales o múltiples
print('\nAsignaciones Simple y Multiple')
s[0] = 10
s['b'] = -19
print(s)

s[0:2] = 18
s[['c','d']] = -4
print(s)
