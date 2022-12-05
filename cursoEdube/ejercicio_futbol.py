# Se tiene una matriz en la que se guardan los 
# partidos ganados en cada mes del año por n equipos. Encontrar:

# 	¿Cuántos partidos gano cada equipo?
# 	¿Cuál es el mes que menos partidos ganados tiene?

class Equipo():
    def __init__(self):
        self.ganados=[]
        self.nombre=''
    def ingresarPartidos(self):
        print('\nIngreso datos:')
        for i in range(12):
            m = f'partidos ganados el {i+1} mes: '
            self.ganados.append(int(input(m)))
    def info(self):
        print(f'{self.nombre} tiene -> {self.ganados}')
    def totalGanados(self):
        print(f'total partidos ganados {self.nombre} -> {sum(self.ganados)}')
    def menosGanados(self):
        m = min(self.ganados)
        i = self.ganados.index(m)
        print(f'el equipo {self.nombre} ha ganado menos veces el mes {i+1}, con: {m}')
            
class Tabla():
    def __init__(self):
        self.equipos=[]
    def ingresarEquipos(self, n):
        for i in range(n):
            e = Equipo()
            e.nombre = f'equipo {i+1}'
            e.ingresarPartidos()
            self.equipos.append(e)
    def verEquipos(self):
        print('\n -- datos de cada equipo')
        [self.equipos[i].info() for i in range(len(self.equipos))]
    def partidosGanadosPorEquipo(self):
        print('\n -- total partidos ganados por equipo')
        [self.equipos[i].totalGanados() for i in range(len(self.equipos))]
    def mesMenosPartidosGanados(self):
        data = [0,(self.equipos[0].ganados[0]+1)**1000]
        for j in range(len(self.equipos[0].ganados)):
            k=0
            for i in range(len(self.equipos)):
                k+=self.equipos[i].ganados[j]               
            if k <= data[1]:
                data= [j,k]
        print(f'\n -- el mes {data[0]+1} es el que menos partidos ganados existe, con: {data[1]}')
    def menosGanadoPorEquipo(self):
        print('\n -- mes que menos ha ganado cada equipo')
        [self.equipos[i].menosGanados() for i in range(len(self.equipos))]
        
        
    


t = Tabla()
t.ingresarEquipos(int(input('numero de equipos a ingresar: ')))
t.verEquipos()
t.partidosGanadosPorEquipo()
t.mesMenosPartidosGanados()
t.menosGanadoPorEquipo()



