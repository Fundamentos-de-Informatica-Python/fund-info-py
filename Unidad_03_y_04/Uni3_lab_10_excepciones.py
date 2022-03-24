# UNIDAD 03.D33 - D36

# Excepciones con try / Catch

print('\n\n---[Diapo 33.a]---------------------')
print('Errores Semánticos:')

numero = int(input('Ingrese un número:'))
division = 10 / numero
print('Resultado: ', division)



# Try / Except
print('\n\n---[Diapo 33.b]---------------------')
print('Excepciones:')

try:
    numero = int(input('Ingrese un número:'))
    division = 10 / numero
    print('Resultado: ', division)
except:
    print('Error: algo fallo al intentar realizar el cálculo')



# Try / Except
print('\n\n---[Diapo 34]---------------------')
print('Se reintenta hasta que se ingresa ok:')

while True:
    try:
        numero = int(input('Ingrese un número:'))
        division = 10 / numero
        print('Resultado: ', division)
        break
    except:
        print('Error: algo fallo al intentar realizar el cálculo')


print('Fin del Programa de división.')


# Try / Except / Else
print('\n\n---[Diapo 35.a]---------------------')
print('Se reintenta hasta que se ingresa ok:')

while True:
    try:
        numero = int(input('Ingrese un número:'))
        division = 10 / numero
    except:
        print('Error: algo fallo al intentar realizar el cálculo')
    else:
        print('Resultado: ', division)
        break

print('Fin del Programa de división.')





# Try / Except / Else / Finally
print('\n\n---[Diapo 35.b]---------------------')
print('Se reintenta hasta que se ingresa ok:')

while True:
    try:
        numero = int(input('Ingrese un número:'))
        division = 10 / numero
    except:
        print('Error: algo fallo al intentar realizar el cálculo')
    else:
        print('Resultado: ', division)
        break
    finally:
        print('Este bloque se ejecuta siempre')

print('Fin del Programa de división.')




'''
Excepciones Múltiples
Ejemplo con ValueError y ZeroDivisionError
'''
print('\n\n---[Diapo 36]---------------------')
print('Determinando el tipo de excepción:')

while True:
    try:
        numero = int(input('Ingrese un número:'))
        division = 10 / numero
        print('Resultado: ', division)
        break
    except Exception as e:
        print('Error del tipo:', type(e).__name__)

print('Fin del Programa de división.')




print('\n\n---[Diapo 37]---------------------')
print('Excepciones múltiples:')

while True:
    try:
        numero = int(input('Ingrese un número:'))
        division = 10 / numero
        print('Resultado: ', division)
        break
    except ValueError:
        print('Ingrese un valor numérico')
    except ZeroDivisionError:
        print('Ingrese un valor distinto de 0')
    except Exception as e:
        print('Error del tipo:', type(e).__name__)

print('Fin del Programa de división.')




print('\n\n---[Diapo 38]---------------------')
print('Lanzando a mis propias excepciones:')

try:
    raise ValueError('Error en el valor del dato')
except Exception as e:
    print('Error de tipo', type(e).__name__, ':', e)