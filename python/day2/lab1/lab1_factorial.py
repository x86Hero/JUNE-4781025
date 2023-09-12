# factorial

userNum=int(input("Please enter a number: ")) # (2)
factorialResult = userNum

while userNum >= 2: # (3)
    userNum -= 1
    factorialResult = userNum * factorialResult

print(factorialResult) # (3)


# Better solution, doesnt destory user input.

userNum=int(input("Please enter a number: "))
factorialResult = userNum
count = 1

while count < userNum:
    factorialResult = factorialResult * count
    count += 1

print(factorialResult)