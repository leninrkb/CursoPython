import pymysql

def setupConnection():
    try:
        connection = pymysql.connect(
            host='localhost',
            user='root',
            password='',
            database='vue'
        )
        cursor = connection.cursor()
        print(f'conexion establecida {type(cursor)}')
        return cursor
    except Exception as e:
        print(f'error db -> setupConnection(): {e}')
    

