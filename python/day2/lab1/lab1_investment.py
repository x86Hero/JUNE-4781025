# investments

investment=int(input("Please enter your initial investment amount: "))
interestRate=float(input("Please enter the yearly interest rate: "))
targetValue=int(input("Please enter the target amount: "))
interestEarned=investment / 10
years=0

while investment < targetValue:
    investment = investment + interestEarned
    years += 1

print("It will take you",years,"to reach",targetValue,"with the",interestRate, "% offered.")