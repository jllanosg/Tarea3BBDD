import flask
from Config import config
from Tablas import db
from flask_cors import CORS
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

@app.route('/', methods=['GET'])
def home():
    return "<h1>Mi primera API :P</h1>"




if __name__ == "__main__":
    app.run(debug=True)