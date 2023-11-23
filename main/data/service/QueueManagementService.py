import json

from flask import Response

from main.constant.ApiStatusConstant import status_error, bad_request_http_code, content_type, indent_level
from main.constant.QueueManagementConstant import invalid_request_transaction_status, cancelled, registered
from main.data.entity.ApiResponsePayload import ApiResponsePayload
from main.data.entity.QueueTransactionDataAccess import QueueTransactionDataAccess


queue_repo = QueueTransactionDataAccess()


def update_transaction_status_service(transaction_id, status):
    if status.upper() == cancelled or status.upper() == registered:
        return queue_repo.update_transaction_status(transaction_id, status.upper())
    else:
        response = json.dumps(ApiResponsePayload(status_error, invalid_request_transaction_status).to_json(),
                              indent=indent_level)
        return Response(response, bad_request_http_code, content_type=content_type)
