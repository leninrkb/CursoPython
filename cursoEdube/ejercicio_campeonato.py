class Partido():
    def __init__(self):
        self.nombre = ''
        self.goles = 0

class Equipo():
    def __init__(self):
        self.partidos=[]
        self.nombre=''

    def jugarPartidos(self):
        print('\nJugando partidos')
        mn = '# partidos a jugar el equipo '+self.nombre+': '
        n = int(input(mn))
        for i in range(n):
            p = Partido()
            p.nombre = 'part'+str((i+1))
            ms='goles del partido'+p.nombre+': '
            p.goles = int(input(ms))
            self.partidos.append(p)


class Juego():
    def __init__(self):
        self.partidos=[]
        self.equipos=[]

    def numeroEquipos(self,n):
        for i in range(n):
            e = Equipo()
            e.nombre = 'equipo'+str((i+1))
            e.jugarPartidos()
            self.equipos.append(e)
            
    
    def verEquipos(self):
        print('\nEquipos: ')
        for i in range(len(self.equipos)):
            print(' - equipo:',self.equipos[i].nombre)

    def verPartidos(self):
        print('\nPartidos: ')
        for i in range(len(self.equipos)):
            print('\nequipo: ',self.equipos[i].nombre)
            for j in range(len(self.equipos[i].partidos)):
                p = self.equipos[i].partidos[j]
                print('partido: ',p.nombre,' goles: ',p.goles)

    def mayorNumeroGolesPartido(self):
        g = self.equipos[0].partidos[0]
        for i in range(len(self.equipos)):
            for j in range(len(self.equipos[i].partidos)):
                if self.equipos[i].partidos[j].goles >  g.goles:
                    g = self.equipos[i].partido[j]
        print('\npartido con mas goles: \npartido: ',g.nombre, ' goles: ',g.goles) 



j = Juego()
j.numeroEquipos(int(input('# equipos: ')))
j.verEquipos()
j.verPartidos()
j.mayorNumeroGolesPartido()

 
    
