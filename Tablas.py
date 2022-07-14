
from flask_sqlalchemy import SQLAlchemy
db = SQLAlchemy()

class Canciones(db.Model):
    _tablename_ = 'canciones'
    id_cancion = db.Column(db.Integer, primary_key=True)
    nombre = db.Column(db.String,nullable=False)
    letra = db.Column(db.String,nullable=True)
    fecha_composicion = db.Column(db.Date,nullable=True)

    classmethod
    def create(cls,nombre,letra.fecha_composicion):
        cancion = Canciones(nombre=nombre,letra=letra)
        return cancion.save()


class Personas(db.Model):
    _tablename_ = 'personas'
    id_usuario = db.Column(db.Integer,primary_key=True)
    nombre = db.Column(db.String(100),nullable=False)
    apellido = db.Column(db.String(80),nullable=True)
    email = db.Column(db.String(100),nullable=False)
    password = db.Column(db.String(100),nullable=False)
    usuario_suscripcion_activa = db.Column(db.Boolean)
    artista_nombre_artistico = db.Column(db.String(100))
    artista_verificado = db.Column(db.Boolean)
    tipo_de_persona = db.Column(db.Boolean,nullable=False)

class Reproducciones(db.Model):
    _tablename_='reproducciones'
    id_cancion = db.Column(db.Integer,db.ForeignKey("canciones.id_cancion"),primary_key=True)
    id_usuario = db.Column(db.Integer,db.ForeignKey("personas.id_usuario"),primary_key=True)
    cantidad_reproducciones = db.Column(db.Integer,nullable=True)
    ultima_reproduccion = db.Column(db.DateTime,nullable=True)

class Facturas(db.Model):
    _tablename_ = 'facturas'
    id_factura = db.Column(db.Integer,primary_key=True)
    monto_facturado = db.Column(db.Integer)
    fecha_facturacion = db.Column(db.Date)
    fecha_vencimiento = db.Column(db.Date)
    estado = db.Column(db.Boolean)
    metodo_de_pago = db.Column(db.String(100))
    fecha_hora_pago = db.Column(db.DateTime)
    id_usuario = db.Column(db.Integer,db.ForeignKey("personas.id_usuario"))
