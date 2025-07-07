import mysql.connector

# Replace with your connection details
mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Sword2bear.",
    database="alx_book_store"
)

print("Connected to MySQL Server version:", mydb.server_info)

cursor = mydb.cursor()
cursor.execute("SHOW TABLES;")
for table in cursor:
    print(table)

