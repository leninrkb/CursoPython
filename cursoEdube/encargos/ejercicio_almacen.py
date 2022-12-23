class Pieza():
    def __init__(self):
        self.nombre=''
        self.cantidad=0
        
class Sucursal():
    def __init__(self):
        self.piezas=[]
        self.nombre=''
        
    def repartoPiezas(self,p):
        print('\nreparto piezas ',self.nombre)
        for i in range(len(p)):
            newp = Pieza()
            newp.nombre = p[i].nombre
            mn = self.nombre +', '+ newp.nombre+' cantidad: '
            newp.cantidad = int(input(mn))
            self.piezas.append(newp)
    
    def piezaMenorCantidad(self):
        menor = self.piezas[0]
        for i in range(len(self.piezas)):
            if self.piezas[i].cantidad < menor.cantidad:
                menor = self.piezas[i]
        return menor
        
    def totalPiezas(self):
        t=0
        for i in range(len(self.piezas)):
            t+=self.piezas[i].cantidad
        return t
    
class Almacen():
    def __init__(self):
        self.sucursales=[]
        self.piezas=[]
        
    def ingresoPiezas(self):
        n = int(input('\n# piezas a ingresar: '))
        for i in range(n):
            p = Pieza()
            p.nombre = input('nombre de la pieza: ')
            self.piezas.append(p)
    
    def ingresoSucursales(self):
        n = int(input('\n# sucursales a ingresar: '))
        for i in range(n):
            s = Sucursal()
            s.nombre = input('\nnombre de la sucursal: ')
            s.repartoPiezas(self.piezas)
            self.sucursales.append(s)
            
    def verPiezas(self):
        print('\nPiezas en el almacen')
        for i in range(len(self.piezas)):
            print((i+1),'-pieza: ',self.piezas[i].nombre)
            
    def verSucursales(self):
        print('\nSucursales')
        for i in range(len(self.sucursales)):
            print((i+1),'-sucursal: ',self.sucursales[i].nombre)
    
    def totalPiezasPorSucursal(self):
        print('\nTotal piezas por sucursal')
        for i in range(len(self.sucursales)):
            s = self.sucursales[i]
            print('\nsucursal ',s.nombre,' tiene: ',len(s.piezas),' piezas')
            for j in range(len(s.piezas)):
                p = s.piezas
                print('pieza: ',p[j].nombre,' - cantidad: ',p[j].cantidad)
                
    def piezaMenorCantidadSucursal(self):
        print('\nPieza menor existe sucursales')
        for i in range(len(self.sucursales)):
            p = self.sucursales[i].piezaMenorCantidad()
            print('sucursal: ',self.sucursales[i].nombre,' - pieza: ',p.nombre,' - cantidad: ',p.cantidad)
            
    def sucursalConMayorCantidadPiezas(self):
        total=0
        print('\nSucursal con mas del 50% de piezas')
        for i in range(len(self.sucursales)):
            total+=self.sucursales[i].totalPiezas()
        for i in range(len(self.sucursales)):
            per = round((self.sucursales[i].totalPiezas()*100/total),0)
            if per >= 50:
                print('sucursal: ',self.sucursales[i].nombre,' con ',per,'%')
    
    
a = Almacen()
a.ingresoPiezas()
a.verPiezas()
a.ingresoSucursales()
a.verSucursales()
a.totalPiezasPorSucursal()
a.piezaMenorCantidadSucursal()
a.sucursalConMayorCantidadPiezas()
