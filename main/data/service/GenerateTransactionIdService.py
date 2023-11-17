from datetime import *
import mysql.connector
from main.constant.QueueManagementConstant import date_pattern_format


# TODO: Reset Transaction ID on every new day
class TransactionIDGenerator:
    def __init__(self, prefix="T"):
        self.prefix = prefix
        self.connection = mysql.connector.connect(
            host="localhost",
            port="3307",
            user="admin",
            password="admin",
            database="queue_management_db"
        )
        self.cursor = self.connection.cursor()

    def generate_transaction_id(self):
        # Retrieve the current running number
        self.cursor.execute("SELECT id FROM generate_transaction_id;")

        try:
            database_number = self.cursor.fetchone()[0]
        except:
            # Insert new record in the database
            self.cursor.execute("INSERT INTO generate_transaction_id (id) VALUES (0);")
            database_number = 0
        new_running_number = database_number + 1

        # Update the running number
        self.cursor.execute("UPDATE generate_transaction_id SET id = %s;" % new_running_number)
        self.connection.commit()

        str_date = str(date.today().strftime(date_pattern_format))
        # Create the transaction ID
        transaction_id = f"{self.prefix}{str_date}{new_running_number:05d}"

        return transaction_id


# Test Transaction ID Generator
generator = TransactionIDGenerator()
print(generator.generate_transaction_id())
print(generator.generate_transaction_id())

