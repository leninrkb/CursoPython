import db
import utils

global CURSOR
CURSOR = db.setupConnection()

def getEmpleados(cursor=CURSOR):
    sql = 'select * from empleado'
    try:
        cursor.execute(sql)
        empleados = cursor.fetchall()
        res = []
        for empleado in empleados:
            e = {}
            e['nombre'] = empleado[1]
            e['apellido'] = empleado[2]
            e['edad'] = utils.calcularEdad(empleado[3].strftime('%d-%m-%Y'))
            e['estado_civil'] = empleado[4]
            e['suscrito'] = empleado[5]
            e['pasatiempos'] = empleado[6].split(',')
            e['email'] = empleado[7]
            res.append(e)
        return res
    except Exception as e:
      print(f'error business -> getEmpleados(): {e}')