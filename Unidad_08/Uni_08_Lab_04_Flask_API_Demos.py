# UNIDAD 08.D32 - 34

# Flask - API - CRUD

print('\n\n---[Diapo 32]---------------------')
print('Flask - API - CRUD')

from flask import Flask

app = Flask(__name__)

if __name__ == '__main__':
    app.run(debug=True, port=4000)




print('\n\n---[Diapo 31]---------------------')
print('Flask - Creando nuestra primer API')

from flask import Flask

app = Flask(__name__)

@app.route('/')
def saludo():
    return 'Hola!'


if __name__ == '__main__':
    app.run(debug=True, port=5000)




print('\n\n---[Diapo 32]---------------------')
print('Flask - Creando nuestra primer API')

from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def saludo():
    return jsonify({'message', 'Hola!'})


if __name__ == '__main__':
    app.run(debug=True, port=6000)

