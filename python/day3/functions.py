import math # import the math module and everything that comes with it.
from string import capwords # import function capwords from the string module.
from calendar import monthcalendar as mnth # import a function monthcalendar from calendar module, and rename it to 'mnth'

# test before cast.
while True: # infinite loop.

    input1 = input("Num1: ")
    input2 = input("Num2: ")

    if input1.isnumeric():
        if input2.isnumeric():
            print(float(input1)+float(input2))
        else:
            print("Num2 needs to be a number...")
    else:
        print("Num1 needs to be a number... ")