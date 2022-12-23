def dias(i):
    i+=1
    if i == 1: return 'lunes'
    if i == 2: return 'martes'
    if i == 3: return 'miercoles'
    if i == 4: return 'jueves'
    if i == 5: return 'viernes'
    if i == 6: return 'sabado'
    if i == 7: return 'domingo'

def regiones(i):
    i+=1
    if i == 1: return 'region insular'
    if i == 2: return 'region costa'
    if i == 3: return 'region sierra'
    if i == 4: return 'region oriente'

def ingresoRegion(region):
    r = Region()
    r.region = region
    print('*** '+region+' precipitaciones ***')
    r.dias = [int(input('dia '+dias(i)+': '))for i in range(7)]
    return r

class Region():
    def __init__(self):
        self.dias=[]
        self.region=''
        self.porcentajes=[]

    def numeroDiasPrecipitaciones(self):
        n = self.dias.count(0)
        return n

    def totalPrecipitaciones(self):
        t=0
        for i in range(len(self.dias)):
            t+=self.dias[i]
        return t

    def porcentajePrecipitacionesPorDia(self):
        t = self.totalPrecipitaciones()
        print('\nregion: '+self.region)
        for i in range(len(self.dias)):
            p = round((self.dias[i]*100/t),0)
            self.porcentajes.append(p)
            print('dia: '+dias(i),' porcentaje: '+str(p)+'%')

    def dosDiasMenosLLuviosos(self):
        print('\nlos dos dias menos lluviosos en la region '+self.region+' son')
        self.dias.sort()
        print('el dia '+dias(0)+' con '+str(self.dias[0]))
        print('el dia '+dias(1)+' con '+str(self.dias[1]))

class Reporte():
    def __init__(self):
        self.regiones=[]
        self.nregiones=0

    def mostrarPorcentajes(self):
        for i in range(len(self.regiones)):
            self.regiones[i].porcentajePrecipitacionesPorDia()

    def ingreso(self):
        r=4
        for i in range(r):
            self.regiones.append(ingresoRegion(regiones(i)))
    def diasMenosLLuvia(self):
        for i in range(len(self.regiones)):
            self.regiones[i].dosDiasMenosLLuviosos()

    def regionesNoPrecipitaciones(self):
        noPrecipitaciones=[]
        for i in range(self.nregiones):
            if self.regiones[i].numeroDiasPrecipitaciones() >= 2:
                noPrecipitaciones.append(reporte.regiones[i].region)
        print(f"Las regiones que no presentaron precipitaciones al menos 2 días a la semana: {noPrecipitaciones}")


reporte = Reporte()
reporte.nregiones=4
reporte.ingreso()

reporte.regionesNoPrecipitaciones()
reporte.mostrarPorcentajes()
reporte.diasMenosLLuvia()