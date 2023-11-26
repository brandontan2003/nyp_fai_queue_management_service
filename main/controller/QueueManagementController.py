import json

from flask import Flask, request, Response

from main.constant.ApiStatusConstant import post, put, status_error, bad_request_http_code, content_type, indent_level
from main.constant.QueueManagementConstant import *
from main.data.entity.ApiResponsePayload import ApiResponsePayload
from main.data.entity.QueueTransaction import QueueTransaction
from main.data.entity.QueueTransactionDataAccess import QueueTransactionDataAccess
from main.data.entity.ResponsePayload import ResponsePayload
from main.data.service.GenerateTransactionIdService import TransactionIDGenerator
from main.data.service.QueueManagementService import update_transaction_status_service

app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

# Transaction ID Generator Class
generator = TransactionIDGenerator()


@app.route(webhook, methods=[post])
def webhook():
    queue_repo = QueueTransactionDataAccess()
    dialogflow_request = request.get_json(force=True)
    if dialogflow_request[query_result][intent][display_name] == appointment_booking:
        symptoms = dialogflow_request[query_result][parameters][conditions]
        transaction_id = generator.generate_transaction_id()
        symptoms_db = ', '.join(symptoms)
        new_queue_transaction = QueueTransaction(transaction_id=transaction_id, symptoms=symptoms_db)
        queue_repo.insert_queue_transaction_record(new_queue_transaction.transaction_id, new_queue_transaction.symptoms,
                                                   new_queue_transaction.status)

        return ResponsePayload(registration_successful_response + transaction_id).to_dict()

    elif dialogflow_request[query_result][intent][display_name] == cancel_appointment:
        transaction_id = dialogflow_request[query_result][query_text]
        return queue_repo.update_transaction_record(transaction_id=transaction_id, status=cancelled)

    elif dialogflow_request[query_result][intent][display_name] == check_queue:
        transaction_id = dialogflow_request[query_result][query_text]
        return queue_repo.retrieve_waiting_time_by_transaction_id(transaction_id=transaction_id, status=in_queue)

    return ResponsePayload(something_went_wrong_error).to_dict()


@app.route(api_v1 + update_transaction_status, methods=[put])
def update_transaction_status_controller():
    try:
        transaction_id = request.json["transaction_id"]
        status = request.json["status"]
        return update_transaction_status_service(transaction_id, status)
    except:
        response = json.dumps(ApiResponsePayload(status_error, missing_mandatory_field).to_json(), indent=indent_level)
        return Response(response, bad_request_http_code, content_type=content_type)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
