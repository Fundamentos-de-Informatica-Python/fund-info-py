# UNIDAD 09.D21 Archivos - Punteros

# Modo de lectura y escritura
import pickle

print('\n\n---[Diapo 24]---------------------')
print('Pickle - Graba')

import pickle
archivo = open('clase archivos/prueba.txt','wb')

lista = [0,1,2,3]
pickle.dump(lista, archivo)

archivo.close()
del (archivo)



print('\n\n---[Diapo 25]---------------------')
print('Pickle - Recupera')

import pickle
archivo = open('clase archivos/prueba.txt','rb')

lista = pickle.load(archivo)
print(lista)

archivo.close()
del (archivo)

