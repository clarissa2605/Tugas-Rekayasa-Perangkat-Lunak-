import sqlite3

conn = sqlite3.connect("carbon_footprint.db")
c = conn.cursor()

c.execute("SELECT * FROM footprint_data")
rows = c.fetchall()

for row in rows:
    print(f"ID: {row[0]}, Nama: {row[1]}, Tanggal: {row[2]}, Jejak Karbon: {row[3]} kg CO₂")

conn.close()

