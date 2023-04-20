# UNIDAD 10.D14

# Creando series a partir de un diccionario


print('\n\n---[Diapo 14]---------------------')
print('Creando series a partir de un diccionario')

import pandas as pd

my_dicc = { 'red':100, 'blue':200, 'yellow':500, 'orange':700 }

my_serie_from_dict = pd.Series(my_dicc)

print(my_serie_from_dict)



print('\n\n---[Diapo 14b]---------------------')
print('Creando series a partir de un diccionario')

import pandas as pd

my_dicc = { 'red':100, 'blue':200, 'yellow':500, 'orange':700 }
colors = {'red', 'blue', 'yellow', 'orange', 'green'}

my_serie_from_dict = pd.Series(my_dicc, index=colors)

print(my_serie_from_dict)
