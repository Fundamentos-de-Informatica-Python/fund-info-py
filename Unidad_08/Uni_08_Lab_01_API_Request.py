# UNIDAD 08.D17 - D19

# API - Ejecutando un Request


print('\n\n---[Diapo 17]---------------------')
print('API - Ejecutando un request desde Python')

import requests
url = 'http://www.google.com'

response = requests.get(url)
print('Respuesta: ', response)
print('Tipo: ', type(response))


print('\n\n---[Diapo 18]---------------------')
print('API - Ejecutando un request desde Python')

import requests
url = 'http://www.google.com'

response = requests.get(url)
print('Respuesta: ', response)
print('Tipo: ', type(response))
print('Status Code: ', response.status_code)



print('\n\n---[Diapo 19]---------------------')
print('API - Ejecutando un request desde Python')

import requests
url = 'http://www.google.com'

response = requests.get(url)
status_code = response.status_code
if status_code == 200:
    content = response.content
    print('content: ', content)
else:
    print('Error en la solicitud')



