# factorial

userNum=int(input("Please enter a number: ")) # (2)
factorialResult = userNum

while userNum > 0: # (3)
    if userNum > 1:
        factorialResult = (userNum - 1) * factorialResult
    userNum -= 1

print(factorialResult) # (3)