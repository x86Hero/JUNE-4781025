# while loop
# basic form


x = 1

while x <= 7:
    print("Stage", x,"/ 7")
    x += 1

print("All stages complete.")


# stopping loops

userNum = int(input("Type in a number: "))

while userNum > 0:
    if userNum == 13:
        print("You have reached 13, the loop will now break")
        break
    print(userNum)
    userNum -= 1

# skipping iteration on conditions

userNum = int(input("Type in a number: "))

while userNum > 0:
    userNum -= 1
    if userNum == 13:
        print("13 is a sacred number, I will skip this!")
        continue
    print(userNum)