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