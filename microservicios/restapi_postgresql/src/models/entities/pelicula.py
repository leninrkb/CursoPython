from utils.DateFormat import DateFormat
class Pelicula:
    def __init__(self, id, nombre=None, duracion=None, fecha_estreno=None):
      self.id = id
      self.nombre = nombre
      self.duracion = duracion
      self.fecha_estreno = fecha_estreno
    def toJSON(self):
        return {
            'id' : self.id,
            'nombre' : self.nombre,
            'duracion' : self.duracion,
            'fecha_estreno' : DateFormat.date2ymd(self.fecha_estreno)
        }