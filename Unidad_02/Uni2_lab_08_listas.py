# UNIDAD 01.D31

#LISTAS
print('\n\n---[Diapo 31.a]--------------')
print('Listas \n')

lista_numerica = [ 5, 10, 15, 20, 25]
lista_textos = ['Juan', 'Pedro', 'Antonio']
lista_mixta = [10, 'enero', 'abril', 25, 5.6]

print('Contenido de la lista numérica', lista_numerica)
print('Contenido de la lista de textos', lista_mixta)
print('Contenido de la lista mixta', lista_mixta)




# Listas - Accediendo a los elementos
print('\n\n---[Diapo 31.b]--------------')
print('Listas - Accediedon a los elementos \n')

lista = [5, 10, 15, 20, 25]
print('El primer elemento de la lista es:', lista[0])
print('El segundo elemento de la lista es: ', lista[1])
print('y el último es:', lista[-1])



# Sublistas
print('\n\n---[Diapo 31]--------------')
print('Sublistas \n')

lista = [5, 10, 15, 20, 25]
print('Los tres primeros elemento de la lista son:', lista[0:3])
print('Los tres primeros elemento de la lista son:', lista[:3])
print('Y los cuatro últimos:', lista[-4:])



# Listas - Elementos Mutables
print('\n\n---[Diapo 32]--------------')
print('Listas Mutables/Inmutables \n')
lista = [5, 10, 20, 30]
print('La lista inicial es:', lista)

lista[1] = 50
print('Luego del cambio:   ', lista)

var1 = 'prueba'
var1[5] = 'o'        ''' Error '''




