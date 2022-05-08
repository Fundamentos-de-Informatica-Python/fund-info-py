# UNIDAD 06.D35

# Programación Orientada a Objetos (POO) 


print('\n\n---[Diapo 35]---------------------')
print("Objetos como Parámetros")


class Articulo:
    precio = 10

def aumentar(art):
    art.precio = art.precio * 2

articulo = Articulo()
print("Precio Original:", articulo.precio)

aumentar(articulo)
print("Precio Nuevo:", articulo.precio)
