# UNIDAD 09.D50 Bases de Datos
# SQL. Visualizando y administrando una base de datos


#---------------------------------------------------
# Diapo 51 - Base de Dato Vacia
import sqlite3

conexion = sqlite3.connect('base de datos/MyNuevaBBDD.db')
conexion.close()


#---------------------------------------------------
# Diapo 53 - Creando una Tabla desde Python
import sqlite3

conexion = sqlite3.connect('base de datos/AprendoBBDD.db')

cursor = conexion.cursor()

sentenciaSQL = 'CREATE TABLE articulos'
sentenciaSQL = sentenciaSQL + '(nombre VARCHAR(100),'
sentenciaSQL = sentenciaSQL + ' stock integer)'

cursor.execute(sentenciaSQL)

conexion = sqlite3.connect('base de datos/AprendiendoBBDD.db')
conexion.close()


#---------------------------------------------------
# Diapo 56 - Insertando registros en la tabla
import sqlite3

conexion = sqlite3.connect('base de datos/AprendoBBDD.db')

cursor = conexion.cursor()

sentenciaSQL = "INSERT INTO articulos "
sentenciaSQL = sentenciaSQL + "VALUES ('Tensiometro', 5)"

cursor.execute(sentenciaSQL)

conexion.commit()
conexion.close()



