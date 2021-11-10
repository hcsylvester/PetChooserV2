# Hunter Sylvester
# Purpose: Shows all pets from a SQL database and allows people to change a pet's age or name.  
#          This updates through the database as well.
#
# We need to install the mypysql library
# In the Terminal window (bottom of PyCharm), run
# pip3 install pymysql
# pip3 install cryptography

# Import pet class, module, and cred file for MySQL access
from petsClass import Pets
import pymysql.cursors
from creds import *

# Create a pet list that is empty for later use
petList = []

# Function that accesses sql pets data and inputs data into Pets class
def gatherData():
    # sql statement
    sqlSelect = """
      Select 
      pets.id as id, 
      pets.name as pets_name, 
      pets.age, 
      owners.name as owners_name, 
      types.animal_type from pets 
      join owners on pets.owner_id = owners.id 
      join types on pets.animal_type_id = types.id;

      """

    # Execute select
    cursor.execute(sqlSelect)

    # Loop through the specific sql statement reading data into petList for each row
    for row in cursor:
        variable = Pets(petName=row['pets_name'],
                        ownerName=row['owners_name'],
                        petAge=row['age'],
                        animalType=row['animal_type'],
                        animalId=row['id'])
        petList.append(variable)


# Connect to the database
try:
    myConnection = pymysql.connect(host=hostname,
                                   user=username,
                                   password=password,
                                   db=database,
                                   charset='utf8mb4',
                                   cursorclass=pymysql.cursors.DictCursor)

# If there is an exception
except Exception:
    print(f"Sorry, connection was not made to sql database.  Check mysql information is set correctly.")
    print()
    exit()

# Once connected, we execute a query
try:
    with myConnection.cursor() as cursor:

        # Runs the function to access sql with specific sql commands and gives the Pets data
        gatherData()

# If there is an exception
except Exception as e:
    print(f"Sorry, but the connection was not made. Check mysql information.")
    print()

# Close connection
finally:
    myConnection.close()
    print("Connection closed.")
    print("\n")

# Function that accesses sql pets data and allows a user to change pet name and age data while updating the database
def updatePet(newName):
    try:
        if 1 <= int(newName) <= 8 or int(newName) == 10:
            if int(newName) == 10:
                # Must subtract 2 due to the index starting at 0
                value = petList[int(newName) - 2]
                print(f"You have chosen to edit {value.getPetName()}, who is {value.getPetAge()} years old.")

                # New name variable
                newName = input(str("New name: [ENTER == no change]"))
                if str.upper(newName) == "QUIT":
                    print("None of the updates were saved.  The program will end now!")
                    exit()
                # This is to prevent space or tabs as a name or else it would make the name blank
                elif len(newName.strip()) > 0:
                    value.setPetName(newName)
                    print(f"The pet's name is now {value.getPetName()}")
                else:
                    print("The name was not changed!")
                    print()
            else:
                # Must subtract 1 due to the index starting at 0
                value = petList[int(newName) - 1]
                print(f"You have chosen to edit {value.getPetName()}, who is {value.getPetAge()} years old.")

                # New name variable
                newName = input(str("New name: [ENTER == no change]"))
                if str.upper(newName) == "QUIT":
                    print("None of the updates were saved.  The program will end now!")
                    exit()
                # This is to prevent space or tabs as a name or else it would make the name blank
                elif len(newName.strip()) > 0:
                    value.setPetName(newName)
                    print(f"The pet's name is now {value.getPetName()}")
                else:
                    print("The name was not changed!")
                    print()
        else:
            input(f'{newName} is not associated with one of the pets. No updates were made. The program will now end!\n')
            exit()

    # If there is an exception
    except Exception:
        print(f'{x} is not associated with one of the pets.  No updates were made.  The program will now end!')
        exit()

    # Pets new age variable
    newAge = input("New age: [ENTER == no change]")
    try:
        if str.upper(newAge) == "QUIT":
            print("None of the updates were saved.  The program will end now!")
            exit()
        elif newAge.isdigit():
            value.setPetAge(newAge)
            print(f"The pet's age is now {value.getPetAge()}")
        elif newAge == "":
            print("The age was not changed!")
        else:
            print("That was not a valid age! The age will not update.")

    except Exception:
        print(f'{newAge} is not an appropriate age.  No updates were made.  The program will now end!')
        exit()

# Connect to the database
    try:
        myConnection = pymysql.connect(host=hostname,
                                       user=username,
                                       password=password,
                                       db=database,
                                       charset='utf8mb4',
                                       cursorclass=pymysql.cursors.DictCursor)

    # If there is an exception
    except Exception:
        print(f"Sorry, connection was not made to sql database.  Check mysql information is set correctly.")
        exit()

    try:
        # Once connected, we execute a query
        with myConnection.cursor() as cursor:
            # sql statement
            sql = """
                    update pets
                    set
                    name = %s, 
                    age = %s
                    where
                    id = %s
                                """

            # Execute and commit query, inputting new pet name and pet age by animal id in database
            cursor.execute(sql, (value.getPetName(), value.getPetAge(), value.getAnimalId()))
            myConnection.commit()
            print(f"Database updated!")

    except Exception:
        print(f"An issue has occurred with the sql information. The program will now end.")
        exit()

    # Close connection###########################PetAgeChange######################################################PetAgeChange###########################
    finally:
        myConnection.close()
        print("Connection closed.")
        input("Press [ENTER] to continue")
        print("\n")

# Show the list of pets to person and let them choose one until they want to quit
while True:
    try:
        print("Please choose a pet from the list below:")

        # Prints each pet with id
        for i in petList:
            print(f"[{i.getAnimalId()}]  {i.getPetName()}")

        print("[Q] Quit")

        requestAnimal = input('Please enter a pet ID (integer) to see more info pertaining to that pet '
                              'or press [Q] to quit! \n')

        if str.upper(requestAnimal) == "Q":
            print("Thank you and have a nice day!")
            break

        elif 1 <= int(requestAnimal) <= 8 or int(requestAnimal) == 10:
            if int(requestAnimal) == 10:
                # Must subtract 2 due to the indexing of Rex
                value = petList[int(requestAnimal) - 2]
                print(f"{value.getPetName()} is {value.getPetAge()} years old.  "
                      f"{value.getPetName()} is a {value.getAnimalType()}.  "
                      f"{value.getPetName()}'s owner is {value.getOwnerName()}.")

                onward = input("Would you like to [C]ontinue, [Q]uit, or [E]dit this pet? \n")
                if str.upper(onward) == "Q":
                    print("Thank you and have a nice day!")
                    break

                elif str.upper(onward) == "E":
                    x = input("Which pet would you like to edit? \n")
                    updatePet(x)

                elif str.upper(onward) == "C":
                    continue

                else:
                    print("That was not one of the options.  The program will exit now!")
                    exit()

            else:
                # Must subtract 1 due to the index starting at 0
                value = petList[int(requestAnimal) - 1]
                print(f"{value.getPetName()} is {value.getPetAge()} years old.  "
                      f"{value.getPetName()} is a {value.getAnimalType()}.  "
                      f"{value.getPetName()}'s owner is {value.getOwnerName()}. \n")

                onward = input("Would you like to [C]ontinue, [Q]uit, or [E]dit this pet? \n")
                if str.upper(onward) == "Q":
                    print("Thank you and have a nice day!")
                    break

                elif str.upper(onward) == "E":
                    x = input("Which pet would you like to edit? \n")
                    updatePet(x)

                elif str.upper(onward) == "C":
                    continue

                else:
                    print("That was not one of the options.  The program will exit now!")
                    exit()

        else:
            input(f'{requestAnimal} is not associated with one of the pets. \nPlease press [ENTER] to continue! \n')

    except Exception:
        print(f'{requestAnimal} is not associated with one of the pets.  Remember, it must be one of their IDs or "Q" '
              f'to quit!')
        input("Press [ENTER] to continue!\n")
