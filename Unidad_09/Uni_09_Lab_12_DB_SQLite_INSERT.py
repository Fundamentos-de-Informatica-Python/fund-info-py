# UNIDAD 09.D50 Bases de Datos
# SQL. Visualizando y administrando una base de datos


#---------------------------------------------------
# Diapo 53 - Creando una Tabla desde Python
import sqlite3

conexion = sqlite3.connect('base de datos/FarmaciaBBDD.db')

try:
    cursor = conexion.cursor()
    sentenciaSQL = 'CREATE TABLE articulos'
    sentenciaSQL = sentenciaSQL + '(nombre VARCHAR(100),'
    sentenciaSQL = sentenciaSQL + ' stock integer)'
    cursor.execute(sentenciaSQL)

except Exception as e:
    print('Hubo una Exception: ', e)

conexion = sqlite3.connect('base de datos/FarmaciaBBDD.db')
conexion.close()



#---------------------------------------------------
# Diapo 57 - Insertando registros en la tabla
import sqlite3

conexion = sqlite3.connect('base de datos/FarmaciaBBDD.db')

cursor = conexion.cursor()


#---
sentenciaSQL  = "INSERT INTO articulos "
sentenciaSQL += "VALUES ('Termometro', 1050)"
cursor.execute(sentenciaSQL)

#---
sentenciaSQL  = "INSERT INTO articulos "
sentenciaSQL += "VALUES ('Ibuprofeno', 50)"
cursor.execute(sentenciaSQL)

#---
sentenciaSQL  = "INSERT INTO articulos "
sentenciaSQL += "VALUES ('Paracetamol', 450)"
cursor.execute(sentenciaSQL)

cursor.execute(sentenciaSQL)

conexion.commit()
conexion.close()






#---------------------------------------------------
# Diapo 59 - Insertando registros en la tabla
import sqlite3

conexion = sqlite3.connect('base de datos/FarmaciaBBDD.db')

cursor = conexion.cursor()


#---
articulos = [
    ('Curitas', 2000),
    ('Vendas',  1400),
    ('Alcohol',  300)
]

sentenciaSQL = "INSERT INTO articulos VALUES (?, ?)"
cursor.executemany(sentenciaSQL, articulos)

conexion.commit()
conexion.close()
