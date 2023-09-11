# selection examples

# IF statement
# if <condition>: perform an action

# simple IF
x=True
if x is True:
    print(f"It is {x}!")


# IF with an else
num=int(input('Try to guess my number: '))
if num == 7:
    print("Wow you got it!")
else:
    print("Aha! That is not my number >:)")


# IF with if else
num=int(input('Try to guess my number: '))
if num == 7:
    print("Wow you got it!")
elif num==5 or num==6:
    print("You're close... but not correct!")
else:
    print("Aha! That is not my number >:)")

# nesting IF
if num != 7:
    if num > 0 and num < 10:
        print('you are close...')
    elif num >= 10:
        print('guessing too high')
    elif num <= 0:
        print('it is not a negative number!')
else:
    print('spot on!')