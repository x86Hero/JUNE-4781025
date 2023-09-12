# part 2

examMark=int(input("Please enter the students exam mark: "))
studentLevel=int(input("Please enter the students level (1 or 2): "))

if studentLevel == 1:
    if examMark < 1 or examMark > 100:
        print("Error: marks must be between 1 and 100")
    elif examMark < 50:
        print("Fail")
    elif examMark >= 50 and examMark <= 60:
        print("Pass")
    elif examMark >= 61 and examMark <= 70:
        print("Merit")
    else:
        print("Distinction")
elif studentLevel == 2:
    if examMark < 1 or examMark > 100:
        print("Error: marks must be between 1 and 100")
    elif examMark < 40:
        print("Fail")
    elif examMark >= 40 and examMark <= 50:
        print("Pass")
    elif examMark >= 51 and examMark <= 65:
        print("Merit")
    else:
        print("Distinction")
else:
    print("Error: student level must be 1 or 2")