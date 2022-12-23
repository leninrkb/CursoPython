import random as rn
class Estudiante():
    def __init__(self):
        self.m=[]
        self.promedios=[]
    def leerMatriz(self):
        columna = int(input('cantidad de alumnos: '))
        fila = int(input('cantidad de examenes: '))
        q = input('llenar matriz automaticamente? (y/n): ');
        if q.lower() == 'y':
            self.m = [[rn.randint(10,99) for j in range(columna)] for i in range(fila)]
        else:
            self.m = [[int(input(f'nota estudiante #{j+1} en examen {i+1}: ')) for j in range(columna)] for i in range(fila)]  
        self.verMatriz(self.m,'calificaciones')
    def verMatriz(self,m, mn):
        print(f'\n{mn.upper()}')
        print(f'#stds: ',end='')
        for i in range(len(self.m[0])):
            print(f'{"e"+str(i+1):>5}',end='')
        print()
        for i in range(len(m)):
            print(f'examen {i+1}',end=': ')
            for j in range(len(m[0])):
                print(f'{m[i][j]}   ',end='')
            print()
        print()
    def calcularPromedios(self):
        promedios=[]
        for columna in range(len(self.m[0])):
            s=0
            for fila in range(len(self.m)):
                s += self.m[fila][columna]
            promedios.append(round(s/len(self.m),2))
            self.promedios = promedios
        print(f'Promedios de los estuaintes: {promedios}')
    def calcularPromedioGrupo(self,n):
        if n > len(self.m):
            n = len(self.m)
        promedio=0
        s=0
        for columna in range(len(self.m[0])):
            s += self.m[n-1][columna]
        promedio = round(s/len(self.m[0]),2)
        print(f'Promedio del grupo en examen {n}: {promedio}')
    def calcularMayorPromedio(self):
        mayor=0
        ind=0
        for i in range(len(self.promedios)):
            if self.promedios[i] > mayor:
                mayor = self.promedios[i]
                ind=i
        print(f'El estudiante No.{ind+1} obtuvo el mayor promedio: {mayor}')
    def definirAprobadosReprovados(self):
        ap=[]
        re=[]
        for i in range(len(self.promedios)):
            if self.promedios[i] >= 70:
                ap.append(self.promedios[i])
            else:
                re.append(self.promedios[i])
        print(f'Total aprobados: {len(ap)},  Total reprovados: {len(re)}')
    def reprobadosPorExamen(self,n):
        if n > len(self.m):
            n = len(self.m)
        re=[]
        for columna in range(len(self.m[0])):
            if self.m[n-1][columna] < 70:
                re.append(self.m[n-1][columna])  
        
        print(f'{len(re)} estudiantes reprobaron el examen {n}')
                
            
e=Estudiante()
e.leerMatriz()
e.calcularPromedios()
e.calcularPromedioGrupo(3)#numero de examen
e.calcularMayorPromedio()
e.definirAprobadosReprovados()
e.reprobadosPorExamen(1)