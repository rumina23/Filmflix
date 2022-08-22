import readFilms 
import addFilm 
import updateFilms 
import deleteFilms 
import filterFilms


def menuOptions():

    options = 0 

    while options not in ["1","2","3","4","5","6"]:
        print(f"\nMenu Options\n1. View all Films.\n2. Add Films.\n3. Update Films.\n4. Delete Films.\n5. Filter Films.\n6. Exit")

        options = input("\nEnter one of the options above (1-6): ")

        if options not in ["1","2","3","4","5","6"]: 

            print("Not in the list of options")

    return  options

mainProgram = True

while mainProgram == True:

    mainMenu = menuOptions()

    if mainMenu == "1": 
       readFilms.readFilms()  # invoke/call the readSong subroutine

    elif mainMenu == "2":
        addFilm.addFilm()
          
    elif mainMenu =="3":
        print('Third')
        updateFilms.updateFilms()
    
    elif mainMenu == "4":
        print('Fourth')
        deleteFilms.deleteFilms()
    
    elif mainMenu == "5":
        print('5th')
        filterFilms.filterFilms()

    else:
        print('Else')
        mainProgram = False

input("Press Enter to exit: ")