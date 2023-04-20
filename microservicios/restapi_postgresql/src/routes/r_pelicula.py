from flask import Blueprint, jsonify
main = Blueprint('blueprint_pelicula',__name__)
#modelos
from models.m_pelicula import ModelPelicula



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