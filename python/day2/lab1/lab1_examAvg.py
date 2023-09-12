# Exam Average

for count in range(10**100):
    mathMark=int(input("Please enter the students Math score (0-100): "))
    if mathMark >= 0 and mathMark <= 100:
        break

for count in range(10**100):
    englishMark=int(input("Please enter the students English score (0-100): "))
    if englishMark >= 0 and englishMark <= 100:
        break

for count in range(10**100):
    ictMark=int(input("Please enter the students ICT score (0-100): "))
    if ictMark >= 0 and ictMark <= 100:
        break

averageMark = (mathMark + englishMark + ictMark) / 3
totalMark = mathMark + englishMark + ictMark

if averageMark >= 65:
    print("Pass")
    print("Average:", averageMark)
    print("Total Mark:", totalMark, "/ 300")
elif averageMark < 65:
    print("Fail")
    print("Average:", averageMark)
    print("Total Mark:", totalMark, "/ 300")