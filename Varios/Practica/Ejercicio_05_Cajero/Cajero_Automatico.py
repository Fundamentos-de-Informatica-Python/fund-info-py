from Varios.Practica.Ejercicio_05_Cajero.Datos_JSON import accounts, accounts_usada_solo_para_pruebas
from Varios.Practica.Ejercicio_05_Cajero.Cajero_Funciones import fun_trx, fun_salir,fun_saldo_cc,fun_acredtar_cc,fun_acredtar_ca,fun_saldo_ca


ACRED_CA = 1
ACRED_CC = 2
SALDO_CA = 3
SALDO_CC = 4
CONS_TRX = 5
SALIR = 6


def fun_operacines_disponibles():
    opcion = 0
    while opcion not in [ACRED_CA, ACRED_CC, SALDO_CA, SALDO_CC, CONS_TRX, SALIR]:
        print('\t 1) Acreditar en CA')
        print('\t 2) Acreditar en CC')
        print('\t 3) Consultar saldo CA')
        print('\t 4) Consultar saldo CC')
        print('\t 5) Consultar Trx')
        print('\t 6) Salir')
        opcion = int(input('Seleccione una opcion: '))

    return opcion


opcion = fun_operacines_disponibles()

print('La opción elegida es: ', opcion)


'''
Dado el usuario y la password, 
retorna la cuenta de ese usuario.
En caso de error, retorna una colección vacia
'''


def fun_login(user, password):
    cuenta_encontrada = {}

    print('\t\t @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
    print('\t\t @@    Banco Digital LA      @@')
    print('\t\t @@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')

    for cuentad in accounts:
        if cuentad['user_id'] == user:
            print('El usuario existe')
            if cuentad['password'] == password:
                print('El usuario esta logoneado')
                cuenta_encontrada = cuentad
            else:
                print('Clave Erronea')

    return cuenta_encontrada


user = input('Ingrese su usuario: ')
password = input('Ingrese su clave: ')

# Para Pruebas Unitarias
# accounts = tmp_accounts_users

cuenta = fun_login(user, password)

print(cuenta)

tmp_cuenta = {'user_id': 'pablo', 'password': 'supersec123',
              'saving_bank': {'account_num': 'CA-888-111', 'amount': 100},
              'current_bank': {'account_num': 'CC-888-111', 'amount': 200},
              'last_trxs': [3.0, 44.0]
              }

cuenta_a_porbar = {'user_id': 'noemi', 'password': 'supersec333',
                   'saving_bank': {'account_num': 'CA-888-111', 'amount': 100},
                   'current_bank': {'account_num': 'CC-888-111', 'amount': 200}
                   }




fun_acredtar_ca(tmp_cuenta)
fun_acredtar_cc(tmp_cuenta)

print(tmp_cuenta['saving_bank']['amount'])
print(tmp_cuenta['current_bank']['amount'])

fun_saldo_ca(tmp_cuenta)
fun_saldo_cc(tmp_cuenta)

fun_trx(tmp_cuenta, 3)

cuenta_a_porbar = {'user_id': 'noemi', 'password': 'supersec333',
                   'saving_bank': {'account_num': 'CA-888-111', 'amount': 100},
                   'current_bank': {'account_num': 'CC-888-111', 'amount': 200},
                   'last_trxs': []
                   }


fun_acredtar_ca(cuenta_a_porbar)
fun_acredtar_cc(cuenta_a_porbar)
fun_saldo_ca(cuenta_a_porbar)

print(cuenta_a_porbar)



while True:
  user     = input('Ingrese su usuario: ')
  password = input('Ingrese su clave: ')

  cuenta = fun_login(user, password)

  print(cuenta)

  if cuenta != {}:

    opcion = ''

    while opcion != SALIR:
      opcion = fun_operacines_disponibles()

      if opcion == ACRED_CA:
        fun_acredtar_ca(cuenta)
      elif opcion == ACRED_CC:
        fun_acredtar_cc(cuenta)
      elif opcion == SALDO_CA:
        fun_saldo_ca(cuenta)
      elif opcion == SALDO_CC:
        fun_saldo_cc(cuenta)
      elif opcion == CONS_TRX:
        fun_trx(cuenta, 3)
      elif opcion == SALIR:
        fun_salir(user)
