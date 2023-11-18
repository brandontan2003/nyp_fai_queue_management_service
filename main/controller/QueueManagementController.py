from flask import Flask, request

from main.constant.ApiStatusConstant import post
from main.constant.QueueManagementConstant import webhook
from main.data.service.GenerateTransactionIdService import TransactionIDGenerator

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Transaction ID Generator Class
generator = TransactionIDGenerator()


@app.route(webhook, methods=[post])
def webhook():
    req = request.get_json(force=True)
    transaction_id = generator.generate_transaction_id()
    print(req)
    return {
        'fulfillmentText': 'This is a sample response from your webhook!' + transaction_id
    }


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
