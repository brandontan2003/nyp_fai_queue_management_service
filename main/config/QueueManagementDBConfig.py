import mysql.connector

# TODO: Retrieve DB Connections depending on the environment
# queue_management_db_connection = mysql.connector.connect(
#     host="queue-management-service-mysql",
#     port="3306",
#     user="admin",
#     password="admin",
#     database="queue_management_db"
# )

queue_management_db_connection = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="admin",
    password="admin",
    database="queue_management_db"
)


