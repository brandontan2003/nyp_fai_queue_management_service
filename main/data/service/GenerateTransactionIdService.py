from datetime import *

from main.config.QueueManagementDBConfig import queue_management_db_connection
from main.constant.GenerateTransactionIdConstant import *
from main.constant.QueueManagementConstant import date_pattern_format


class TransactionIDGenerator:
    def __init__(self, prefix="T"):
        self.prefix = prefix
        self.connection = queue_management_db_connection
        self.cursor = self.connection.cursor()
        self.current_date = datetime.now().strftime("%Y-%m-%d")

    def check_date(self):
        self.cursor.execute(query_date_from_transaction_id)
        try:
            last_date = self.cursor.fetchone()[0]
            if str(last_date) != self.current_date:
                # Reset the running number for the new day
                self.cursor.execute(insert_default_trans_id_value)
                self.connection.commit()
                return 1
        except:
            self.cursor.execute(insert_default_trans_id_value)
            self.connection.commit()
            return 1
        return 0

    def generate_transaction_id(self):
        check_for_first = self.check_date()

        # Retrieve the current running number
        self.cursor.execute(select_id_from_generate_transaction_id)
        database_number = self.cursor.fetchone()[0]
        new_running_number = check_for_first + database_number + 1

        # Update the running number
        self.cursor.execute(update_new_transaction_id % new_running_number)
        self.connection.commit()

        str_date = str(date.today().strftime(date_pattern_format))
        # Create the transaction ID
        transaction_id = f"{self.prefix}{str_date}{new_running_number:05d}"

        return transaction_id

