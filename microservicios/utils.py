from datetime import date

def calcularEdad(fecha):
    datos = fecha.split('-')
    hoy = date.today()
    edad = hoy.year - int(datos[2])
    meses = hoy.month - int(datos[1])
    # dias = hoy.day - int(datos[0])
    if meses < 0:
        meses = 12 + meses
        edad-=1
    return edad