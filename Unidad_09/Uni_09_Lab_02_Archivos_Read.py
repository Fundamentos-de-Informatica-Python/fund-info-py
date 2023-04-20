# UNIDAD 09.D11 Archivos

# Leyendo el contenido de un archivo de texto plano

print('\n\n---[Diapo 09]---------------------')
print('Archivos - Archivos de texto plano')

from io import  open
archivo = open('clase archivos/prueba.txt','r')

contenido = archivo.read()
print(contenido)

archivo.close()
del (archivo)




print('\n\n---[Diapo 13 y 14]---------------------')
print('Archivos - Lectura del contenido en lista')

from io import  open

#----------------------------
# Lee: Todas las líneas
archivo = open('clase archivos/prueba.txt','r')

contenidoLista = archivo.readlines()
print(contenidoLista)

archivo.close()
del (archivo)

#----------------------------
# Lee: Solo una línea
archivo = open('clase archivos/prueba.txt','r')

linea = archivo.readline()
print(linea)

archivo.close()
del (archivo)



print('\n\n---[Diapo 15]---------------------')
print('Archivos - Procesamiento línea por línea')

from io import  open

#----------------------------
# Lee: Todas las líneas
archivo = open('clase archivos/prueba.txt','r')

contenidoLista = archivo.readlines()
for linea in contenidoLista:
    print(linea)

archivo.close()
del (archivo)


#----------------------------
# Lee: Todas las líneas
archivo = open('clase archivos/prueba.txt','r')

linea = archivo.readline()
while linea != '':
    print(linea)
    linea = archivo.readline()

archivo.close()
del (archivo)




print('\n\n---[Diapo 16]---------------------')
print('Archivos - Procesamiento línea por línea')

from io import  open

#----------------------------
# Lee: Todas las líneas

with open('clase archivos/prueba.txt','r') as archivo:
    for linea in archivo:
        print(linea)

# Con With no se necesita cerrar al archivo


