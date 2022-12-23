import random as rn

class Departamento():
    def __init__(self):
        self.nombre=''
        self.costo=0
    def ingreso(self,n,c):
        self.nombre = n
        self.costo=c

class Tiempo():
    def __init__(self):
        self.deps=[]
        self.meses=12
        self.noms=['dep dulce','dep bebida','dep conservas']
    
    def mes(self,i):
        i+=1
        if i == 1: return '1  enero     '
        if i == 2: return '2  febrero   '
        if i == 3: return '3  marzo     '
        if i == 4: return '4  abril     '
        if i == 5: return '5  mayo      '
        if i == 6: return '6  junio     '
        if i == 7: return '7  julio     '
        if i == 8: return '8  agosto    '
        if i == 9: return '9  septiembre'
        if i == 10: return '10 octubre   '
        if i == 11: return '11 noviembre '
        if i == 12: return '12 diciembre '
        
    def ingresoDeps(self):
        q=input('ingresar datos automaticamente (y/n): ')
        if q.lower()=='y':
            for i in range(self.meses):
                dps=[]
                for n in self.noms:
                    ob = Departamento()
                    c=rn.randint(0,10)
                    ob.ingreso(n,c)
                    dps.append(ob)
                self.deps.append(dps.copy())
        else:
            for i in range(self.meses):
                dps=[]
                for n in self.noms:
                    ob = Departamento()
                    c = int(input(f'costo de produccion de {n} en el mes {self.mes(i)}: '))
                    ob.ingreso(n,c)
                    dps.append(ob)
                self.deps.append(dps.copy())
                print()
            
    def verTabla(self):
        for i in self.noms:
            print(f'{i:>16}',end=' / ')
        print()
        for i in range(self.meses):
            print(self.mes(i),end=' ')
            n=20
            for j in range(len(self.deps[i])):
                sp = n - len(self.mes(i))
                print(f'{self.deps[i][j].costo:{sp}}', end=' ')
            print()
    
    def mesMayorCostoDulces(self):
        x=0
        index=0
        for i in range(self.meses):
            y = self.deps[i][0].costo
            if y >= x:
                index=i
                x=y
        print(f'\n{self.mes(index)} tiene el mayor costo de producción de dulces')
        
    def mesMenorCostoBebidas(self):
        x=100
        index=0
        for i in range(self.meses):
            y = self.deps[i][1].costo
            if y <= x:
                index=i
                x=y
        print(f'{self.mes(index)} registro el menor costo de producción de bebidas')
    
    def mesMenorProduccionAgosto(self):
        x=100
        index=0
        for i in range(len(self.noms)):
            y = self.deps[7][i].costo
            if y <= x:
                index=i
                x=y
        print(f'{self.noms[index]} tuvo el menor costo de producción en Agosto')
    
    def promedioCostoAnualBebida(self):
        x=0
        for i in range(self.meses):
            x+= self.deps[i][1].costo
        x = x/self.meses
        print(f'Promedio anual de los costos de producción de bebidas = {round(x,2)}')


t = Tiempo()
t.ingresoDeps()
t.verTabla()
t.mesMayorCostoDulces()
t.promedioCostoAnualBebida()
t.mesMenorCostoBebidas()
t.mesMenorProduccionAgosto()