
# the idea of 'self'
# better atrtibute assignation

class Login:
    
    def __init__(self,passeduser,passedpass,passedserver):
        self.username=passeduser
        self.password=passedpass
        self.server=passedserver

    def login(self):
        return "You have logged in to:", self.server, "as:", self.username

    def emailcheck(self):
        self.login()
        return "You got mail in: ",self.server

    def privacyviolation(self,otheraccount):
        otheraccountdata = [otheraccount.username,otheraccount.password,otheraccount.server]
        otheraccount.login()
        return otheraccountdata

gmail = Login("ashley","pass","gmail.com")
hotmail = Login("ian","pass","hotmail.co.uk")
yahoo = Login("brice","pass","yahoo.com")

print(gmail.login())
print(hotmail.login())
print(yahoo.login())

print(gmail.privacyviolation(yahoo))
gmail.privacyviolation(yahoo)