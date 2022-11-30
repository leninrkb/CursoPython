class Tablero():
    def __init__(self):
        self.mat=[]
        self.fila=0
        self.columna=0
    
    def ingreso(self):
        self.fila = int(input('valor fila: '))
        self.columna = int(input('valor columna: '))
        self.mat = [[input('posicion '+str(i)+'-'+str(j)+' numero: ') for i in range(self.fila)] for j in range(self.columna)]

    def menorCifraFila(self):
        fil=[]
        for i in range(self.columna):
            for j in range(self.fila):
                fil.append(self.mat[i][j])
            print('fila ',i,': ',len(max(fil,key=len)))
            del fil[:]


t = Tablero()
t.ingreso()
t.menorCifraFila()