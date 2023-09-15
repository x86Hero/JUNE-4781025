# classes
# A programmatic object containing data and methods
# i.e variables and functions

# basic class
"""
class MyClass:

    attribute = "some data"

    def methodname(input):
        # <code for method>
        return value
"""

class Dog:

    breed="labrador"
    weight=40
    energy="High"

    # you must always include self in functions inside a class
    def communicate(self):
        return "Woof!"


# you never directly call the class code

# create an instance of a class
goldie = Dog()
bonnie = Dog()

# call a function from the instance
print(goldie.communicate())
print(type(bonnie))

# we are creating instances of dog, this means we can overwrite data in instances without affecting the class or other instances.

# change data within an instance
print(bonnie.energy)
bonnie.energy = "Low"
print(bonnie.energy)

# double '__' are internal methods, not to be called by the end user/instance(s)