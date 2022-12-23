import random as rn
class Matriz():
    def __init__(self):
        self.m=[]
    def leerMatriz(self):
        n = int(input('dimension de la matriz: '))
        q = input('llenar matriz automaticamente? (y/n): ');
        if q.lower() == 'y':
            self.m = [[rn.randint(0,9) for j in range(n)] for i in range(n)]
        else:
            self.m = [[int(input(f'valor fila {i+1}: ')) for j in range(n)] for i in range(n)]        
    def identificarMatriz(self):
        traspuesta = [[self.m[j][i] for j in range(len(self.m))] for i in range(len(self.m))]
        self.verMatriz(self.m,'original')
        self.verMatriz(traspuesta,'traspuesta')
        if self.m == traspuesta:
            print(f'la matriz SI es simetrica')
        else:
            print(f'la matriz NO es simetrica')
    def verMatriz(self,m, mn):
        print(f'\n{mn.upper()}')
        for i in range(len(m)):
            for j in range(len(m[0])):
                print(f'{m[i][j]} ',end='')
            print()
        print()
m = Matriz()
m.leerMatriz()
m.identificarMatriz()