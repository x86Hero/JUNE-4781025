# Limits - input an integer between two limits

userInput=0
minVal=1
maxVal=10
attempts=0

while userInput < minVal or userInput > maxVal:
    userInput=int(input("Please enter a number between 1 and 10: "))
    attempts += 1
    if attempts == 3:
        userInput = None
        break

print(userInput)