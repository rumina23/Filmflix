import time
from dbConnectFilmflix import *
def readFilms():
    time.sleep(2)
    cursor.execute('SELECT * from tblfilms')
    row = cursor.fetchall()
    for record in row:
        print(record)

#readFilm()