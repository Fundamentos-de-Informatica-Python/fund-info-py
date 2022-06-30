# UNIDAD 10.D28

# Visualizando con MAtpilot

print('\n\n---[Diapo 28]---------------------')
print('Realizando operaciones aritméticas entre DataFrames')

import pandas as pd
import matpilot.pylot as plt

# barras
df = pd.DataFrame()
df.plot.bar(x='lab', y='val', rot=0)

# barras con colores
speed = [0.1, 17.5, 40, 48, 52, 69, 88]
lifespan = [2, 8, 79, 1.5, 25, 12, 28]

index = ['snail', 'pig', 'elephant',
         'rabbit', 'giraffe', 'coyote', 'horse']

df = pd.DataFrame({'speed': speed,
                   'lifespan': lifespan}, index=index)

df.plot.bar(rot=0)


# ploting pie

df_pie = pd.DataFrame({'mass': [0.330, 4.87, 5.97],
                       'radius': [2439.7, 6051.8, 6378.1]},
                      index=['Mercury', 'Venus', 'Earth'])

plot = df.pie.plot.pie(y='mass', figsize=(5, 5))  # sun solo pie

plot = df.pie.plot.pie(subplots=True, figsize=(11, 6))  # si se quiere un subplot (dos pie)

plt.show()