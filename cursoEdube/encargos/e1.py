import statistics

# utils
def pedirBulto():
    b = float(input("ingrese el peso del bulto en kg: "))
    if b <= 0:
        print('peso no valido')
        return None
    return b

def confirmar():
    return input('desea ingresar otro bulto? s/n: ')


# objetos
class Boing():
    capMax=18000
    bultos=[]
    pesoMaxBulto=500
    totalIngresos=0

    def noExcedePesoTotal(self):
        if sum(self.bultos) < self.capMax:
            return True
        return False

    def espacioDisponible(self):
        return self.capMax - sum(self.bultos)

    def valorPorKg(self,bulto):
        if bulto > -1 and bulto <= 25:
            self.totalIngresos += (bulto * 0)
            return
        if bulto > 25 and bulto <= 300:
            self.totalIngresos += (bulto * 7.5)
            return
        if bulto > 300 and bulto <= 500:
            self.totalIngresos += (bulto * 8.45)
            return

    def agregarBulto(self,bulto):
        if self.noExcedePesoTotal():
            if bulto <= self.espacioDisponible():
                if bulto <= self.pesoMaxBulto:
                    self.valorPorKg(bulto)
                    self.bultos.append(bulto)
                    print('bulto ingresado')
                    return True
                else:
                    print('el bulto exce el peso maximo =',self.pesoMaxBulto)
            else:
                print('el peso del bulto excede la capacidad restante')  
        return False         
            


        
# funcionalidad
boing = Boing()
sn = 's'
while sn == 's':
    sn = 'n'
    b = pedirBulto()
    if not b == None: 
        if boing.agregarBulto(b):
            if not boing.noExcedePesoTotal():
                print('-- maximo alcanzado --')
                break
            sn = confirmar()
            continue
    d = boing.espacioDisponible()
    if d > 0:
        print('espacio disponible =',d)
        sn = confirmar()

bultos = boing.bultos
totalIngresados = len(boing.bultos)
masPesado = max(boing.bultos)
masLiviano = min(boing.bultos)
pesoPromedio = statistics.mean(boing.bultos)
ingresos = boing.totalIngresos

print('\n detalle bultos:',bultos)
print('a) total bultos ingresados para el vuelo:',totalIngresados)
print('b) bulto mas pesado:',masPesado,'kg / bulto mas liviano:',masLiviano,'kg')
print('c) peso promedio de los bultos',pesoPromedio,'kg')
print('d) ingresos por conceptos de carga:',ingresos,'$')
print('*** by rkb.lenin@gmail.com ***')

