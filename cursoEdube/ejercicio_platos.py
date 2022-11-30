class Plato(object):

    def __init__(self):
        self.ndias=7
        self.nombre=''
        self.dias=[]
        self.total=0

    def leer(self):
        self.nombre = input('nombre del plato: ')
        for i in range(self.ndias):
            mn = '# ventas de ' + str(self.nombre) + ' el dia ' + str((i+1)) + ': '
            self.dias.append(int(input(mn)))
    
    def calcularTotalVendido(self):
        self.total = sum(self.dias)


class Restaurante():

    def __init__(self):
        self.platos = []
        self.cantidadPlatos = 0
        self.menosVendido = None

    def ingresoPlatos(self):
        self.cantidadPlatos = int(input('# platos: '))
        for i in range(self.cantidadPlatos):
            p = Plato()
            p.leer()
            p.calcularTotalVendido()
            self.platos.append(p)

    def verPlatos(self):
        print('\nplatos en el restaurante:')
        for i in range(self.cantidadPlatos):
            print(' - ',self.platos[i].nombre)

    def calcularMenosVendido(self):
        self.menosVendido = self.platos[0]
        for i  in range(self.cantidadPlatos):
            if self.platos[i].total < self.menosVendido.total:
                self.menosVendido = self.platos[i]

        print('plato menos vendido es: ',self.menosVendido.nombre,' con ',self.menosVendido.total,' ventas')

    def calcularTotalPLatosVendidosPorDia(self):
        n = self.platos[0].ndias
        vec = [0 for i in range(n)]
        for i in range(n):
            for j in range(self.cantidadPlatos):
                vec[i]+=self.platos[j].dias[i]
        print(f"""
                                     L  M  X  J  V  S  D
            platos vendidos por dia: {vec}       
            """)




r = Restaurante()
r.ingresoPlatos()
r.verPlatos()
r.calcularMenosVendido()
r.calcularTotalPLatosVendidosPorDia()


