from flask import Flask, request

from main.constant.ApiStatus import put
from main.constant.QueueManagementConstant import api_v1, id_validator

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route(api_v1 + id_validator, methods=[put])
def id_validation_controller():
    return {"result": request.json['id_number']}


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
