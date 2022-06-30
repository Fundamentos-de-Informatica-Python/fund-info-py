# UNIDAD 10.D28

# Obteniendo relación entre DataFrames


print('\n\n---[Diapo 28]---------------------')
print('Realizando operaciones aritméticas entre DataFrames')

import pandas as pd

sec1 = pd.Series([3,4,3,4,5,4,3,2], [2006, 20007, 2008, 2009, 2010, 2011, 2012, 2013])
sec2 = pd.Series([1,2,3,4,4,1,3,1], [2006, 20007, 2008, 2009, 2010, 2011, 2012, 2013])

correlacion = sec1.corr(sec2)
covarianza  = sec1.cov(sec2)

print('correlación: ', correlacion, ' - covarianza: ', covarianza)



print('\n\n---[Diapo 29]---------------------')
print('Importando y exportando CSV')

data = {
    'color': ['blue','green','yellow','red','white'],
    'object': ['red', 'yellow', 'green', 'orange', 'blue'],
    'price': [1.2, 1.0, 0.6, 0.9, 1.7]
}



frame = pd.DataFrame(data, columns=['one', 'two', 'three','four', 'five'])

frame.to_csv('')


