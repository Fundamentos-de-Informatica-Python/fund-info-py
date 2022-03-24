# UNIDAD 05.D17 - D18

# Funciones. Argumentos Variables

print('\n\n---[Diapo 17.a]---------------------')
print('Funciones - Argumentos Indeterminados')

def indeterminados(*args):
    print('Argumentos: ', args)
    print('Tipo de datos: ', type(args))
    return

indeterminados('Hola', 25, [1,2,3,4,5], True)


print('\n\n---[Diapo 17.b]---------------------')
print('Funciones - Argumentos Indeterminados')

def indeterminados(*args):
    for arg in args:
        print('Argumento: ', arg)
    return

indeterminados('Hola', 25, [1,2,3,4,5], True)



print('\n\n---[Diapo 18.a]---------------------')
print('Funciones - Argumentos Indeterminados, por nombre')


def indeterminados(**kvargs):
    print('Argumentos: ', kvargs)
    print('Tipo: ', type(kvargs))
    return

indeterminados(producto='Caramelos', precio=2.00, stock=1500)


def indeterminados(**kvargs):
    for kvarg in kvargs:
        print('Clave ', kvarg, ' Valor: ', kvargs[kvarg])
    return

indeterminados(producto='Caramelos', precio=2.00, stock=1500)

