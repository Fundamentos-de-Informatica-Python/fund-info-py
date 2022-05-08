# UNIDAD 05.D21

# Funciones. Recursion

print('\n\n---[Diapo 21]---------------------')
print('Funciones - Recursivas')

def bomba(nro):
    if nro > 0:
        print(nro)
        bomba(nro-1)
    else:
        print('BOOOOOOOM!!!')
    return

bomba(5)



print('\n\n---[Diapo 21]---------------------')
print('Funciones - Recursivas - Ejemplo Factorial')
def factorial(n):
    if n > 1:
        f = factorial(n-1)  * n
        print("Respuesta de factorial(", n, ") =",  f)
        return f
    if n == 1:
        print("Caso Base de factorial(", n, ") = 1" )
        return 1


num = 5
val = factorial(num)

print("Factroial de {} = {}".format(num, val))

print('\n\n---[Diapo 21]---------------------')
print('Funciones - Recursivas - Ejemplo Búsqueda Binaria')

def buscar(n, lista):
    if len(lista) == 1:
        if lista[0] == n:
            return True
        else:
            return False

    return buscar(n, lista[0:1]) or buscar(n, lista[1:])


mi_lista = [7, 1, 3, 8, 4]
num1 = 8
encontro = buscar(num1, mi_lista)

print("En la lista {} esta el número {} ? = {}".format(mi_lista, num1, encontro))

num2 = 12
encontro = buscar(num2, mi_lista)

print("En la lista {} esta el número {} ? = {}".format(mi_lista, num2, encontro))
