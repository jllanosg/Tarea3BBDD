import json
import flask
from Config import config
from Tablas import*
from flask_cors import CORS
from flask import jsonify, request
from datetime import date

app = flask.Flask(__name__)
app.config["DEBUG"] = True



def create_app(enviroment):
    app = flask.Flask(__name__)
    app.config["JSON_ASK_ASCII"] = False
    app.config.from_object(enviroment)
    with app.app_context():
        db.init_app(app)
        db.create_all()
    return app


enviroment = config["development"]
app = create_app(enviroment)
#=====================================CANCIONES======================================#
@app.route('/api/canciones', methods=['GET'])
def canciones_select():
    canciones = [cancion.json() for cancion in Canciones.query.all()]
    response = jsonify(canciones)
    return response
#====================================================================================#
@app.route('/api/canciones', methods=['POST'])
def canciones_insert():
    json = request.get_json()
    canciones = Canciones.create(json['nombre'],json['letra'],json['fecha_composicion'])
    response = jsonify(canciones.json())
    return response
#====================================================================================#
@app.route('/api/canciones/<id_cancion>', methods=['DELETE'])
def canciones_delete(id_cancion):
    canciones = Canciones.query.filter_by(id_cancion=id_cancion).first()
    canciones.delete()
    return jsonify({'mensaje':'Cancion eliminada con exito'})
#====================================================================================#
@app.route('/api/canciones/<id_cancion>', methods=['PUT'])
def canciones_put(id_cancion):
    json = request.get_json()
    canciones = Canciones.query.filter_by(id_cancion=id_cancion).first()
    canciones.nombre = json['nombre']
    canciones.letra = json['letra']
    canciones.fecha_composicion = json['fecha_composicion']
    canciones.update()
    return jsonify(canciones.json())
#====================================================================================#
#=====================================PERSONAS=======================================#
@app.route('/api/personas', methods=['GET'])
def personas_select():
    personas = [persona.json() for persona in Personas.query.all()]
    response = jsonify(personas)
    return response
#====================================================================================#
@app.route('/api/personas', methods=['POST'])
def personas_insert():
    json = request.get_json()
    personas = Personas.create(json['nombre'],json['apellido'],json['email'],json['password'],json['usuario_suscripcion_activa'],json['artista_nombre_artistico'],json['artista_verificado'],json['tipo_de_persona'])
    response = jsonify(personas.json())
    response.status_code=200
    return response
#====================================================================================#
@app.route('/api/personas/<id_usuario>', methods=['DELETE'])
def personas_delete(id_usuario):
    personas = Personas.query.filter_by(id_usuario=id_usuario).first()
    personas.delete()
    return jsonify({'mensaje':'Usuario eliminada con exito'})
#====================================================================================#
@app.route('/api/personas/<id_usuario>', methods=['PUT'])
def personas_put(id_usuario):
    json = request.get_json()
    personas = Personas.query.filter_by(id_usuario=id_usuario).first()
    personas.nombre = json['nombre']
    personas.apellido = json['apellido']
    personas.email = json['email']
    personas.password = json['password']
    personas.usuario_suscripcion_activa = json['usuario_suscripcion_activa']
    personas.artista_nombre_artistico = json['artista_nombre_artistico']
    personas.artista_verificado = json['artista_verificado']
    personas.tipo_de_persona = json['tipo_de_persona']
    personas.update()
    return jsonify(personas.json())
#====================================================================================#
#=====================================FACTURAS=======================================#
@app.route('/api/facturas', methods=['GET'])
def facturas_select():
    facturas = [factura.json() for factura in Facturas.query.all()]
    response = jsonify(facturas)
    return response
#====================================================================================#
@app.route('/api/facturas', methods=['POST'])
def facturas_insert():
    json = request.get_json()
    facturas = Facturas.create(json['monto_facturado'],json['fecha_facturacion'],json['fecha_vencimiento'],json['estado'],json['metodo_de_pago'],json['fecha_hora_pago'],json['id_usuario'])
    response = jsonify(facturas.json())
    return response
#====================================================================================#
@app.route('/api/facturas/<id_factura>', methods=['DELETE'])
def facturas_delete(id_factura):
    factura = Facturas.query.filter_by(id_factura=id_factura).first()
    factura.delete()
    return jsonify({'mensaje':'Factura eliminada con exito'})
#====================================================================================#
@app.route('/api/facturas/<id_factura>', methods=['PUT'])
def facturas_put(id_factura):
    json = request.get_json()
    facturas = Facturas.query.filter_by(id_factura=id_factura).first()
    facturas.monto_facturado = json['monto_facturado']
    facturas.fecha_facturacion = json['fecha_facturacion']
    facturas.fecha_vencimiento = json['fecha_vencimiento']
    facturas.estado = json['estado']
    facturas.metodo_de_pago = json['metodo_de_pago']
    facturas.fecha_hora_pago = json['fecha_hora_pago']
    facturas.id_usuario = json['id_usuario']
    facturas.update()
    return jsonify(facturas.json())
#====================================================================================#
#=====================================REPRODUCCIONES=================================#
@app.route('/api/reproducciones', methods=['GET'])
def reproducciones_select():
    reproducciones = [reproduccion.json() for reproduccion in Reproducciones.query.all()]
    response = jsonify(reproducciones)
    return response
#====================================================================================#
@app.route('/api/reproducciones', methods=['POST'])
def reproducciones_insert():
    json = request.get_json()
    reproducciones = Reproducciones.create(json['id_cancion'],json['id_usuario'],json['cantidad_reproducciones'],json['ultima_reproduccion'])
    response = jsonify(reproducciones.json())
    return response
#====================================================================================#
@app.route('/api/reproducciones/<id_cancion>/<id_usuario>', methods=['DELETE'])
def reproducciones_delete(id_cancion,id_usuario):
    reproducciones = Reproducciones.query.filter_by(id_cancion=id_cancion,id_usuario=id_usuario).first()
    reproducciones.delete()
    return jsonify({'mensaje':'Cancion eliminada con exito'})
#====================================================================================#
@app.route('/api/reproducciones/<id_cancion>/<id_usuario>', methods=['PUT'])
def reproducciones_put(id_cancion,id_usuario):
    json = request.get_json()
    reproducciones = Reproducciones.query.filter_by(id_cancion=id_cancion,id_usuario=id_usuario).first()
    reproducciones.cantidad_reproducciones = json['cantidad_reproducciones']
    reproducciones.ultima_reproduccion = json['ultima_reproduccion']
    reproducciones.update()
    return jsonify(reproducciones.json())
#====================================================================================#

#====================================================================================#
#=====================================MOROSO=========================================#
@app.route('/api/moroso/<id_usuario>', methods=['GET'])
def moroso(id_usuario):
    facturas = [factura.json() for factura in Facturas.query.filter_by(id_usuario=id_usuario)]

    today = date.today()

    fac = []

    for factura in facturas:
        fecha = factura["fecha_vencimiento"]
        if (( fecha - today).days <0):
            fac.append(factura)

    if (fac==[]):
        mensaje="El usuario no tiene facturas vencidas."
    else:
        mensaje="El usuario tiene facturas vencidas."


    response= {
        "mensaje": mensaje,
        "facturas": fac
    }
    response = jsonify(response)
    return response

#====================================================================================#
#=================================PERSONAS MOROSAS===================================#
@app.route('/api/morosos', methods=['GET'])
def morosos():
    facturas = [factura.json() for factura in Facturas.query.all()]
    today = date.today()

    # Se guardan las id's de las morosas, para contar qty_personas
    ids_facturas_morosas=[]
    platita=0
    for factura in facturas:
        fecha = factura["fecha_vencimiento"]
        if (( fecha - today).days <0):
            platita+=factura["monto_facturado"]
            if factura["id_usuario"] not in ids_facturas_morosas:
                ids_facturas_morosas.append(factura["id_usuario"])

    response = {
        "qty_personas": len(ids_facturas_morosas),
        "qty_dinero": platita
    }
    return jsonify(response)
#====================================================================================#
#===================================STONKS===========================================#
@app.route('/api/stonks', methods=['GET'])
def stonks():
    facturas = [factura.json() for factura in Facturas.query.all()]
    today = date.today()
    platita=0
    for factura in facturas:
        fecha = factura["fecha_hora_pago"]
        if (fecha and ( today - fecha.date() ).days <=31):
            platita+=factura["monto_facturado"]
    response = {
        "qty_dinero": platita
    }
    return jsonify(response)

#====================================================================================#
#===================================TOP10============================================#
''' WORK IN PROGRESS XD
@app.route('/api/topten/<id_usuario>', methods=['GET'])
def top_ten(id_usuario):
    canciones = Reproducciones.query.filter_by(id_usuario=id_usuario).order_by(desc(model.Entry.amount))
'''
if __name__ == "__main__":
    app.run(debug=True)