# UNIDAD 08.D20 - D26

# API - Consumiendo una API de terceros


print('\n\n---[Diapo 20]---------------------')
print('API - Consumiendo una API de terceros')

import requests
import decouple

My_NewsApi_KEY = decouple.config('My_NewsApi_KEY')

url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-04-10&sortBy=publishedAt&apiKey=' + My_NewsApi_KEY

response = requests.get(url)
status_code = response.status_code
if status_code == 200:
    content = response.content
    print('content: ', content)
else:
    print('Error en la solicitud')






print('\n\n---[Diapo 22]---------------------')
print('API - Consumiendo una API de terceros')

import requests
import decouple

My_NewsApi_KEY = decouple.config('My_NewsApi_KEY')

url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-04-10&sortBy=publishedAt&apiKey=' + My_NewsApi_KEY

response = requests.get(url)
status_code = response.status_code
if status_code == 200:
    json = response.json()
    print('tipo: ', type(json))
    print(json)
else:
    print('Error en la respuesta')



print('\n\n---[Diapo 24]---------------------')
print('API - Consumiendo una API de terceros')

import requests
import decouple

My_NewsApi_KEY = decouple.config('My_NewsApi_KEY')

url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-04-10&sortBy=publishedAt&apiKey=' + My_NewsApi_KEY

response = requests.get(url)
status_code = response.status_code
if status_code == 200:
    json = response.json()
    status = json['status']
    cantidadResultados = json['totalResults']
    print('Status: ', status)
    print('Cantidad noticias: ', cantidadResultados)
else:
    print('Error en la solicitud')





print('\n\n---[Diapo 25]---------------------')
print('API - Consumiendo una API de terceros')

import requests
import decouple

My_NewsApi_KEY = decouple.config('My_NewsApi_KEY')

url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-04-10&sortBy=publishedAt&apiKey=' + My_NewsApi_KEY

response = requests.get(url)
status_code = response.status_code
if status_code == 200:
    json = response.json()
    noticia = json['articles']
    cantidadResultados = json['totalResults']
    print('Type: ', type(noticia))
    print('Primera noticias ', noticia)
else:
    print('Error en la solicitud')






print('\n\n---[Diapo 26]---------------------')
print('API - Consumiendo una API de terceros')

import requests
import decouple

My_NewsApi_KEY = decouple.config('My_NewsApi_KEY')

url = 'https://newsapi.org/v2/everything?q=tesla&from=2022-04-10&sortBy=publishedAt&apiKey=' + My_NewsApi_KEY

response = requests.get(url)
status_code = response.status_code
if status_code == 200:
    json = response.json()
    noticia = json['articles'][0]
    fuente = noticia['source']
    autor = noticia['author']
    titulo = noticia['title']
    descripcion = noticia['description']
    url = noticia['url']
    print('Fuente: ', fuente)
    print('Autor: ', autor)
    print('Titulo: ', titulo)
    print('Descripcion: ', descripcion)
    print('url: ', url)
else:
    print('Error en la solicitud')
