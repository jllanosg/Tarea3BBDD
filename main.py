import json
from urllib import response
import flask
from sqlalchemy import false
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
    if canciones:
        response = jsonify(canciones.json())
        return response
    else:
        response = jsonify({'mensaje':'Mala sintaxis'})
        response.status_code = 400
        return response
#====================================================================================#
@app.route('/api/canciones/<id_cancion>', methods=['DELETE'])
def canciones_delete(id_cancion):
    canciones = Canciones.query.filter_by(id_cancion=id_cancion).first()
    if canciones:
        canciones.delete()
        return jsonify({'mensaje':'Cancion eliminada con exito'})
    else:
        response = jsonify({'mensaje':'No se encontró la canción'})
        response.status_code = 404
        return response
#====================================================================================#
@app.route('/api/canciones/<id_cancion>', methods=['PUT'])
def canciones_put(id_cancion):
    json = request.get_json()
    try:
        canciones = Canciones.query.filter_by(id_cancion=id_cancion).first_or_404()
    except:
        response = jsonify({'mensaje':'No se encontró la canción'})
        response.status_code = 404
        return response
    try:
        canciones.nombre = json['nombre']
        canciones.letra = json['letra']
        canciones.fecha_composicion = json['fecha_composicion']
        canciones.update()
        return jsonify(canciones.json())
    except:
        response = jsonify({'mensaje':'Mala sintaxis'})
        response.status_code = 400
        return response
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
    if personas:
        response = jsonify(personas.json())
        return response
    else:
        response = jsonify({'mensaje':'Mala sintaxis'})
        response.status_code = 400
        return response
#====================================================================================#
@app.route('/api/personas/<id_usuario>', methods=['DELETE'])
def personas_delete(id_usuario):
    personas = Personas.query.filter_by(id_usuario=id_usuario).first()
    if personas:
        personas.delete()
        return jsonify({'mensaje':'Persona eliminada con exito'})
    else:
        response = jsonify({'mensaje':'No se encontró al usuario'})
        response.status_code = 404
        return response
#====================================================================================#
@app.route('/api/personas/<id_usuario>', methods=['PUT'])
def personas_put(id_usuario):
    json = request.get_json()

    try:
        personas = Personas.query.filter_by(id_usuario=id_usuario).first_or_404()
    except:
        response = jsonify({'mensaje':'Usuario no encontrado.'})
        response.status_code = 404
        return response
    
    try:
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
    except:
        response = jsonify({'mensaje':'Mala sintaxis'})
        response.status_code = 400
        return response
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
    if facturas:
        response = jsonify(facturas.json())
        return response
    else:
        response = jsonify({'mensaje':'Mala sintaxis'})
        response.status_code = 400
        return response
#====================================================================================#
@app.route('/api/facturas/<id_factura>', methods=['DELETE'])
def facturas_delete(id_factura):
    factura = Facturas.query.filter_by(id_factura=id_factura).first()
    if factura:
        factura.delete()
        return jsonify({'mensaje':'Factura eliminada con exito'})
    else:
        response = jsonify({'mensaje':'No se encontró la factura'})
        response.status_code = 404
        return response
#====================================================================================#
@app.route('/api/facturas/<id_factura>', methods=['PUT'])
def facturas_put(id_factura):
    json = request.get_json()
    try:
        facturas = Facturas.query.filter_by(id_factura=id_factura).first_or_404()
    except:
        response = jsonify({'mensaje':'No se encontró la factura.'})
        response.status_code = 404
        return response
    try:
        facturas.monto_facturado = json['monto_facturado']
        facturas.fecha_facturacion = json['fecha_facturacion']
        facturas.fecha_vencimiento = json['fecha_vencimiento']
        facturas.estado = json['estado']
        facturas.metodo_de_pago = json['metodo_de_pago']
        facturas.fecha_hora_pago = json['fecha_hora_pago']
        facturas.id_usuario = json['id_usuario']
        facturas.update()
        response = jsonify(facturas.json())
        return response
    except:
        response = jsonify({'mensaje':'Mala sintaxis'})
        response.status_code = 400
        return response
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
    if reproducciones:
        response = jsonify(reproducciones.json())
        return response
    else:
        response = jsonify({'mensaje':'Mala sintaxis'})
        response.status_code = 400
        return response
#====================================================================================#
@app.route('/api/reproducciones/<id_cancion>/<id_usuario>', methods=['DELETE'])
def reproducciones_delete(id_cancion,id_usuario):
    reproducciones = Reproducciones.query.filter_by(id_cancion=id_cancion,id_usuario=id_usuario).first()
    if reproducciones:
        reproducciones.delete()
        return jsonify({'mensaje':'Reproducción eliminada con exito'})
    else:
        response = jsonify({'mensaje':'No se encontró la reproducción'})
        response.status_code = 404
        return response
#====================================================================================#
@app.route('/api/reproducciones/<id_cancion>/<id_usuario>', methods=['PUT'])
def reproducciones_put(id_cancion,id_usuario):
    json = request.get_json()
    try:
        reproducciones = Reproducciones.query.filter_by(id_cancion=id_cancion,id_usuario=id_usuario).first_or_404()
    except:
        response = jsonify({'mensaje':'No se encontró la reproducción'})
        response.status_code = 404
        return response
    try:
        reproducciones.cantidad_reproducciones = json['cantidad_reproducciones']
        reproducciones.ultima_reproduccion = json['ultima_reproduccion']
        reproducciones.update()
        return jsonify(reproducciones.json())
    except:
        response = jsonify({'mensaje':'Mala sintaxis'})
        response.status_code = 400
        return response
#====================================================================================#

#====================================================================================#
#=====================================MOROSO=========================================#
@app.route('/api/moroso/<id_usuario>', methods=['GET'])
def moroso(id_usuario):

    facturas = [factura.json() for factura in Facturas.query.filter_by(id_usuario=id_usuario)]
    today = date.today()
    if facturas != []:
        fac = []

        for factura in facturas:
            fecha = factura["fecha_vencimiento"]
            estado = factura["estado"]
            if (( fecha - today).days <0) and estado == false:
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
    else:
        response = { "mensaje": "El usuario no existe."}
        response = jsonify(response)
        response.status_code = 404
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
        estado = factura["estado"]
        if (( fecha - today).days <0) and estado == false:
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
@app.route('/api/topten/<id_usuario>', methods=['GET'])
def top_ten(id_usuario):
    canciones = [reproduccion.json() for reproduccion in Reproducciones.query.filter_by(id_usuario=id_usuario).order_by(Reproducciones.cantidad_reproducciones.desc()).limit(10).all()]
    return jsonify(canciones)

# Top 10 Global
@app.route('/api/toptenglobal', methods=['GET'])
def top_ten_global():
    # perdon me dio lata ponerlo en mas de una linea xd
    query = db.text("SELECT CANCIONES.NOMBRE,TOP.TOTAL_REPRODUCCIONES FROM CANCIONES INNER JOIN (SELECT ID_CANCION, SUM (CANTIDAD_REPRODUCCIONES) AS TOTAL_REPRODUCCIONES FROM REPRODUCCIONES GROUP BY ID_CANCION ORDER BY TOTAL_REPRODUCCIONES DESC LIMIT 10) AS TOP ON CANCIONES.ID_CANCION = TOP.ID_CANCION;")
    result = db.session.execute(query)
    response = [{"cancion":row[0],"reproducciones":row[1]} for row in result]
    return jsonify(response)

# ======================== STATS ========================  #
@app.route('/api/stats', methods=["GET"])
def stats():
    query1 = db.text("SELECT count(id_cancion) AS cantidad_canciones FROM canciones;")
    result1 = db.session.execute(query1)
    query2 = db.text("SELECT count(id_usuario) AS cantidad_usuarios FROM personas;")
    result2 = db.session.execute(query2)
    for row in result1:
        response = {"canciones": row[0]}
    for row in result2:
        response["usuarios"]=row[0]
    return jsonify(response)

if __name__ == "__main__":
    app.run(debug=True)