import sqlite3
DATABASE_NAME = "DreamFlyDB.db"

from model import Restriction

def get_db():
    conn = sqlite3.connect(DATABASE_NAME)
    return conn

def select_all_dietas():

    db = get_db()
    cursor = db.cursor()

    query = "SELECT id, code, name_eng, name_esp, stock, date, usd_value FROM Dietas "
    cursor.execute(query)
    list_rta = cursor.fetchall()

    restrictions_list = []

    for row in list_rta:
        id = row[0]
        code = row[1]
        name_eng = row[2]
        name_esp = row[3]
        stock = row[4]
        date = row[5]
        usd_value = row[6]

        obj_restriction = Restriction(id, code, name_eng, name_esp, stock, date, usd_value)
        restrictions_list.append(obj_restriction)

    db.close()

    return restrictions_list


def select_one_dieta(restr_id):

    db = get_db()
    cursor = db.cursor()

    query = "SELECT id, code, name_eng, name_esp, stock, date, usd_value FROM Dietas WHERE code =  '" + restr_id + "'"
    cursor.execute(query)

    row = cursor.fetchone()
    if row == None:
        return []

    id = row[0]
    code = row[1]
    name_eng = row[2]
    name_esp = row[3]
    stock = row[4]
    date = row[5]
    usd_value = row[6]

    obj_restriction = Restriction(id, code, name_eng, name_esp, stock, date, usd_value)

    db.close()

    return obj_restriction

def insert_one_dieta(obj_restriccion):

    db = get_db()
    cursor = db.cursor()

    obj = obj_restriccion

    statement = """INSERT OR IGNORE INTO Dietas (id, code, name_eng, name_esp, stock, date, usd_value) 
                                           VALUES (?, ?, ?, ? ,?, ?, ?)"""
    cursor.execute(statement, [obj.id, obj.code, obj.name_eng, obj.name_esp, obj.stock, obj.date, obj.usd_value])

    db.commit()
    db.close()