# UNIDAD 09.D17 Archivos - A´´emd

# Agregando contenido de un archivo de texto plano

print('\n\n---[Diapo 17]---------------------')
print('Archivos - Archivos de texto plano')

from io import  open
archivo = open('clase archivos/prueba.txt','a')

nuevaLinea = '\nEsta es la nueva línea'
archivo.write(nuevaLinea)

archivo.close()
del (archivo)




print('\n\n---[Diapo 17]---------------------')
print('Archivos - Procesamiento línea por línea')

from io import  open

#----------------------------
# Lee: Todas las líneas

with open('clase archivos/prueba.txt','r') as archivo:
    for linea in archivo:
        print(linea)

# Con With no se necesita cerrar al archivo


