from flask import Flask, jsonify
from flask_cors import CORS
from database import db

app = Flask(__name__)
CORS(app)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:''@localhost/dashdiner'


@app.route('/')
def home():
    return jsonify('hola mundo')


def main():
    db.init_app(app)

    # antes de correr la aplicacion, se debe crear la base de datos
    # correr el comando en mysql:
    # create database dashdiner;
    with app.app_context():
        db.create_all()
    app.run()

# GET all restaurantes


@app.route('/api/restaurantes', methods=['GET'])
def get_all_restaurant():
    restaurante = Restaurante.query.all()
    resultado = [{"id": r.id, "nombre": r.nombre} for r in restaurante]
    return jsonify(resultado)

# GET all restaurantes por id


@app.route('/api/restaurantes/<int:id>', methods=['GET'])
def get_restaurante_by_id(id):
    sql = ""
    restaurante = Restaurante.query.get(id)
    if restaurante is None:
        return jsonify({"message": "Restaurante no encontrado"}), 404
    return jsonify({"id": restaurante.id, "nombre": restaurante.nombre})

# GET producto


@app.route('/api/productos', methods=['GET'])
def get_all_producto():
    producto = Producto.query.all()
    resultado = [{"id": p.id, "nombre": p.nombre} for p in producto]
    return jsonify(resultado)

# GET producto by id


@app.route('/api/productos/<int:id>', methods=['GET'])
def get_producto_by_id(id):
    producto = Producto.query.get(id)
    if producto is None:
        return jsonify({"message": "Producto no encontrado"}), 404
    return jsonify({"id": producto.id, "nombre": producto.nombre})


if __name__ == "__main__":
    main()
