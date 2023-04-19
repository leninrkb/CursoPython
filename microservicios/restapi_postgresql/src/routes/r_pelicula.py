from flask import Blueprint, jsonify
main = Blueprint('blueprint_pelicula',__name__)

@main.route('/')
def get_peliculas():
    return jsonify({'saludo':'hola! esta es la raiz de la api'})