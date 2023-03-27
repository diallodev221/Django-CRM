import mysql.connector
# import psycopg2

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    password='passer'
)

# prepare a cursor object
cursorObject = dataBase.cursor()

cursorObject.execute("CREATE DATABASE crm_db")


# conn = psycopg2.connect("dbname=django_crm user=postgres")

# cursorObject = conn.cursor()

# cursorObject.execute("SELECT * FROM django_crm")

# records = cursorObject.fetchall()


print("All Done!")
