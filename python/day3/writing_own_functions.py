# writing your own fucntions

# basic
def myFunction():
    #code
    pass # this allows us to define nothing and just continue.


# example
def showTwo(): # defining the function
    print(2) # code bit

showTwo() # calling a function later on


# calculator example
def addTwo(userNum):
    if userNum.isnumeric() :
        print(int(userNum) + 2)
    else:
        print("You didnt provide a number...")

userNum = input("Give me a number: ")

addTwo(userNum)

# function with a return - doubling input into a list.
def doubler(userNum):
    return [userNum,userNum]

userNum = input("Give me a number: ")
doubledInput = doubler(userNum)
print(doubledInput)