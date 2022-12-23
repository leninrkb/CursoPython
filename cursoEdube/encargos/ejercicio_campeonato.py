class Partido():
    def __init__(self):
        self.nombre = ''
        self.goles = 0

class Equipo():
    def __init__(self):
        self.partidos=[]
        self.nombre=''
        self.totalGoles=0

    def jugarPartidos(self):
        print('\nJugando partidos')
        mn = '# partidos a jugar el equipo '+self.nombre+': '
        n = int(input(mn))
        for i in range(n):
            p = Partido()
            p.nombre = 'part'+str((i+1))
            ms='goles del partido '+p.nombre+': '
            p.goles = int(input(ms))
            self.totalGoles+=p.goles
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
                    g = self.equipos[i].partidos[j]
        print('\n-- partido con mas goles: \npartido: ',g.nombre, ' goles: ',g.goles) 
        
    def mediaGolesPorEquipo(self):
        for i in range(len(self.equipos)):
            eq = self.equipos[i]
            media= round((eq.totalGoles/len(eq.partidos)),0)
            print('\n-- media de goles del equipo: ',eq.nombre,' es ',media)
            
    def ordernarPorGoles(self,eq):
        e = self.equipos
        for i in range(len(e)):
            if e[i].nombre == eq:
                ep = e[i].partidos
                for h in range(len(ep)-1):
                    for j in range(len(ep)-1):
                        if ep[j].goles > ep[j+1].goles:
                            aux = ep[j]
                            ep[j] = ep[j+1]
                            ep[j+1] = aux
                print('\n-- goles ordenados de ',eq,' :',)
                for h in range(len(ep)):
                    print('partido: ',ep[h].nombre,' goles: ',ep[h].goles)
        
        



j = Juego()
j.numeroEquipos(int(input('# equipos: ')))
j.verEquipos()
j.verPartidos()
j.mayorNumeroGolesPartido()
j.mediaGolesPorEquipo()
j.ordernarPorGoles('equipo3')

 
    
