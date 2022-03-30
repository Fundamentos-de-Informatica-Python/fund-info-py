# UNIDAD 03.D31 - D33

# Errores

print('\n\n---[Diapo 31]---------------------')
print('Errores Sintácticos:')


print('Comienzo')
#  articulo = "Pelota
#  print("El artícuo es:", articulo)



print('\n\n---[Diapo 32]---------------------')
print('Errores Semánticos:')

numero = int(input("Ingrese un número:"))
division = 10 / numero
print("Resultado: ", division)




print('\n\n---[Diapo 33]---------------------')
print('Errores Semánticos controlados:')

numero = int(input("Ingrese un número:"))
if numero == 0:
    print("Error: no se puede ingresar un 0!")
else:
    division = 10 / numero
    print("Resultado: ", division)
