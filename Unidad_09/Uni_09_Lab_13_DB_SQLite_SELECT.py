# UNIDAD 09.D50 Bases de Datos
# SQL. Visualizando y administrando una base de datos


#---------------------------------------------------
# Diapo 59 - SELECT - Consultando un único registro desde Python
import sqlite3

conexion = sqlite3.connect('base de datos/FarmaciaBBDD.db')

cursor = conexion.cursor()

sentenciaSQL  = "SELECT * FROM articulos WHERE nombre = 'Termometro' "
cursor.execute(sentenciaSQL)

articulo = cursor.fetchone()
print('articulo: ', articulo)
conexion.close()





#---------------------------------------------------
# Diapo 60 - SELECT - Consultando un único registro desde Python
import sqlite3

conexion = sqlite3.connect('base de datos/FarmaciaBBDD.db')

cursor = conexion.cursor()

sentenciaSQL  = "SELECT * FROM articulos WHERE nombre = 'Termometro' "
cursor.execute(sentenciaSQL)

articulo = cursor.fetchone()

print('articulo: ', articulo)
print('articulo: nombre - ', articulo[0])
print('articulo: stock  - ', articulo[1])


#-- Varias veces trae diferentes ------

sentenciaSQL  = "SELECT * FROM articulos "
cursor.execute(sentenciaSQL)

#-- Siguientes articulos ---
articulo = cursor.fetchone()
print('articulo: ', articulo)

#-- Siguientes articulos ---
articulo = cursor.fetchone()
print('articulo: ', articulo)

#-- Siguientes articulos ---
articulo = cursor.fetchone()
print('articulo: ', articulo)


print("\n----")

#-- Varias veces, con fetchalll ------

sentenciaSQL  = "SELECT * FROM articulos "
cursor.execute(sentenciaSQL)

articulos = cursor.fetchall()
for articulo in articulos:
    print("Articulo: ", articulo)

conexion.close()



#---------------------------------------------------
# Diapo 60 - SELECT - Consultando un único registro desde Python



#---------------------------------------------------
# Diapo 62 - SELECT - Consultando varios registros desde Python