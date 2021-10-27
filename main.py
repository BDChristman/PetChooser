# Brian D. Christman
# Purpose: To import the pets database from sql and allow users to select a pet from the database and
# learn more about them.

# See https://pymysql.readthedocs.io/en/latest/index.html
#  We need to install the mypysql library
#  In the Terminal window (bottom of PyCharm), run
#  pip3 install pymysql

# Import all packages and information required for this program
import pymysql.cursors
from creds import *
from petchooser import *

# Create the pets dictionary and list for all pet id numbers
petsDict = {}
idList = []

# Define petsMenu function which will list the pets in the database and their corresponding id
# Fill in the idList with the pet id numbers
def petsmenu():
    for id in petsDict:
        print(f"[{id}] {petsDict[id].getname()}")
        idList.append(id)

# Define the petsData function which will read in the data from sql and store it in a dictionary
def petsdata():
    # Our sql statement, easy to read
    sqlSelect = """
      Select pets.name as name, pets.id as id, pets.age as age, owners.name as owner, 
      types.animal_type as animal from pets join owners on pets.owner_id = owners.id 
      join types on pets.animal_type_id = types.id;
      """
    # Execute select
    cursor.execute(sqlSelect)

    # Loop through all the results and store in dictionary
    for row in cursor:
        petinfo = pets(name=row['name'],
                       id=row['id'],
                       age=row['age'],
                       owner=row['owner'],
                       animal=row['animal'])
        petsDict[row['id']] = petinfo

# Connect to the database and alert if something goes wrong. Reads info from creds.py.
try:
    myConnection = pymysql.connect(host=hostname,
                                   user=username,
                                   password=password,
                                   db=database,
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

except Exception as e:
    print(f"An error has occurred. Cannot connect to the database. You have entered incorrect credentials.")
    print()
    exit()

# In the database, print and loop through the pet selection menu
try:
    with myConnection.cursor() as cursor:
        # ==================
        # Get and store the pets data in a dictionary
        petsdata()
        # Print the instructions to the pet selection menu and print the selection menu
        print("Welcome to the pet selection menu!")
        print("To learn more about one of the pets, enter the number found to left of their name.")
        print("To quit and exit the menu, enter 'Q' or 'q' in the selection prompt at any time.")
        petsmenu()

        # Define stopping values and allow user to choose the pet they'd like to learn about
        stop = ['Q', 'q']
        petSelection = input("Please enter the number of the pet you'd like to learn about: ")

        # Loop through the responses. If the choice is valid print the pet information
        # If the choice is to stop, stop the program. Otherwise, have the user choose again
        # Always show the selection table to the user again so they can better make their choice
        while True:
            if petSelection in stop:
                print("Thank you for learning about our pets! We hope to see you again!")
                break
            elif not petSelection.isnumeric():
                print("Your entry was not an integer corresponding to one of the pets.\n")
                petsmenu()
                petSelection = input("Please enter the number of the pet you'd like to learn more about: ")
            elif int(petSelection) < 0:
                print("Your entry was not an integer corresponding to one of the pets.\n")
                petsmenu()
                petSelection = input("Please enter the number of the pet you'd like to learn more about: ")
            elif int(petSelection) and int(petSelection) in idList:
                id = int(petSelection)
                print(f"You have chosen {petsDict[id].getname()}, the {petsDict[id].getage()} year old {petsDict[id].getanimal()} owned by {petsDict[id].getowner()}.\n")
                input("Press [ENTER] to continue. ")
                petsmenu()
                petSelection = input("Please enter the number of the pet you'd like to learn more about: ")
            else:
                print("Your entry was not an integer corresponding to one of the pets.\n")
                petsmenu()
                petSelection = input("Please enter the number of the pet you'd like to learn more about: ")

# Check for errors. If something went wrong, print what went wrong
except Exception as e:
    print(f"A non-integer was entered that did not correspond to one of the pets and also forced the program to close.")
    print()

# Close connection
finally:
    myConnection.close()
    print("Connection closed.")
