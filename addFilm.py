from dbConnectFilmflix import *
import time

def addFilm():

	films = []

	filmID = cursor.lastrowid

	title = input("Enter a film title: ")
	yearReleased = input("Enter the year released: ")
	rating = input("Enter film rating: ")
	duration = input("Enter film duration: ")
	genre = input("Enter film genre: ")

	films.append(filmID)
	films.append(title)
	films.append(yearReleased)
	films.append(rating)
	films.append(duration)
	films.append(genre)

	try:

		cursor.execute('INSERT INTO tblfilms VALUES(?,?,?,?,?,?)', films)
		conn.commit()
		print(f"{title} added to Films Table")

		time.sleep(3)

		cursor.execute('SELECT * FROM tblfilms')

		row = cursor.fetchall()

		for record in row:
			print(record)
	
	except:

		print(f"{title} not added!")

# addFilm()