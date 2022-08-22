from dbConnectFilmflix import * 
import time


def filterGenre():

    genreDict = {'1':'Action', '2': 'Animation', '3': 'Comedy', '4':'Crime', '5': 'Fantasy', '6':'Fighting'}

    options = 0 

    while options not in ["1","2","3","4","5","6"]:
        print("\n1. Action\n2. Animation\n3. Comedy\n4. Crime\n5. Fantasy \n6. Fighting")

        options = input("\nWhich Genre do you want to filter? (1-6): ")

        if options not in ["1","2","3","4","5","6"]: 

            print("Not in the list of options")
        
        else:
            break

    time.sleep(2)
    cursor.execute(f"SELECT * from tblfilms WHERE genre = '{genreDict[options]}'")
    row = cursor.fetchall()
    for record in row:
        print(record)

#############################################################################################################


def filterRating():

    filterDict = {'1': 'G', '2': 'PG', '3': 'R'}

    options = 0 

    while options not in ["1","2","3"]:
        print("\n1. G\n2. PG\n3. R")

        options = input("\nWhich Rating do you want to filter? (1-3): ")

        if options not in ["1","2","3"]: 

            print("Not in the list of options")
        
        else:
            break

    time.sleep(2)
    cursor.execute(f"SELECT * from tblfilms WHERE rating = '{filterDict[options]}'")
    row = cursor.fetchall()
    for record in row:
        print(record)


#############################################################################################################


def filterReleaseYear():

    orderDict = {'1': 'ASC', '2': 'DESC'}

    options = 0 

    while options not in ["1","2",]:
        print("\n1. Ascending\n2. Descending")

        options = input("\nIn which order do you want to filter the release dates of the films? (1-2): ")

        if options not in ["1","2"]: 

            print("Not in the list of options")
        
        else:
            break

    time.sleep(2)
    cursor.execute(f"SELECT * from tblfilms ORDER BY yearReleased {orderDict[options]}")
    row = cursor.fetchall()
    for record in row:
        print(record)


#############################################################################################################


def filterFilms():

    options = 0

    while options not in ["1", "2", "3"]:

        print("What would you like to filter: \n 1. Genre \n 2. Rating \n 3. Release Dates")

        options = input("\nWhich category would you like to filter? (1-3): ")

        if options not in ["1","2","3"]: 

            print("Not in the list of options")
        
        elif options == "1":
            filterGenre()
        
        elif options == "2":
            filterRating()

        elif options == "3":
            filterReleaseYear()