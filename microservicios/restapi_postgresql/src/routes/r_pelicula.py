from flask import Blueprint, jsonify, request
import uuid
main = Blueprint('blueprint_pelicula',__name__)
#modelos
from models.m_pelicula import ModelPelicula
from models.entities.pelicula import Pelicula



@main.route('/')
def get_peliculas():
    try:
        peliculas = ModelPelicula.get_peliculas()
        return jsonify(peliculas)
    except Exception as e:
        return jsonify({'error get_peliculas':str(e)}),500
    
@main.route('/<id>')
def get_pelicula(id):
    try:
        pelicula = ModelPelicula.get_pelicula(id)
        if pelicula != None:
            return pelicula
        else:
            return jsonify({}),404
    except Exception as e:
        return jsonify({'error get_pelicula':str(e)}),500

@main.route('/add',methods=['post'])
def add_pelicula():
    try:
        #validar datos
        id = str(uuid.uuid4())
        nombre = request.json['nombre']
        duracion = request.json['duracion']
        fecha_estreno = request.json['fecha_estreno']
        pelicula = Pelicula(id, nombre, duracion, fecha_estreno)
        filas_afectadas = ModelPelicula.add_pelicula(pelicula)
        return jsonify({"mensaje":filas_afectadas}),500
    except Exception as e:
        return jsonify({'error add_pelicula':str(e)}),500 

@main.route('/del/<id>',methods=['delete'])
def del_pelicula(id):
    try:
        #validar datos
        filas_afectadas = ModelPelicula.del_pelicula(id)
        if filas_afectadas == 1:
            return jsonify({"mensaje":filas_afectadas}),200
        return jsonify({"mensaje":"no se ejecuto"}),404
    except Exception as e:
        return jsonify({'error del_pelicula':str(e)}),500 

@main.route('/update',methods=['put'])
def update_pelicula():
    try:
        #validar datos
        id = request.json['id']
        nombre = request.json['nombre']
        duracion = request.json['duracion']
        fecha_estreno = request.json['fecha_estreno']
        pelicula = Pelicula(id, nombre, duracion, fecha_estreno)
        filas_afectadas = ModelPelicula.update_pelicula(pelicula)
        if filas_afectadas == 1:
            return jsonify({"mensaje":filas_afectadas}),200
        return jsonify({"mensaje":"no se ejecuto"}),404
    except Exception as e:
        return jsonify({'error update_pelicula':str(e)}),500