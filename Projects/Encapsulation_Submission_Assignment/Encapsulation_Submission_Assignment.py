class Person:                       # Created class Person.
    def __init__(self, name, age):  # Initiated Person with properties name and age.
        self.__name = name          # Set name.
        self._age = age             # Set age.

    def getName(self):              # Made a function to call on __name.
        print(self.__name)
    

person = Person("Bob", 25)          # Inserted arguments for Person.


print(person._age)                  # "print()" is able to be utilized for protected classes.
person.getName()                    # However, private classes must be called on with a function.
print(person.__name)                # This line will return an error.
