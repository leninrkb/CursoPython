from flask import Flask, jsonify, make_response
import business as bs
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

@app.route('/get_empleados')
def getEmpleados():
    try:
        response = make_response(jsonify(bs.getEmpleados()),200)
        return response
    except Exception as e:
        print(f'error app -> getEmpleados(): {e}')
        return make_response('error', 500)