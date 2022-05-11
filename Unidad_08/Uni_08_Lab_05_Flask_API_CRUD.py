# UNIDAD 08.D32 Creando nuestra primer API

# Flask - Creando nuestra primer API

print('\n\n---[Diapo 32 y 34]---------------------')
print('Flask - Creando nuestra primer API')

from flask import Flask, jsonify, request

app = Flask(__name__)


productos = [
    {'Nombre': 'tensiometro', 'stock': 5},
    {'Nombre': 'termometro', 'stock': 20},
    {'Nombre': 'ibupofreno', 'stock': 500},
    {'Nombre': 'paracetamol', 'stock': 450},
]


@app.route('/')
def saludo():
    return jsonify({'message', 'Hola!'})


#
# D.35: [GET] Consultando información de todos los productos
#
@app.route('/productos', methods=['GET'])
def productos():
    return jsonify({'productos':productos, 'status':'ok' })

#
# D.37: [GET] Consultando información de un único producto
#
@app.route('/productos/<producto>', methods=['GET'])
def productoGet(producto):
    for p in productos:
        if p['nombre'] == producto:
            return jsonify({'producto':producto[0], 'busqueda':producto, 'status':'ok'})
    return jsonify({'productos':productos, 'status':'nof found' })


#
# D.39: [POST] Dando de alta un nuevo producto
#
@app.route('/productos', methods=['POST'])
def productoPost():
    body = request.json
    nombre = body['nombre']
    stock  = body['stock']
    productoAlta = {'Nombre': nombre, 'stock': stock},
    return jsonify({'productos':productos, 'status':'ok' })

#
# D.42: [PUT] Actualiza un Producto
#             - busca por el nombre
#             - y actualiza el stock
#
@app.route('/productos', methods=['PUT'])
def productoPut(producto):
    body = request.json
    nombre = body['nombre']
    stock  = body['stock']
    for p in productos:
        if p['nombre'] == nombre:
            p['stock'] = stock
            return jsonify({'producto':p,
                            'busqueda': producto,
                            'status': 'ok'})

    return jsonify({'busqueda':productos,
                    'status':'not found' })



#
# D.37: [DELETE] Consultando información de un único producto
#
@app.route('/productos/<producto>', methods=['DELETE'])
def productoDelete(producto):
    for indice, p in enumerate(productos):
        if p['nombre'] == producto:

            # TODO: Eliminarlo de la base de datos
            # productos[indice] = 0
            productos[indice:indice+1] = []
            return jsonify({'producto':p, 'busqueda':producto, 'status':'ok'})
    return jsonify({'productos':productos, 'status':'nof found' })




if __name__ == '__main__':
    app.run(debug=True, port=6000)

