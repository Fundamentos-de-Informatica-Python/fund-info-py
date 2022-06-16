# UNIDAD 09.D19 Archivos - Punteros

# Archivos de texto plano. Manejo del puntero

print('\n\n---[Diapo 19]---------------------')
print('Archivos - Manejo del puntero')

from io import  open
archivo = open('clase archivos/prueba.txt','r')

archivo.seek(10)
contenido = archivo.read()
print(contenido)

archivo.close()
del (archivo)



print('\n\n---[Diapo 20]---------------------')
print('Archivos - Manejo del puntero')

from io import  open
archivo = open('clase archivos/prueba.txt','r')

archivo.seek(10)
contenido = archivo.read(6)
print(contenido)

archivo.close()
del (archivo)
