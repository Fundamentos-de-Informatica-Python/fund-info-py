# UNIDAD 09.D30 Archivos CSV - Escritura

# Archivos CSV


print('\n\n---[Diapo 35]---------------------')
print('Archivos CSV. Escritura en Diccionarios')

import csv

clientes = [
    ( 'Jose', 'Peralta', 24, 'jose.peralta@email.com' ),
    ( 'Marta', 'Lopez', 33, 'marta.lopez@email.com' ),
    ( 'Ernesto', 'Garcia', 36, 'ernesto.garcia@email.com' ),
    ( 'Norma', 'Gonzalez', 28, 'norma.gonzalez@email.com' )
]

with open('clase archivos/clientes_dicc.csv','w', newline='\n') as archivo:
    campos = ['nombre', 'apellido', 'edad', 'email']
    writer = csv.DictWriter(archivo, fieldnames=campos)
    writer.writeheader()
    for nombre, apellido, edad, email in clientes:
        writer.writerow({
            'nombre':nombre,
            'apellido': apellido,
            'edad': edad,
            'email': email
        })

archivo.close()
del (archivo)






print('\n\n---[Diapo 36]---------------------')
print('Archivos CSV. Lectura en Diccionarios')

import csv

with open('clase archivos/clientes_dicc.csv','r', newline='\n') as archivo:
    reader = csv.DictReader(archivo)
    for cliente in reader:
        print(cliente['nombre'],
              cliente['apellido'],
              cliente['edad'],
              cliente['email'])