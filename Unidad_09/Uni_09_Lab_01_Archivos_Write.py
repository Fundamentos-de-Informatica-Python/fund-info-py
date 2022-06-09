# UNIDAD 00.D01 Archivos

# Archivos de texto plano

print('\n\n---[Diapo 05]---------------------')
print('Archivos - Archivos de texto plano')

from io import  open
archivo = open('clase archivos/prueba.txt','w')

linea = 'Una línea con texto\nOtra línea con texto'
archivo.write(linea)


lista = ['\n\nUna línea con texto\n',
            'Otra línea con texto\n',
            'Y la tercera línea']
archivo.writelines(lista)


print('\n\n---[Diapo 06 a 08]---------------------')
print('Archivos - Cierre y Borrado')

val = input('Se va aborrar el achivo, continúa (S/N)?')

print(val)

if val in ['s','S','Y','Yes','Si']:
    print('es un sí')
    archivo.close()
    del (archivo)
else:
    print('es un no')