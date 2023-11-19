select_id_from_generate_transaction_id = "SELECT id FROM generate_transaction_id where created_date = CURRENT_DATE;"

update_new_transaction_id = "UPDATE generate_transaction_id SET id = %s WHERE created_date = CURRENT_DATE;"

query_date_from_transaction_id = "SELECT created_date FROM generate_transaction_id ORDER BY created_date DESC LIMIT 1;"

insert_default_value_transaction_id = "INSERT INTO generate_transaction_id (id, created_date) VALUES (0, CURRENT_DATE);"
