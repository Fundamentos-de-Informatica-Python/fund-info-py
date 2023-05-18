# academic-books

Forked from:
https://github.com/rs08ucema/fdi-academic-books

Créditos: Rodrigo Sellanes

# academic-books

Las importaciones de productos a la Argentina sigue siendo un tema complicado. Los usuarios que compran productos afuera utilizando plataformas internacionales, y a veces no están conformes con el trato ante un issue, lo cual sumado a las nuevos eventos a nivel global esto sucede mas a menudo. 

Notando esta oportunidad de negocio, y junto a un grupo de 3 socios de diferentes expertises decidimos realizar un startup para la importación de libros académicos. Con los avances de la tecnología y la demanda laboral, las universidades han tenido que adaptarse  rápidamente por lo cual han cambiado sus programas de estudio. El problema es que los alumnos tienen cierta dificultad para obtener los libros en el país, ya que la mayoría son impresos en Estados Unidos y Europa.

Como sabemos que los negocios digitales tienen la ventaja de ser rápidos y de bajo costo de implementación. Nuestro objetivo es crear una página web donde los usuarios (alumnos de la universidad) puedan encargar sus libros. Para emprender el negocio, realizamos la división de tareas, de la cual quedamos como responsable de desarrollar el Backend de la Web App.

Debemos cumplir con los siguientes features para nuestro MVP:

Desarrollar una API que cuente con los siguientes endpoints:
La URL Base de nuestra API será la siguiente: `<host>:<port>/api/academic-books/books`
* Método GET para obtener listado de los libros académicos, solo los siguientes atributos (ISBN, title, author, price). En el mismo endpoint definir un parámetro “language” opcional para filtrar por idioma (EN/ES) inglés o español. Si el parámetro está ausente devuelve la lista de todos los libros, y si el parámetro está presente, devuelve los que corresponden a “EN” o “ES”.
* Método GET para obtener la información completa de un libro específico por ISBN. Definir esto en el path.
* Método POST para crear una orden de compra de un libro seleccionado. El usuario lo definiremos como “user_id” y el valor será “univ_cema_9920”. El body request tendrá la misma estructura que “purchases_orders.json”. Vamos a suponer que solo este usuario es válido, por lo tanto si el valor de “user_id” es distinto, mostrar un mensaje de error al cliente con código de error HTTP 404.
* Importar el archivo “books.csv” provisto, el cual deberá ser leído y cargado al iniciar nuestro programa.
* Cuando un cliente realice una orden de compra, persistir esta información en un archivo llamado “purchases_orders.csv”. 

(Opcional): Desarrollar un endpoint con método GET que devuelve la lista de todas las órdenes de compra.

NOTA: Utilizar todo lo aprendido durante el curso. POO es mandatorio para diseñar la API.

### Ej: body response (GET lista)

```
[
	{
		"ISBN": "2348734",
		"title": "Python Crash Course",
		"author": "Eric Matthes",
		"price": 8400
	}
]

```

### Ej. body request (POST)
```
{
	"purchase_date": "20/05/2022",
	"ISBN": "2348734",
	"user_id": "univ_cema_9022",
	"full_address": "Av. Cordoba 423, CABA, Argentina"
}
```