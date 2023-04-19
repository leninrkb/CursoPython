from flask import Flask
from config import config
#rutas
from routes import r_pelicula

def pagina_no_encontrada(error):
    return '<h1>Pagina no funcionar, hombre triste :(</h1>',404

app = Flask(__name__)
if __name__ == '__main__':
    app.config.from_object(config['development'])
    # blueprint
    app.register_blueprint(r_pelicula.main,url_prefix='/api/peliculas')
    # soporte de errores
    app.register_error_handler(404,pagina_no_encontrada)
    app.run()