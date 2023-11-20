from flask import Flask, request

from main.constant.ApiStatusConstant import post
from main.constant.QueueManagementConstant import webhook, registration_successful_response, appointment_booking
from main.data.entity.ResponsePayload import ResponsePayload
from main.data.service.GenerateTransactionIdService import TransactionIDGenerator

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Transaction ID Generator Class
generator = TransactionIDGenerator()


@app.route(webhook, methods=[post])
def webhook():
    dialogflow_request = request.get_json(force=True)
    transaction_id = generator.generate_transaction_id()
    # print(dialogflow_request)
    if dialogflow_request["queryResult"]["intent"]["displayName"] == appointment_booking:
        return ResponsePayload(registration_successful_response + transaction_id).to_dict()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080, debug=True)
