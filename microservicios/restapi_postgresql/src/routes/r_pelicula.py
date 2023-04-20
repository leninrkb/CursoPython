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
        return jsonify({'error':str(e)}),500