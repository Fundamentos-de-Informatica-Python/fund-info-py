# Clase 'Restriction' con las restricciones posibles para el menú de DreamFly
class Restriction:

    # Constructor de de lo objetos
    def __init__(self, id, code, name_eng, name_esp, stock, date, usd_value):
        self.id = id
        self.code = code
        self.name_eng = name_eng
        self.name_esp = name_esp
        self.stock = stock
        self.date = date
        self.usd_value = usd_value
        print('Restriction - constructor ', self)

    def serialize(self):
        return {
            'id': self.id,
            'code': self.code,
            'name_eng': self.name_eng,
            'name_esp': self.name_esp,
            'stock': self.stock,
            'date': self.date,
            'usd_value': self.usd_value
        }

    # Destructor
    def __del__(self):
        print('Restriction - destructor de ', self)
        self.id = ''
        self.code = ''
        self.name_eng = ''
        self.name_esp = ''
        self.stock = ''
        self.date = ''
        self.usd_value = ''

