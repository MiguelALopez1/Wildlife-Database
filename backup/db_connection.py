import mysql.connector

# Set up the database connection
conn = mysql.connector.connect(
    host='73.171.45.18',
    user='remote_user',
    password='sqlhokies',
    database='wildlife_call_database'
)

