select_id_from_generate_transaction_id = "SELECT id FROM generate_transaction_id;"

insert_default_id_to_generate_transaction_id = "INSERT INTO generate_transaction_id (id) VALUES (0);"

update_new_transaction_id = "UPDATE generate_transaction_id SET id = %s;"
