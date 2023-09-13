# calculate personal tax - with functions

#(1)
def getIncomeTax(salary):
    allowance=11850
    taxBand1Limit=34500
    taxBand2Limit=150000

    if salary > allowance:
         taxableSalary=salary-allowance
    else:
         return "Your salary is below the threshold, you will not be taxed."

    if (taxableSalary - taxBand2Limit) > 0:
        print("True")
    else:
        print("False")

getIncomeTax(150001)
#userSalary = int(input("Please enter your salary to calculate your income tax: "))
#taxed = getIncomeTax(userSalary)
#print(taxed)