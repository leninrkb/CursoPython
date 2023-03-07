from flask import Flask
import business as bs

app = Flask(__name__)
@app.route('/get_saludo')
def getSaludo():
    return 'today is gonna be a great day!'

@app.route('/empleados_suscritos')
def getEmpleadosSuscritos():
    return bs.getEmpleadosSuscritos()