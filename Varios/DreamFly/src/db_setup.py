import sqlite3
DATABASE_NAME = "DreamFlyDB.db"

from model import Restriction

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

# Crea la Tabla de los distintos tipos de Dieta y Restricciones en el menú
def create_table():
    my_query = """CREATE TABLE IF NOT EXISTS Dietas (
                id INTEGER PRIMARY KEY,
                code TEXT NOT NULL,
                name_eng TEXT NOT NULL,
                name_esp TEXT NOT NULL,
                stock INTEGER NOT NULL,
                date INTEGER NOT NULL,
                usd_value INTEGER NOT NULL
            )
            """

    db = get_db()
    cursor = db.cursor()
    cursor.execute(my_query)



def save_data_inicial():

    restrictions_data = [
        Restriction(1, 'R001', 'Gluten-free', 'Libre de Gluten', 350, '12/08/2024', 100),
        Restriction(2, 'R002', 'Dairy-free', 'Libre de Lacteos', 240, '24/07/2024', 112),
        Restriction(3, 'R003', 'Nut-free', 'Libre de Frutos Secos', 160, '22/12/2024', 123),
        Restriction(4, 'R004', 'Vegetarian', 'Vegetariano', 430, '14/07/2024', 144),
        Restriction(5, 'R005', 'Vegan', 'Vegano', 220, '15/07/2024', 155),
    ]

    db = get_db()
    cursor = db.cursor()

    for obj in restrictions_data:
        statement = """INSERT OR IGNORE INTO Dietas (id, code, name_eng, name_esp, stock, date, usd_value) 
                                               VALUES (?, ?, ?, ? ,?, ?, ?)"""
        cursor.execute(statement, [obj.id, obj.code, obj.name_eng, obj.name_esp, obj.stock, obj.date, obj.usd_value])


    db.commit()
    db.close()

