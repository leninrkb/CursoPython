class Region():
    dias=[]
    region=''
    def numeroDiasPrecipitaciones(self):
        n = self.dias.count(0)
        return n


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

r=4
reg=[ingresoRegion(regiones(region)) for region in range(r)]
noPrecipitaciones=[]

for i in range(r):
    if reg[i].numeroDiasPrecipitaciones() >= 2:
        noPrecipitaciones.append(reg[i].region)

print(f"""
    Las regiones que no presentaron precipitaciones
    al menos 2 días a la semana: {noPrecipitaciones}
    El porcentaje de precipitaciones 
    por cada día de la semana:
""")