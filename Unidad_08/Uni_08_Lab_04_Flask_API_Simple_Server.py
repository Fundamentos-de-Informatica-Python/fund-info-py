# UNIDAD 08.D32 - 34

# Para Probar en Postman:
#  GET http://localhost:6000/json
#  GET http://localhost:6000/texto

print('\n\n---[Diapo 32]---------------------')
print('Flask - Creando nu localhost:6000/jsonestra primer API')

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/json')
def saludoJson():
    return jsonify({'message': 'Hola!'})

@app.route('/texto')
def saludoTxt():
    return 'Hola!'


if __name__ == '__main__':
    app.run(debug=True, port=6000)

