# Variables Booleanas [Diapo 36]


print('\n-----------------------------')
print('Variables Booleanas [Diapo 36] \n')

aprobado = True
print('El alumno aprobó el examen: ', aprobado)

aprobado = False
print('El alumno aprobó el examen: ', aprobado)

print('\n-----------------------------')
print('Operadores Relacionales [Diapo 38] \n')

var = 25
print('La variable es igual a 25: ', var == 25)
print('La variable es distinta a 25: ', var != 25)
print('La variable es mayor a 20: ', var > 20)
print('La variable es menor a 20: ', var < 20)
print('La variable es mayor o igual a 30: ', var >= 30)
print('La variable es menor o igual a 30: ', var <= 30)

print('\n-----------------------------')
print('Operadores Lógicos [Diapo 39] AND \n')

var1 = 5
var2 = 10

print('var1 es igual a 5 y var2 es igual a 10 = ', var1 == 5 and var2 == 10)
print('var1 es igual a 5 y var2 es igual a 15 = ', var1 == 5 and var2 == 15)
print('var1 es igual a 1 y var2 es igual a 10 = ', var1 == 1 and var2 == 10)
print('var1 es igual a 1 y var2 es igual a 2 = ',  var1 == 1 and var2 == 2)



print('\n-----------------------------')
print('Operadores Lógicos [Diapo 39] OR \n')

var1 = 5
var2 = 10

print('var1 es igual a 5 ó var2 es igual a 10 = ', var1 == 5 or var2 == 10)
print('var1 es igual a 5 ó var2 es igual a 15 = ', var1 == 5 or var2 == 15)
print('var1 es igual a 1 ó var2 es igual a 10 = ', var1 == 1 or var2 == 10)
print('var1 es igual a 1 ó var2 es igual a 2 = ',  var1 == 1 or var2 == 2)


print('\n-----------------------------')
print('Operadores Lógicos [Diapo 39] NOT \n')

var1 = 5

print('var1 NO es igual a 5: ', not var1 == 5)
print('var1 NO es igual a 7: ', not var1 == 7)
