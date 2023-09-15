class LetterCheck:
    
    def __init__(self):
        self.vowels=["a","e","i","o","u"]
        self.straightlines="AEFHIKLMNTVWXYZ"
        self.romannumerals="CDILMVX"

    def isvowel(self, letterinput):
        if letterinput in self.vowels:
            return True
        else:
            return False

    def islinestraight(self, letterinput):
        if letterinput in self.straightlines:
            return True
        else:
            return False

    def isromannumeral(self, letterinput):
        if letterinput in self.romannumerals:
            return True
        else:
            return False

letterchecker = LetterCheck()
print(letterchecker.isvowel("t"))
print(letterchecker.islinestraight("T"))
print(letterchecker.isromannumeral("I"))