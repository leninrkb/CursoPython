import random as rn
class Matriz():
    def __init__(self):
        self.m=[]
    def leerMatriz(self):
        f = int(input('dimension de la matriz: '))
        q = input('llenar matriz automaticamente? (y/n): ');
        if q.lower() == 'y':
            self.m = [[rn.randint(1,9) for j in range(f)] for i in range(f)]
        else:
            self.m = [[int(input(f'valor fila {i+1}: ')) for j in range(f)] for i in range(f)]
    def verMatriz(self):
        print(f'\nMatriz')
        for i in range(len(self.m)):
            for j in range(len(self.m)):
                print(f'{self.m[i][j]} ',end='')
            print()
        print()
    def verificarDiagonalFila(self):
        v=[]
        for columna in range(len(self.m)):
            if not self.m[0][columna]%2==0:
                v.append(self.m[0][columna])
        if len(self.m) == len(v):
            print(f'de la diagonal fila: {v} todos los elementos son impares')
        else:
            print(f'de la diagonal fila NO todos los elementos son impares')   
    def verificarDiagonalColumna(self):
        v=[]
        for fila in range(len(self.m)):
            if not self.m[fila][0]%2==0:
                v.append(self.m[fila][0])
        if len(self.m) == len(v):
            print(f'de la diagonal columna: {v} todos los elementos son impares')
        else:
            print(f'de la diagonal columna NO todos los elementos son impares')
    def verificarDiagonalPrincipal(self):
        v=[]
        for i in range(len(self.m)):
            if not self.m[i][i]%2==0:
                v.append(self.m[i][i])
        if len(self.m) == len(v):
            print(f'de la diagonal principal: {v} todos los elementos son impares')
        else:
            print(f'de la diagonal principal NO todos los elementos son impares')
                
        
m = Matriz()
m.leerMatriz()
m.verMatriz()
m.verificarDiagonalFila()
m.verificarDiagonalColumna()
m.verificarDiagonalPrincipal()