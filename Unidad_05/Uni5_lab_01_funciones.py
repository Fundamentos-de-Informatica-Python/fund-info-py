# UNIDAD 05.D04 - D05

# Funciones

print('\n\n---[Diapo 05]---------------------')
print('Funciones')

def saludar():
    print('Hola! Estoy saludando desde la función')

print('Antes de la función "saludar()" ')
saludar()
print('Después de la función "saludar()" ')


print('\n\n---[Diapo 06]---------------------')
print('Función tabla del 10')

def tabla_del_10():
    for nro in range(10):
        print('10 x {} = {}'.format(nro, nro*10))

tabla_del_10()


print('\n\n---[Diapo 06.b]---------------------')
print('Función tabla del Multiplicar')
print('Recibe Parámetros!')


def tabla_de_multiplicar(n):
    print('\n Tabla del ', n)
    for nro in range(10):
        print('{} x {} = {}'.format(n, nro, nro * n))

tabla_de_multiplicar(3)
tabla_de_multiplicar(5)