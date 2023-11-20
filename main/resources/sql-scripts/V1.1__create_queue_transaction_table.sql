CREATE TABLE IF NOT EXISTS queue_transaction_table (
    transaction_id VARCHAR(15) PRIMARY KEY,
    symptoms VARCHAR(255),
    status VARCHAR(10),
    created_date DATETIME(3) DEFAULT CURRENT_TIMESTAMP(3)

);