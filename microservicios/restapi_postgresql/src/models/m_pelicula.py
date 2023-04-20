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
    @classmethod
    def get_pelicula(self,id):
        try:
            coneccion = get_coneccion()
            with coneccion.cursor() as cursor:
                cursor.execute(f'select id, nombre, duracion, fecha_estreno from pelicula where id = %s',(id,))  
                result = cursor.fetchone()     
                if result != None:
                    pelicula = Pelicula(
                        result[0],result[1],result[2],result[3],
                    )
                    pelicula = pelicula.toJSON()
            coneccion.close()
            return pelicula
        except Exception as e:
            raise e