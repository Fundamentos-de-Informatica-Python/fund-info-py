from flask import Flask,jsonify,request

from db_setup import create_table, save_data_inicial
from db_manager import  select_all_dietas, select_one_dieta, insert_one_dieta
from model import Restriction
from call_api_tercero import get_xr

app = Flask(__name__)

create_table()

# Home: Bienvenida a DreamFly!
@app.get('/')
def home():
    return 'Bienvenido a DreamFly!'


@app.get('/carga inicial')
def carga_inicial():
    save_data_inicial()
    return 'Data inicial cargado!'


@app.route('/api/dreamfly/dietas', methods = ['GET'])
def get_all_dietas():
    list_restrictions = select_all_dietas()
    return jsonify([restr.serialize() for restr in list_restrictions])


@app.route('/api/dreamfly/dietas/<restr_id>', methods = ['GET'])
def get_one_dietas(restr_id):
    restr = select_one_dieta(restr_id)
    return jsonify(restr.serialize())


@app.route('/api/dreamfly/dietas', methods = ['POST'])
def do_post():
    data = request.get_json()

    id = data['id']
    code = data['code']
    name_eng = data['name_eng']
    name_esp = data['name_esp']
    stock = data['stock']
    date = data['date']
    usd_value = data['usd_value']

    obj_restriction = Restriction(id, code, name_eng, name_esp, stock, date, usd_value)

    insert_one_dieta(obj_restriction)

    return jsonify(obj_restriction.serialize())




@app.route('/api/dreamfly/dietas/<restr_id>/pais/<pais>', methods = ['GET'])
def get_one_dietas_por_pais(restr_id, pais):
    restr = select_one_dieta(restr_id)

    if restr == []:
        return jsonify(status=400, description="Codigo de dieta no valido para (" + restr_id + ")"), 400


    texto_eng = restr.name_eng
    usd_value = int(restr.usd_value)
    rta = "The value of " + texto_eng + " is " + str(usd_value)

    if pais == 'ARG':
        texto_esp = restr.name_esp
        dolar = get_xr()
        ars_value = usd_value * dolar
        rta = "El valor de " + texto_esp + " es de " + str(ars_value)

    return jsonify(status=200, description=rta), 200




if __name__ == '__main__':
    app.run()
