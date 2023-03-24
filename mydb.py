import mysql.connector

dataBase = mysql.connector.connect(
    host = 'localhost',
    user = 'diallodeveloper',
    password = 'passer'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_db")

print("All Done!")

