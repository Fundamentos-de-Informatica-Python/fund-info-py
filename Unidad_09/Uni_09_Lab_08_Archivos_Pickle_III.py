# UNIDAD 00.D21 Archivos - Punteros

# Pickle. Administrando una lista de clientes.
import pickle

print('\n\n---[Diapo 28]---------------------')
print('Pickle - Lee')

import pickle
archivo = open('clase archivos/pickles.pkl','rb')

while True:
    try:
        cliente = pickle.load(archivo)
        print(cliente)
    except IOError:
        break

archivo.close()
del (archivo)

