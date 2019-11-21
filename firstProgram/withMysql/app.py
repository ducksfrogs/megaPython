import mysql.connector

conn = mysql.connector.connect(
   user='masanari',
   password="dddd",
   host='108.167.122',
   database='databeseneme'
)

cursor = conn.cursor()

query = cursor.execute("SELECT * FROM dictonary WHERE Expression = 'inlay'")
results = cursor.fetchall()
print(results[0])