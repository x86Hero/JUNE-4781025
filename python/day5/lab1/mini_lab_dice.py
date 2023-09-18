import random

class Dice:
    
    def __init__(self):
        self.d6=6
        self.d20=20
        self.d2=2
        self.d4=4

    def rolld6(self):
        value=random.randint(1,6)
        return value

    def rolld20(self):
        value=random.randint(1,20)
        return value

    def rolld2(self):
        value=random.randint(1,2)
        return value

    def rolld4(self):
        value=random.randint(1,4)
        return value


dice = Dice()
print(dice.rolld20())
print(dice.rolld6())
print(dice.rolld2())
print(dice.rolld4())

