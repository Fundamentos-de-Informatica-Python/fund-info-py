# UNIDAD 00.D21 Archivos - Punteros

# Modo de lectura y escritura

print('\n\n---[Diapo 21]---------------------')
print('Modo de lectura y escritura')

from io import  open
archivo = open('clase archivos/prueba.txt','r+')

print('\n------------')
archivo.seek(1)
contenido = archivo.read()
print(contenido)

print('\n------------')
archivo.seek(25)
nuevo = '--hola--'
archivo.write(nuevo)

print('\n------------')
archivo.seek(1)
contenido = archivo.read()
print(contenido)

archivo.close()
del (archivo)

