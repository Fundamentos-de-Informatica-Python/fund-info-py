# UNIDAD 09.D30 Archivos CSV - Escritura

# Archivos CSV


print('\n\n---[Diapo 30]---------------------')
print('Archivos CSV. Escritura')

import csv

clientes = [
    ( 'Jose', 'Peralta', 24, 'jose.peralta@email.com' ),
    ( 'Marta', 'Lopez', 33, 'marta.lopez@email.com' ),
    ( 'Ernesto', 'Garcia', 36, 'ernesto.garcia@email.com' ),
    ( 'Norma', 'Gonzalez', 28, 'norma.gonzalez@email.com' )
]

with open('clase archivos/clientes.csv','w', newline='\n') as archivo:
    writer = csv.writer(archivo, delimiter=';')
    for cliente in clientes:
        writer.writerow(cliente)

archivo.close()
del (archivo)






print('\n\n---[Diapo 32]---------------------')
print('Archivos CSV. Lectura')

import csv

with open('clase archivos/clientes.csv','r', newline='\n') as archivo:
    reader = csv.reader(archivo, delimiter=';')
    for cliente in reader:
        print(cliente, type(cliente))

archivo.close()
del (archivo)
