# UNIDAD 05.D08 - D11

# Funciones. Retornando Valores

print('\n\n---[Diapo 08]---------------------')
print('Funciones - Retornando Valores')

def saludar():
    return 'Hola a tod@s!'

saludar = saludar()
print('el valor de la función es ', saludar)



print('\n\n---[Diapo 09]---------------------')

def valor5():
    return 5

print('5 mas 5 es ', valor5() + 5)

def dias_semana():
    return ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

print('Hábiles: ', dias_semana()[0:5])
print('No Hábiles: ', dias_semana()[-2:])


print('\n Parametrizado: ')

def dias_semana(habiles):
    dias = ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']
    if habiles:
        return dias[0:5]
    else:
        return dias[-2:]


print('Hábiles: ', dias_semana(True))
print('No Hábiles: ', dias_semana(False))


print('\n\n---[Diapo 10]---------------------')

def dias_semana():
    return ['Lunes', 'Martes', 'Miércoles', 'Jueves', 'Viernes', 'Sábado', 'Domingo']

dias = dias_semana()
print('Hábiles: ', dias[0:5])
print('No Hábiles: ', dias[-2:])



print('\n\n---[Diapo 11]---------------------')
print('Multiples retonos')

def multiples_retornos():
    return 'Hola', 29, True, [1,2,3,4]

multiple = multiples_retornos()
print('Tipo de retorno: ', type(multiple))
print('Valor retornado: ', multiple)
print('El primer valor es: ', multiple[0])


primero, segundo, tercero, cuarto = multiples_retornos()
print('El primer valor es: ', primero)
print('El segundo valor es: ', segundo)
print('El tercero valor es: ', tercero)
print('El cuarto valor es: ', cuarto)

