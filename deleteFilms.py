from dbConnectFilmflix import * 
import readFilms
import time

def deleteFilms():

    readFilms.readFilms()

    idField = input("Enter the ID for the record to be deleted: ")

    cursor.execute("DELETE FROM tblfilms WHERE filmID=" + idField)
    conn.commit()

    print(f"Record {idField} deleted")

    time.sleep(3)

    readFilms.readFilms() 

# deleteFilms()