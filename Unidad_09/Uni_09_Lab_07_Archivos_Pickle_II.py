# UNIDAD 00.D21 Archivos - Punteros

# Pickle. Administrando una lista de clientes.
import pickle

print('\n\n---[Diapo 26]---------------------')
print('Pickle - Graba')

import pickle
archivo = open('clase archivos/pickles.pkl','wb')

persona = { 'nombre':'Gustavo', 'apellido':'Rodriguez', 'edad':'30', 'telefono':'1154325423' }
pickle.dump(persona, archivo)

persona = { 'nombre':'Gloria' , 'apellido':'Perez',     'edad':'72', 'telefono':'1154326544' }
pickle.dump(persona, archivo)

persona = { 'nombre':'Marcos',  'apellido':'Gimenez',   'edad':'39', 'telefono':'1185687687' }
pickle.dump(persona, archivo)

archivo.close()
del (archivo)



print('\n\n---[Diapo 25]---------------------')
print('Pickle - Recupera')

import pickle
archivo = open('clase archivos/pickles.pkl','rb')

persona1 = pickle.load(archivo)
persona2 = pickle.load(archivo)
persona3 = pickle.load(archivo)
print(persona1)
print(persona2)
print(persona3)


archivo.close()
del (archivo)

