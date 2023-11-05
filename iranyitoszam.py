from os.path import isfile
import sqlite3

if not isfile('iranyitoszam.db'):
    print('Adatbázis fájl nem található! Letöltés...')
    import urllib.request
    urllib.request.urlretrieve('https://github.com/Parancsmester/hungarian-towns/blob/main/iranyitoszam.db?raw=true', 'iranyitoszam.db')
    print('Kész!\n')

conn = sqlite3.connect('iranyitoszam.db')
'''conn.execute('CREATE TABLE IF NOT EXISTS iranyitoszam (id INT PRIMARY KEY NOT NULL, ksh INT NOT NULL, isz INT NOT NULL, megye_id INT NOT NULL, megye TEXT NOT NULL, telepules TEXT NOT NULL);')

with open('db.txt', 'r', encoding='UTF-8') as f:
    for i, v in enumerate(f.readlines()):
        if i == 0: continue
        conn.execute('INSERT INTO iranyitoszam (id, ksh, isz, megye_id, megye, telepules) VALUES (?, ?, ?, ?, ? ,?)', tuple(v.split()))
conn.commit()'''

while True:
    inp = (input('Város: '),)
    cursor = conn.execute('SELECT isz FROM iranyitoszam WHERE telepules=?;', inp)
    found = cursor.fetchall()
    if found == []:
        print('Nincs találat!\n')
        continue
    print('Irányítószám:', *[i[0] for i in found])

    if inp[0] != 'Budapest':
        cursor = conn.execute('SELECT megye FROM iranyitoszam WHERE telepules=?;', inp)
        found = cursor.fetchall()
        print(found[0][0], 'vármegye\n')
