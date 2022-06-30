# UNIDAD 10.D15

# Operando aritméticamente entre dos series


print('\n\n---[Diapo 15]---------------------')
print('Operando aritméticamente entre dos series')

import pandas as pd

my_dicc = { 'red':100, 'blue':200, 'yellow':500, 'orange':700, 'green':600 }
colors = ['red', 'yellow', 'green', 'orange', 'blue']

my_serie_from_dict = pd.Series(my_dicc, index=colors)


my_dicc2 = { 'red':400, 'yellow':100, 'black':500 }
my_serie_from_dict = pd.Series(my_dicc)

my_series2 = pd.Series(my_dicc2)

sumar_series = my_serie_from_dict + my_series2
print('Sumar Series: \m', sumar_series)



print('\n\n---[Diapo 14b]---------------------')
print('Creando series a partir de un diccionario')

import pandas as pd

my_dicc = { 'red':100, 'blue':200, 'yellow':500, 'orange':700 }
colors = {'red', 'blue', 'yellow', 'orange', 'green'}

my_serie_from_dict = pd.Series(my_dicc, index=colors)

print(my_serie_from_dict)



print('\n\n---[Diapo 15]---------------------')
print('Operando aritméticamente entre dos series')


import pandas as pd

my_dicc = { 'red':100, 'blue':200, 'yellow':500, 'orange':700 }
colors = {'red', 'blue', 'yellow', 'orange', 'green'}

my_serie_from_dict = pd.Series(my_dicc, index=colors)


my_dicc2 = { 'red':400, 'yellow':100, 'black':500 }
my_series2 = pd.Series(my_dicc2)


sumar_series = my_serie_from_dict + my_series2
print('Sumar Series: \n', sumar_series)
