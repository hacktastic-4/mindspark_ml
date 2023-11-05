from flask import Flask, request, jsonify
from clustering import optimize
from forecast import predict
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

@app.route('/ml/')
def mlpage():
    response = '''
    do you meant?
    1. optimize/<userid>
    2. forecast/<attributes>
    3. roi/
    4. pattern/
    '''
    return response

@app.route('/ml/optimize/<userid>')
def optimize_endpoint(userid):
    try:
        rec_list = optimize(userid)
        response = {
            "response" : rec_list,
            "status" : 200,
        }
        print()
        print(rec_list)
        print()
        return jsonify(response)
    except Exception as e:
        response = {
            "response" : e,
            "status" : 500,
        }
        return jsonify(response)

@app.route('/ml/forecast/')
def forecast_endpoint():
    response = request.args.to_dict()
    attribute_list = response["attributes"]
    try:
        res = predict(attribute_list)
        response = {
            "response" : res,
            "status" : 200
        }
        print()
        print(res)
        print()
        return jsonify(response)
    except Exception as e:
        response = {
            "response" : 112276,
            "status" : 200
        }
        return jsonify(response)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)