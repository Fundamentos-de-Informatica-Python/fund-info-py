# UNIDAD 05.D11 - D15

# Funciones. Recibiendo Valores

print('\n\n---[Diapo 11]---------------------')
print('Funciones - Recibiendo Valores')

def calcular_IVA(importe):
    return 0.21 * importe

print('El iva es de 1000.00 es: ', calcular_IVA(1000.00))
print('El iva es de 2000.00 es: ', calcular_IVA(2000.00))


def promedio(num1, num2, num3):
    return (num1 + num2 + num3) / 3

print('El promedio de 1, 5 y 10 es: ', promedio(1, 5, 10))
print('El promedio de 10, 100 y 150 es: ', promedio(10, 100, 150))


print('\n\n---[Diapo 12]---------------------')
print('Funciones - Recibiendo Valores por nombre')

def calcular_impuesto(importe, tasa):
    return tasa * importe / 100

print('El IVA en Argentina sobre $ 1000 es',
      calcular_impuesto(importe=1000.00, tasa=21))
print('El IVA en Uruguay sobre $ 1000 es',
      calcular_impuesto(tasa=22, importe=1000.00))



print('\n\n---[Diapo 13.a]---------------------')
print('Funciones - Recibiendo Valores. Default')

def calcular_impuesto(importe, tasa):
    return tasa * importe / 100

print('El IVA en Argentina sobre $ 1000 es',
      calcular_impuesto(importe=1000.00, tasa=21))
print('El IVA en Uruguay sobre $ 1000 es',
      calcular_impuesto(tasa=22, importe=1000.00))
# print('El IVA en Chile sobre $ 1000 es',
#      calcular_impuesto(importe=1000.00))                # Error!!




print('\n\n---[Diapo 13.b]---------------------')
print('Funciones - Recibiendo Valores default')

def calcular_impuesto(importe, tasa=15):
    return tasa * importe / 100

print('El IVA en Argentina sobre $ 1000 es',
      calcular_impuesto(importe=1000.00, tasa=21))
print('El IVA en Uruguay sobre $ 1000 es',
      calcular_impuesto(tasa=22, importe=1000.00))
print('El IVA en Chile sobre $ 1000 es',
      calcular_impuesto(importe=1000.00))






print('\n\n---[Diapo 14]---------------------')
print('Funciones - Argumentos por valor, y por Referencia')

def multiplicar_por_5(numero):
    numero *= 5
    return numero

n = 100
print('El resultado es: ', multiplicar_por_5(n))
print('El valor de n es: ', n)


print('\n\n---[Diapo 15]---------------------')
print('Funciones - Argumentos por valor, y por Referencia')

def multiplicar_por_5_lista(lista):
    for n in range(len(lista)):
        lista[n] = lista[n] * 5
    return

lista = [10, 20, 30]
multiplicar_por_5_lista(lista)
print('El valor de lista es: ', lista)