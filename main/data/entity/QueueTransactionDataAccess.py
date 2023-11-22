from main.config.QueueManagementDBConfig import queue_management_db_connection
from main.constant.QueueManagementConstant import transaction_id_not_found, in_queue, cancelled, registered, \
    transaction_status_already_cancelled, transaction_status_already_registered, transaction_cancelled_successfully, \
    transaction_registered_successfully, next_in_line_success, invalid_transaction_status
from main.constant.QueueTransactionDatabaseConstant import retrieve_queue_transaction_by_transaction_id, \
    insert_into_queue_transaction_sql, update_queue_transaction_sql, retrieve_waiting_time_by_transaction_id
from main.data.entity.QueueTransaction import QueueTransaction
from main.data.entity.ResponsePayload import ResponsePayload
from main.data.service.QueueManagementService import get_waiting_time


class QueueTransactionDataAccess:
    def __init__(self):
        self.connection = queue_management_db_connection
        self.cursor = self.connection.cursor()

    def insert_queue_transaction_record(self, transaction_id, symptoms, status):
        self.cursor.execute(insert_into_queue_transaction_sql, (transaction_id, symptoms, status))
        self.connection.commit()

    def update_transaction_record(self, transaction_id, status):
        self.cursor.execute(retrieve_queue_transaction_by_transaction_id % transaction_id)
        result = self.cursor.fetchone()
        queue = QueueTransaction(transaction_id=result[0], symptoms=result[1], status=result[2])

        if result:
            if queue.status == in_queue and status == cancelled:
                self.cursor.execute(update_queue_transaction_sql % (status, transaction_id))
                self.connection.commit()
                return ResponsePayload(transaction_cancelled_successfully % transaction_id).to_dict()

            elif queue.status == in_queue and status == registered:
                self.cursor.execute(update_queue_transaction_sql % (status, transaction_id))
                self.connection.commit()
                return ResponsePayload(transaction_registered_successfully % transaction_id).to_dict()

            elif queue.status == cancelled:
                return ResponsePayload(transaction_status_already_cancelled).to_dict()

            elif queue.status == registered:
                return ResponsePayload(transaction_status_already_registered).to_dict()
            else:
                return ResponsePayload(transaction_id_not_found).to_dict()
        else:
            return ResponsePayload(transaction_id_not_found).to_dict()

    def retrieve_waiting_time_by_transaction_id(self, transaction_id, status):
        self.cursor.execute(retrieve_queue_transaction_by_transaction_id % transaction_id)
        result = self.cursor.fetchone()
        queue = QueueTransaction(transaction_id=result[0], symptoms=result[1], status=result[2])

        if result:
            if queue.status == cancelled or queue.status == registered:
                return ResponsePayload(invalid_transaction_status).to_dict()
            self.cursor.execute(retrieve_waiting_time_by_transaction_id % (status, transaction_id))
            queue_result = self.cursor.fetchone()[0]
            if queue_result == 1:
                return ResponsePayload(next_in_line_success).to_dict()
            else:
                return get_waiting_time(queue_result)
        else:
            return ResponsePayload(transaction_id_not_found).to_dict()
