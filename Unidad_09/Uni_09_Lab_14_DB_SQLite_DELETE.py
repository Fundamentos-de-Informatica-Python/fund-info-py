# UNIDAD 09.D50 Bases de Datos
# SQL. Visualizando y administrando una base de datos


#---------------------------------------------------
# Diapo 62 - SELECT - Todos los Registros
import sqlite3

conexion = sqlite3.connect('base de datos/FarmaciaBBDD.db')

cursor = conexion.cursor()

sentenciaSQL  = "SELECT * FROM articulos   "
cursor.execute(sentenciaSQL)

articulos = cursor.fetchall()
for articulo in articulos:
    print("Articulo: ", articulo)

conexion.close()


#---------------------------------------------------
# Diapo 62 - DELETE - Borramos todos los registros 'Paracetamol'

import sqlite3

conexion = sqlite3.connect('base de datos/FarmaciaBBDD.db')

cursor = conexion.cursor()

print('\n\n--[Borra Parracetamol]----- ')
sentenciaSQL  = "DELETE FROM articulos WHERE nombre = 'Paracetamol' "
cursor.execute(sentenciaSQL)


sentenciaSQL  = "SELECT * FROM articulos   "
cursor.execute(sentenciaSQL)

articulos = cursor.fetchall()
for articulo in articulos:
    print("Articulo: ", articulo)

conexion.close()