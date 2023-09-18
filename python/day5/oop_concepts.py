"""
4 core concepts

Inheritance - inheriting atrtibutes or functions
Polymorphism - inheritance but with change
Encapsulation - multiple data and functions inside a single object
Abstraction - hiding the complexity behind the functionality, the end user can see what they want to do, but dont know how its done.

overloading - can do different things depending on the context, for example using '+' = str + str will concatinate, but int + int will add numbers.

"""

# Abstraction class example

from abc import ABC, abstractmethod

class Bird(ABC):

    def __init__(self,reproductioncount):
        self.reproductioncount = reproductioncount

    @abstractmethod # decorator - this means every time you inherit the bird class, you must rewrite the 'eat' class.
    def eat(self):
        pass

    def communicate(self):
        return "tweet"


class Finch(Bird):
    
    def eat(self):
        return "Worms yummy!"


class Penguin(Bird):
    
    def eat(self):
        return "Fish yummy!"




# Testing 
fred = Finch(2)
print(fred.communicate())
print(fred.eat())

pingu = Penguin(1)
print(pingu.eat())