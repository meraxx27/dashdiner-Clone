from colorama import Cursor
from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

app = Flask(__name__)
# Sustituir por las credenciales del servidor
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:Themeraxx@localhost/dashdiner'
db = SQLAlchemy(app)
CORS(app)

# GET all restaurantes


@app.route('/api/restaurantes', methods=['GET'])
def get_all_restaurant():
    restaurante = Restaurante.query.all()
    resultado = [{"id": r.id, "nombre": r.nombre} for r in restaurante]
    return jsonify(resultado)

# GET all restaurantes por id


@app.route('/api/restaurantes/<int:id>', methods=['GET'])
def get_restaurante_by_id(id):
    query = "SELECT * FROM restaurante WHERE id = %s"
    Cursor.execute(query, (elemento_id,))
    elemento_encontrado = cursor.fetchone()

    if elemento_encontrado:
        return jsonify(elemento_encontrado)
    else:
        return jsonify({"mensaje": "Elemento no encontrado"}), 404

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
