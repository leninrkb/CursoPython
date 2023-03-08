from flask import Flask, jsonify, make_response
import business as bs

app = Flask(__name__)
@app.route('/get_empleados')
def getEmpleados():
    try:
        response = make_response(jsonify(bs.getEmpleados()),200)
        return response
    except Exception as e:
        print(f'error app -> getEmpleados(): {e}')
        return make_response('error', 500)