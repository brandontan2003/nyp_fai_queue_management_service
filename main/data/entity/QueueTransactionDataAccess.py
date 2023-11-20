from main.config.QueueManagementDBConfig import queue_management_db_connection
from main.constant.QueueManagementConstant import transaction_id_not_found
from main.constant.QueueTransactionDatabaseConstant import retrieve_queue_transaction_by_transaction_id
from main.data.entity.QueueTransaction import QueueTransaction
from main.data.entity.ResponsePayload import ResponsePayload


class QueueTransactionDataAccess:
    def __init__(self):
        self.connection = queue_management_db_connection
        self.cursor = self.connection.cursor()

    def get_queue_transaction_by_transaction_id(self, transaction_id):
        self.cursor.execute(retrieve_queue_transaction_by_transaction_id % transaction_id)
        result = self.cursor.fetchone()

        if result:
            return QueueTransaction(transaction_id=result[0], symptoms=result[1], status=result[2],
                                    created_date=result[3])
        else:
            return ResponsePayload(transaction_id_not_found)
