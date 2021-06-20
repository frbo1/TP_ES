import sqlite3
import csv

#Código para popular tabelas do database (Código não precisa ser utilizado novamente)
#Este código serve apenas para mostrar o processo.

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("CREATE TABLE IF NOT EXISTS professores(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
name TEXT, photo BLOB)")

#Script para popular database com info. dos professores
"""
with open('data.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=';')
    for row in csv_reader:
        # row[0] : nome do professor
        # row[1] : photo url
        name = row[0]
        url = "C:\\Users\\User\\Documents\\TP_ES\\resources\\fotos-professores\\" + row[1]
        with open(url, 'rb') as f:
            photo = f.read()
            #cursor.execute...
        conn.commit()
"""
#cursor.execute(""" INSERT INTO professores (name, photo) VALUES (?,?)""", (name,photo))

cursor.execute("CREATE TABLE IF NOT EXISTS comentarios(id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL, \
prof_id REFERENCES professores(id), comment TEXT)")
conn.commit()

#Script para popular tabela de comentários
"""
with open('C:\\Users\\User\\Documents\\TP_ES\\resources\\data2.txt') as file:
    for row in file:
        # row[0] : nome do professor
        # row[1] : photo url
        # row[2] ... row[n] : comentários
        row = row.split(';')
        n = len(row)
        name = row[0]
        #prof_id = ...
        prof_id = prof_id.fetchone()[0]
        for i in range(2, n):
            if i == (n-1):
                row[i] = row[i].rstrip('\n')
            #cursor.execute...
            conn.commit()
"""
#prof_id = cursor.execute(""" SELECT id FROM professores WHERE name = (?) """, (name,))
#cursor.execute(""" INSERT INTO comentarios (prof_id,comment) VALUES (?,?) """, (prof_id,str(row[i])))


"""
url = "C:\\Users\\User\\Documents\\TP_ES\\resources\\fotos-professores\\marcos3.jpeg"
with open(url, 'rb') as f:
    photo = f.read()
    #cursor.execute...
    conn.commit()
"""
#cursor.execute(""" UPDATE professores SET photo = (?) WHERE name = (?)""", (photo,'Marcos Augusto Menezes Vieira'))


cursor.close()
conn.close()