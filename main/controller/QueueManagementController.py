from flask import Flask, request

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route("/api/v1/id-validator", methods=['PUT'])
def id_validation_controller():
    return {"result": request.json['id_number']}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
