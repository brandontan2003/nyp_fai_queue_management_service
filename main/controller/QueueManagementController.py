from flask import Flask, request

from main.constant.ApiStatusConstant import post
from main.constant.QueueManagementConstant import webhook

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True


@app.route(webhook, methods=[post])
def webhook():
    req = request.get_json(force=True)
    print(req)
    return {
        'fulfillmentText': 'This is a sample response from your webhook!'
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
