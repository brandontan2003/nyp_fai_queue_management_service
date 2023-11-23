import mysql.connector
import os
env = os.environ.get('ENVIRONMENT', 'local')  # Default to development if ENVIRONMENT is not set

if env == 'development':
    from main.config.config_dev import DB_CONFIG
elif env == 'local':
    from main.config.config_local import DB_CONFIG
else:
    raise ValueError(f"Invalid environment: {env}")


queue_management_db_connection = mysql.connector.connect(**DB_CONFIG)


