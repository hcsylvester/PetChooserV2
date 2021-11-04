# Hunter C. Sylvester
# Purpose: Creating a Pet Class that allows a user to set and get a pet's age, name, owner's name, animal type, and
#          animal id
# The Pets class
#
# Properties
#  Pet Age: getPetAge(), setPetAge()
#  Pet Name: getPetName(), setPetName()
#  Owner Name: getOwnerName(), setOwnerName()
#  Animal Type: getAnimalType(), setAnimalType()
#  Animal ID: getAnimalId(), setAnimalId()
#

class Pets:
    # Private Properties
    __petAge: int = 1
    __petName: str = ""

    __ownerName: str = ""
    __animalType: str = ""
    __animalId: int = 1

    ########################
    # Instantiate a copy of this class
    def __init__(self,
                petAge = 1,
                petName = "Bailey",
                ownerName = "Hunter",
                animalType = "chicken",
                animalId = 1):

        # Set all our properties
        self.setPetAge(petAge)
        self.setPetName(petName)
        self.setOwnerName(ownerName)
        self.setAnimalType(animalType)
        self.setAnimalId(animalId)

    ###############################################
    # Getter and Setter for the age of the pet
    def getPetAge(self):
        return(self.__petAge)

    def setPetAge(self, petAge):
        if petAge:
            self.__petAge = petAge

    ###############################################
    # Getter and Setter for the pet's name
    def getPetName(self):
        return(self.__petName)

    def setPetName(self, petName):
        if petName:
            self.__petName = petName

    ###############################################
    # Getter and Setter for the pet owner's name
    def getOwnerName(self):
        return (self.__ownerName)

    def setOwnerName(self, ownerName):
        if ownerName:
            self.__ownerName = ownerName

    ###############################################
    # Getter and Setter for the pet's animal type
    def getAnimalType(self):
        return (self.__animalType)

    def setAnimalType(self, animalType):
        if animalType:
            self.__animalType = animalType

    ###############################################
    # Getter and Setter for the pet's ID
    def getAnimalId(self):
        return (self.__animalId)

    def setAnimalId(self, animalId):
        if animalId:
            self.__animalId = animalId
