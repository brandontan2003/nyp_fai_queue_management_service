import mysql.connector

queue_management_db_connection = mysql.connector.connect(
    host="localhost",
    port="3307",
    user="admin",
    password="admin",
    database="queue_management_db"
)


