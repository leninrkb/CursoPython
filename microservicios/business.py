import db

global CURSOR
CURSOR = db.setupConnection()

def getEmpleados(cursor=CURSOR):
    sql = 'select * from empleado'
    try:
        cursor.execute(sql)
        empleados = cursor.fetchall()
        return empleados
    except Exception as e:
      print(f'error business -> getEmpleados(): {e}')
    