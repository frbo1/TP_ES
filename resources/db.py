import sqlite3
import csv

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS professores(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
name TEXT, photo BLOB)")

with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    line_count = 0
    for row in csv_reader:
        # row[0] : nome do professor
        # row[1] : photo url
        name = row[0]
        url = "C:\\Users\\User\\Documents\\TP_ES\\resources\\fotos-professores\\" + row[1]
        with open(url, 'rb') as f:
            photo = f.read()
        cursor.execute(""" INSERT INTO professores (name, photo) VALUES (?,?)""", (name,photo))
        conn.commit()


cursor.close()
conn.close()