Storing local env variables

pip install python-decouple

touch .env 

My_NewsApi_KEY = 'dd502979669640......'

Add .env to
.gitignore

------------------


sudo pip install flask



------------------



*********************************
POST

▶ curl -X GET http://127.0.0.1:6000/productos/
▶ curl -X GET http://127.0.0.1:6000/productos/termometro

▶ curl -X GET http://127.0.0.1:6000/productos/aspirina

▶ curl -X POST -d  '{"Nombre": "aspirina", "stock": 25}' -H "Content-Type: application/json"  http://127.0.0.1:6000/productos 

▶ curl -X GET http://127.0.0.1:6000/productos/aspirina

▶ curl -X GET    http://127.0.0.1:6000/productos/aspirina
▶ curl -X DELETE http://127.0.0.1:6000/productos/aspirina
▶ curl -X GET    http://127.0.0.1:6000/productos/aspirina
