# UNIDAD 08.D27

# API - Integrando los parámetros en el llamado


print('\n\n---[Diapo 27]---------------------')
print('API - Consumiendo una API de terceros')

import requests
import decouple

My_NewsApi_KEY = decouple.config('My_NewsApi_KEY')

url = 'https://newsapi.org/v2/top-headlines'
args = {
    'country' : 'ar',
    'apiKey' : 'dd5029796696402ca5941ff5a70e3fb0'
}

response = requests.get(url, params=args)

cantResultados = response.json()['totalResults']

print('Cantidad de noticias: ', cantResultados)