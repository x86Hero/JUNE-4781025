# factorial

userNum=int(input("Please enter a number: ")) # (2)
factorialResult = userNum

while userNum >= 2: # (3)
    userNum -= 1
    factorialResult = userNum * factorialResult

print(factorialResult) # (3)