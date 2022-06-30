# UNIDAD 10.D26

# Realizando operaciones aritméticas entre DataFrames


print('\n\n---[Diapo 26]---------------------')
print('Realizando operaciones aritméticas entre DataFrames')

import pandas as pd

mesDict = {
    'red': {2012:800, 2013:600},
    'white': {2011:1500, 2012:800, 2013:400},
    'Blue': {2011:300, 2012:800, 2013:600}
}

mesDict2 = {
    'red': {2012:800, 2013:600},
    'white': {2011:1500, 2012:800, 2013:400},
    'Blue': {2011:300, 2012:800, 2013:600}
}

frame = pd.DataFrame(mesDict)
frame2 = pd.DataFrame(mesDict2)

frameSuma = frame.add(frame2)

print('Frame from Dicc: \n', frameSuma)


print('\n\n---[Diapo 27]---------------------')
print('Obteniendo medidas estadísticas de un DataFrame')

import pandas as pd

mesDict = {
    'red': {2012:800, 2013:600},
    'white': {2011:1500, 2012:800, 2013:400},
    'Blue': {2011:300, 2012:800, 2013:600}
}


frame = pd.DataFrame(mesDict)

suma = frame.sum()
promedio = frame.mean()

print('suma: ', suma)
print('promedio: ', promedio)

print('describe: ', frame.describe())


