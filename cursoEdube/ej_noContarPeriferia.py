import random as rn

class Matriz():
    def __init__(self):
        self.m=[]
    
    def ingresoMatriz(self):
        f = int(input('ingrese las filas: '))
        c = int(input('ingrese las columnas: '))
        if self.comprobarMinimo(f,c):
            q=input('llenar matriz automaticamente? (y/n): ')
            if q.lower() == 'y':
                self.m = [[rn.randint(1,9) for columnas in range(c)] for filas in range(f)]
            else: 
                self.m = [[int(input(f'fila-{filas},columna-{columnas}: ')) for columnas in range(c)] for filas in range(f)]
            self.verMatriz()
            return True
        else:
            print('dimensiones minimas 3x3!')
        return False
    
    def verMatriz(self):
        print('Matriz ingresada: ')
        for fila in range(len(self.m)):
            for columna in range(len(self.m[0])):
                print(self.m[fila][columna], end=' ')
            print()
        
    def comprobarMinimo(self,f,c):
        if f < 3 or c < 3:
            return False
        return True

    def sumarElementos(self):
        s=0
        if self.ingresoMatriz():
            print('\nsumando: ',end='')
            for fila in range(1,len(self.m)-1):
                for columna in range(1,len(self.m[0])-1):
                    print(f'{self.m[fila][columna]}',end=' + ')
                    s+=self.m[fila][columna]
        print(f'\nsumatoria = {s}')
                    

mat = Matriz()
mat.sumarElementos()