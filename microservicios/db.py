import pymysql

class Database:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host='localhost',#ip
                user='root',
                password='',
                db='vue'
            )
            self.cursor = self.connection.connect()
            print(f'conexion establecida')
        except Exception as e:
            print(f'error: {e}')
