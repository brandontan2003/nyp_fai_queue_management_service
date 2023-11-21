retrieve_queue_transaction_by_transaction_id = "SELECT * FROM queue_transaction_table WHERE transaction_id = '%s'"

insert_into_queue_transaction_sql = '''INSERT INTO queue_transaction_table (transaction_id, symptoms, status) 
VALUES (%s, %s, %s)'''

update_queue_transaction_sql = "UPDATE queue_transaction_table SET status = '%s' WHERE transaction_id = '%s'"
