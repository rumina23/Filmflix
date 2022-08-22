from dbConnectFilmflix import * 

cursor.execute('SELECT * from tblfilms')
row = cursor.fetchall()
for record in row:
    print(record)

#readFilm()