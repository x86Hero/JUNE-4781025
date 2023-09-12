# part 2

examMark=int(input("Please enter the students exam mark: "))

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