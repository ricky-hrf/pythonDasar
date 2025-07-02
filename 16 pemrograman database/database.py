import sqlite3

connection = sqlite3.connect("database.db")
conn = connection.cursor()

# create table
conn.execute("CREATE TABLE IF NOT EXISTS mahasiswa(npm INTEGER, nama TEXT)")

# insert data
conn.execute("INSERT INTO mahasiswa (npm,nama) VALUES(12345, 'Tri')")
connection.commit()

# menampilkan data
conn.execute("SELECT * FROM mahasiswa")
rows = conn.fetchall()

for row in rows:
  print(row)

conn.close()
connection.close()