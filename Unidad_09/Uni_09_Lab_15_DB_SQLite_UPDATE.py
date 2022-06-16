# UNIDAD 09.D50 Bases de Datos
# SQL. Visualizando y administrando una base de datos


#---------------------------------------------------
# Diapo 64 - UPDATE UN REGISTRO
import sqlite3

conexion = sqlite3.connect('base de datos/FarmaciaBBDD.db')

cursor = conexion.cursor()

sentenciaSQL  = "UPDATE articulos SET stock = stock - 1 WHERE nombre = 'Termometro'  "
cursor.execute(sentenciaSQL)

sentenciaSQL  = "SELECT * FROM articulos  WHERE nombre = 'Termometro'  "
cursor.execute(sentenciaSQL)

articulos = cursor.fetchall()
for articulo in articulos:
    print("Articulo: ", articulo)

conexion.close()
