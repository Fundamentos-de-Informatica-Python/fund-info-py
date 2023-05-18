from flask import Flask, jsonify, request

from mod.persona import Persona

app = Flask(__name__)

productos = [
    {'Nombre': 'tensiometro', 'stock': 5},
    {'Nombre': 'termometro', 'stock': 20},
    {'Nombre': 'ibupofreno', 'stock': 500},
    {'Nombre': 'paracetamol', 'stock': 450},
]


@app.route('/')
def home():
    return 'Hola!'


@app.route('/holaPablo')
def saludarPablo():
    return 'Hola Pablo!'

@app.route('/saludar/<nombre>/<edad>', methods=['GET'])
def saludar(nombre, edad):
    my_persona = Persona(nombre, edad)
    return 'Hola ' + str(my_persona) + ' !'

@app.route('/productos', methods=['GET'])
def productosGet():
    return jsonify({'productos':productos, 'status':'ok' })


@app.route('/productos/<nombre>', methods=['GET'])
def productosGetUno(nombre):
    for indice, p in enumerate(productos):
        print('p: ', p)
        print('nombre:', nombre)
        if p['Nombre'] == nombre:
            return jsonify({'productos':productos[indice], 'status':'ok' })
    return 'error'


@app.route('/productos', methods=['POST'])
def productosPost():
    body = request.json
    print(body)
    nombre = body['Nombre']
    stock = body['stock']

    newProd = {'Nombre': nombre, 'stock': stock}
    productos.append(newProd)

    return jsonify({'productos':productos, 'status':'ok' })



@app.route('/productos/<nombre>/operacion/<op>', methods=['PUT'])
def productoPutUpdatePorPathString(nombre, op):
    for indice, p in enumerate(productos):
        if p['Nombre'] == nombre:
            if op == 'venta':
                p['stock'] = p['stock'] -1
            if op == 'compra':
                p['stock'] = p['stock'] +1

    return jsonify({'productos':productos, 'status':'ok' })



@app.route('/productos', methods=['PUT'])
def productoPutUpdatePorBody():

    body = request.json
    nombre = body['Nombre']
    stock = body['stock']

    for indice, p in enumerate(productos):
        if p['Nombre'] == nombre:
            p['stock'] = stock
    return jsonify({'productos': productos, 'status': 'ok'})


@app.route('/productos/<nombre>', methods=['DELETE'])
def productoDelete(nombre):
    for indice, p in enumerate(productos):
        if p['Nombre'] == nombre:
            productos[indice: indice+1] = []
    return jsonify({'productos': productos, 'status': 'ok'})





if __name__ == '__main__':
    app.run(debug=True, port=5000)
