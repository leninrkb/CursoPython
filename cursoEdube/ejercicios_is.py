# ejercicio 1
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

# ejercicio 2

# def meses(i):
#     i+=1
#     if i == 1: return 'enero'
#     if i == 2: return 'febrero'
#     if i == 3: return 'marzo'
#     if i == 4: return 'abril'
#     if i == 5: return 'mayo'
#     if i == 6: return 'junio'
#     if i == 7: return 'julio'
#     if i == 8: return 'agosto'
#     if i == 9: return 'septiembre'
#     if i == 10: return 'octubre'
#     if i == 11: return 'noviembre'
#     if i == 12: return 'diciembre'

# def ingresoValorMes(mes, sucursal):
#     ms = 'total ventas en $ de la sucursal '+str((sucursal+1))+' en el mes de '+str(mes)+': '
#     return int(input(ms))


# n=int(input('numero de sucursales: '))
# m=12
# comp = [[ingresoValorMes(meses(mes),sucursal) for mes in range(m)] for sucursal in range(n)]
# totalVentas=0
# totalVentasSucursal=[]
# mejorSucursal=0
# mejorSucursalTxt=''
# peorMesPorcentaje=100
# peorMesPorcentajeTxt=''

# for i in range(n):
#     totalVentas += sum(comp[i])
#     totalVentasSucursal.append(sum(comp[i]))

# for i in range(n):
#     for j in range(m):
#         p = (comp[i][j]/totalVentas)*100
#         if p < peorMesPorcentaje:
#             peorMesPorcentaje = p
#             peorMesPorcentajeTxt = meses(j)

# mejorSucursal = max(totalVentasSucursal)
# mejorSucursalTxt = f'Sucursal {totalVentasSucursal.index(mejorSucursal)+1}'

# print(f"""
#         ventas = {comp}
#         Total, de ventas de la compañía en $ = {totalVentas}
#         Total, de ventas por cada sucursal = {totalVentasSucursal}
#         Sucursal que más vendió durante el año = {mejorSucursalTxt} con {mejorSucursal}$
#         Mes que menos porcentaje de ventas tuvo en la compañía = {peorMesPorcentajeTxt} con {peorMesPorcentaje}%
#         """)


# ejercicio 2
# def ingresoValor(dia, region):
#     ms = 'precipitacion en '+region+' el dia '+str(dia)+': '
#     return int(input(ms))

# def dias(i):
#     i+=1
#     if i == 1: return 'lunes'
#     if i == 2: return 'martes'
#     if i == 3: return 'miercoles'
#     if i == 4: return 'jueves'
#     if i == 5: return 'viernes'
#     if i == 6: return 'sabado'
#     if i == 7: return 'domingo'

# def regiones(i):
#     i+=1
#     if i == 1: return 'region insular'
#     if i == 2: return 'region costa'
#     if i == 3: return 'region sierra'
#     if i == 4: return 'region oriente'

# n=4
# m=7
# comp = [[ingresoValor(dias(dia),regiones(region)) for dia in range(m)] for region in range(n)]





# print(f"""
#         regiones que no presentaron precipitaciones 
#         al menos 2 dias en la semana: 
        
#         """)