from datetime import *
import mysql.connector

from main.constant.GenerateTransactionIdConstant import *
from main.constant.QueueManagementConstant import date_pattern_format


class TransactionIDGenerator:
    def __init__(self, prefix="T"):
        self.prefix = prefix
        # TODO: Retrieve DB Connections depending on the environment
        self.connection = mysql.connector.connect(
            host="localhost",
            port="3307",
            user="admin",
            password="admin",
            database="queue_management_db"
        )
        self.cursor = self.connection.cursor()
        self.current_date = datetime.now().strftime("%Y-%m-%d")

    def check_date(self):
        self.cursor.execute(query_date_from_transaction_id)
        try:
            last_date = self.cursor.fetchone()[0]
            if str(last_date) != self.current_date:
                # Reset the running number for the new day
                self.cursor.execute(insert_default_value_transaction_id)
                self.connection.commit()
        except:
            self.cursor.execute(insert_default_value_transaction_id)
            self.connection.commit()

    def generate_transaction_id(self):
        self.check_date()

        # Retrieve the current running number
        self.cursor.execute(select_id_from_generate_transaction_id)
        database_number = self.cursor.fetchone()[0]
        new_running_number = database_number + 1

        # Update the running number
        self.cursor.execute(update_new_transaction_id % new_running_number)
        self.connection.commit()

        str_date = str(date.today().strftime(date_pattern_format))
        # Create the transaction ID
        transaction_id = f"{self.prefix}{str_date}{new_running_number:05d}"

        return transaction_id


# Test Transaction ID Generator
generator = TransactionIDGenerator()
print(generator.generate_transaction_id())
print(generator.generate_transaction_id())

