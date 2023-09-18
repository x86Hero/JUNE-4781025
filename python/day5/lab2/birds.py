from abc import ABC, abstractmethod
import random

class Bird():

    def __init__(self,reproductioncount):
        self.reproductioncount = reproductioncount
        
    @abstractmethod # decorator - this means every time you inherit the bird class, you must rewrite the 'eat' class.
    def extinct(self):
        pass

    @abstractmethod
    def eat(self):
        pass

    def flap(self):
        return "flap flap flap!"


class Owl(Bird):
    
    def extinct(self):
        return False

    def eat(self):
        return "Mouse! snap snap!"


class Dodo(Bird):
    
    def extinct(self):
        return True

    def eat(self):
        return "Fruit! gobble gobble"

dodo=Dodo(1)
owl=Owl(random.randint(4,7))

print(dodo.eat())
print(dodo.extinct())

print(owl.eat())
print(owl.extinct())