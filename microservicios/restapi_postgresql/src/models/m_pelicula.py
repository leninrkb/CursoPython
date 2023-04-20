from database.db import get_coneccion
from .entities.pelicula import Pelicula

class ModelPelicula:
    @classmethod
    def get_peliculas(self):
        try:
            coneccion = get_coneccion()
            peliculas = []
            with coneccion.cursor() as cursor:
                cursor.execute('select id, nombre, duracion, fecha_estreno from pelicula')  
                resultset = cursor.fetchall()       
                for i in resultset:     
                    pelicula = Pelicula(        
                        i[0],i[1],i[2],i[3]     
                    )
                    peliculas.append(pelicula.toJSON())
            coneccion.close()
            return peliculas
        except Exception as e:
            raise e