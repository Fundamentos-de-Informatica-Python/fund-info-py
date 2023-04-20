def fun_acredtar_ca(cuenta):
    print('Deposito en Caja de Ahorro (CA):')
    cantidad = int(input('Ingrese la cantidad: '))
    # _fun_ingresar_cantidad()
    cuenta['saving_bank']['amount'] += cantidad
    cuenta['last_trxs'].append(cantidad)


def fun_saldo_ca(cuenta):
    account_num = cuenta['saving_bank']['account_num']
    amount = cuenta['saving_bank']['amount']

    print('++ Resumen de la CA ++')
    print('Numero de la cuenta', account_num)
    print('Saldo: La$ ', amount)
    print('----------------------')


def fun_saldo_cc(cuenta):
    account_num = cuenta['current_bank']['account_num']
    amount = cuenta['current_bank']['amount']

    print('++ Resumen de la CC ++')
    print('Numero de la cuenta', account_num)
    print('Saldo: La$ ', amount)
    print('----------------------')


def _fun_ingresar_cantidad():
    cantidad = 0
    while True:
        try:
            cantidad = int(input("Ingrese la cantidad en La$ : "))
            break
        except Exception:
            print('Ingrese un valor valido')
    return cantidad


def fun_acredtar_cc(cuenta):
    print('Deposito en Cuenta Corriente (CC):')
    cantidad = _fun_ingresar_cantidad()
    cuenta['current_bank']['amount'] += cantidad
    cuenta['last_trxs'].append(cantidad)


def fun_trx(cuenta, cant):
    print('------------------------------')
    print('Ultimas ', cant, 'realizadas: ')
    trxs = cuenta['last_trxs'][-cant:]
    trxs.reverse()
    for t in trxs:
        print('\t La$ ', t)
    print('------------------------------')


def fun_salir(user):
    print('Gracias ', user, ' por utilizar nuestro sistema.')
    user = ''
    password = ''
    cuenta = {}
    print('Saliendo....')
