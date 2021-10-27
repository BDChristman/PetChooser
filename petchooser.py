# Brian D. Christman
# Purpose: To define the class and properties used in the Pets Chooser program (main.py).

# Define the class and private properties
class pets:
    # Private properties
    __name = "Herman"
    __id = 1
    __age = 0
    __owner = "Brian"
    __animal = "dog"

    # Class instantiator
    def __init__(self, name: str = "Herman", id: int = 1, age: int = 0, owner: str = "Brian", animal: str = "dog"):
        # Set all our properties
        self.setname(name)
        self.setid(id)
        self.setage(age)
        self.setowner(owner)
        self.setanimal(animal)

    # Getter for the __name property
    def getname(self):
        return self.__name

    # Setter for the __name property
    # Valid values are any strings (symbols and numbers allowed)
    def setname(self, name):
        try:
            if name:
                self.__name = name
        except Exception as e:
            raise ValueError(f"The pet's name is missing.")

# Getter for the __id property
    def getid(self, id):
        return self.__id

# Setter for the __id property
# Valid values are any integers
    def setid(self, id) -> None:
        try:
            if int(id):
                pass

        except Exception as e:
            raise TypeError(f"{id} is not an integer. This value must be changed.")

# Getter for the __age property
    def getage(self):
        return self.__age

# Setter for the __age property
# Valid values are integers greater than or equal to zero
    def setage(self, age):
        try:
            # Is the argument an integer?
            if int(age):
                pass

        except Exception as e:
            raise TypeError(f"{age} is not an integer. This value must be changed.")
        if int(age) >= 0:
            self.__age = age
        else:
            raise ValueError(f"{age} is not an integer greater than or equal to zero.")

 # Getter for the __owner property
    def getowner(self):
        return self.__owner

    # Setter for the __owner property
    # Valid values are any strings (symbols and numbers allowed)
    def setowner(self, owner):
        try:
            if owner:
                self.__owner = owner
        except Exception as e:
            raise ValueError(f"The owner's name is missing.")

            # Getter for the __animal property
    def getanimal(self):
        return self.__animal

        # Setter for the __animal property
        # Valid values are any strings (symbols and number allowed)
    def setanimal(self, animal):
        try:
            if animal:
                self.__animal = animal
        except Exception as e:
            raise ValueError(f"The animal's type is missing.")
